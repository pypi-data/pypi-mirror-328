"""
客服数据模块数据采集
"""

from random import uniform
from time import sleep, time

from DrissionPage import Chromium

from .._utils import Utils
from ._dict import RequestData
from ._utils import clone__ktrace_str


class Urls:
    assess = 'https://im.kwaixiaodian.com/workbench/zone/data/assess'


class DataPacketUrls:
    assess__detail = (
        'https://im.kwaixiaodian.com/gateway/business/cs/get/data/center/examine/detail'
    )
    assess__download_task__create = (
        'https://im.kwaixiaodian.com/gateway/business/cs/get/export/data'
    )
    assess__download_task__list = (
        'https://im.kwaixiaodian.com/gateway/business/cs/get/export/list'
    )


class Data:
    def __init__(self, browser: Chromium):
        self._browser = browser
        self._timeout = 15

    def download__assess__detail(
        self,
        date: str,
        save_path: str,
        save_name: str,
        timeout: float = None,
        download_wait_count: int = None,
        open_page=False,
    ):
        """
        下载客服考核数据详情表单文件

        Args:
            download_wait_count: 下载等待次数, 默认为 30 次
            open_page: 是否打开页面, 如果为 False 则使用当前激活的页面
        Returns:
            下载的文件路径
        """

        _timeout = timeout if isinstance(timeout, (int, float)) else self._timeout
        _download_wait_count = (
            download_wait_count if isinstance(download_wait_count, int) else 30
        )

        page = (
            self._browser.new_tab() if open_page is True else self._browser.latest_tab
        )
        page.listen.start(
            targets=DataPacketUrls.assess__detail,
            method='POST',
            res_type='XHR',
        )
        if open_page is True:
            page.get(Urls.assess)
        else:
            reset_btn = page.ele('t:button@@text()=重 置', timeout=3)
            if not reset_btn:
                raise RuntimeError('未找到 [重置] 按钮')
            reset_btn.click(by_js=True)

        detail_packet = page.listen.wait(timeout=_timeout)
        if not detail_packet:
            raise TimeoutError('首次进入页面获取数据超时, 可能页面访问失败')

        req_headers = detail_packet.request.headers

        download_btn = page.ele('t:button@@text()=导出数据', timeout=3)
        if not download_btn:
            raise RuntimeError('未找到 [导出数据] 按钮')

        page.change_mode('s', go=False)

        ktrace_str = req_headers.get('ktrace-str', '') or ''

        pub_headers = {
            'kpf': req_headers.get('kpf'),
            'kpn': req_headers.get('kpn'),
            'Referer': req_headers.get('Referer'),
        }

        def create__download_task():
            """通过API创建下载任务"""
            timestamp = str(time() * 1000)[:-2]
            headers = {
                **pub_headers,
                'trace-str': clone__ktrace_str(ktrace_str, timestamp),
                'Trace-Id': f'1.0.0.{timestamp}',
            }
            prev_date = Utils.date_calculate(1, date)
            post_data = {
                **RequestData.data.assess__download_task__create,
                'currentStartDay': date,
                'currentEndDay': date,
                'compareStartDay': prev_date,
                'compareEndDay': prev_date,
            }
            response = page.post(
                DataPacketUrls.assess__download_task__create,
                json=post_data,
                headers=headers,
                timeout=_timeout,
            )
            resp_json: dict = response.json()
            if resp_json.get('result') != 1:
                raise RuntimeError(resp_json.get('error_msg'))

            request_id = resp_json.get('requestId')
            return request_id

        try:
            create__download_task()
        except Exception as e:
            raise RuntimeError(f'创建下载任务出错: {e}') from e

        def get__download_task():
            """通过API获取下载任务对象"""
            timestamp = str(time() * 1000)[:-2]
            headers = {
                **pub_headers,
                'trace-str': clone__ktrace_str(ktrace_str, timestamp),
                'Trace-Id': f'1.0.0.{timestamp}',
            }
            post_data = {'pageNum': 1, 'pageSize': 5}
            response = page.post(
                DataPacketUrls.assess__download_task__list,
                json=post_data,
                headers=headers,
                timeout=_timeout,
            )
            resp_json: dict = response.json()
            if resp_json.get('result') != 1:
                raise RuntimeError(resp_json.get('error_msg'))

            if 'data' not in resp_json:
                raise ValueError('任务列表数据包未找到 data 字段')

            data = resp_json.get('data')
            if not isinstance(data, dict):
                raise ValueError('任务列表数据包 data 字段非预期 dict 类型')

            if 'records' not in data:
                raise ValueError('任务列表数据包未找到 data.records 字段')

            records: list[dict] = data.get('records')
            if not isinstance(records, list):
                raise ValueError('任务列表数据包 data.records 字段非预期 list 类型')

            task: dict = next(
                filter(
                    lambda x: x.get('exportCondition') == '全部客服'
                    and x.get('calculateRange') == f'{date}~{date}',
                    records,
                ),
                None,
            )
            if not task:
                raise ValueError('未找到符合条件的下载任务')

            return task

        task = get__download_task()
        for _ in range(_download_wait_count):
            if task.get('status') == 2:
                break

            sleep(uniform(3.2, 3.5))
            task = get__download_task()
        else:
            raise TimeoutError('下载任务等待完成超时')

        page.change_mode('d', go=False)
        status, file_path = page.download(
            file_url=task.get('fileUrl'),
            save_path=save_path,
            rename=save_name,
            file_exists='overwrite',
            show_msg=False,
        )
        if status != 'success':
            raise RuntimeError('文件下载失败')

        if open_page is True:
            page.close()

        return file_path
