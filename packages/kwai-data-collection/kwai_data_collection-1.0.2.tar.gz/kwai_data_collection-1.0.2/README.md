# kwai-data-collection
快手后台数据采集工具

## 安装
```bash
pip install kwai-data-collection
```

## 使用方法
### 连接浏览器
```python
from XhsDataCollection import Collector

collector = Collector()
collector.connect_browser(port=9527)
```

### 下载客服考核文件
```python
file_path = collector.im.data.download__assess__detail(
    date='2025-02-05',
    save_path=r'C:\Users\sanrose\Desktop\temp',
    save_name='快手客服数据_20250205',
    open_page=True,
)
```