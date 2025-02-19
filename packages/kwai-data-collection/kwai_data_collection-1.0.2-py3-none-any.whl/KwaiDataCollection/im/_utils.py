from base64 import b64decode, b64encode
from random import randint


def clone__ktrace_str(ktrace_str: str, timestamp: str):
    """根据原始ktrace字符串克隆出一个新的ktrace字符串"""

    if not ktrace_str:
        return ktrace_str

    ktrace_str_list = ktrace_str.split('|')
    if len(ktrace_str_list) < 3:
        return ktrace_str

    # 3.4583698286736769.26681996.1739174169122.1048
    _timestamp = str(int(float(timestamp)))
    for i in range(1, 3):
        try:
            decode = b64decode(ktrace_str_list[i]).decode('utf-8')
            decode_list = decode.split('.')
            increment = int(decode_list[-1]) + 1
        except Exception:
            return ktrace_str

        r_list = [
            *decode_list[:2],
            str(randint(10000000, 88888888)),
            _timestamp,
            str(increment),
        ]
        r = '.'.join(r_list)
        ktrace_str_list[i] = b64encode(r.encode('utf-8')).decode('utf-8')

    return '|'.join(ktrace_str_list)
