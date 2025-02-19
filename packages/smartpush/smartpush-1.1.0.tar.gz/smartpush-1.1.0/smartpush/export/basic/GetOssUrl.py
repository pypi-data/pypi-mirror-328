import requests
from retry import retry
import json
from smartpush.utils.StringUtils import StringUtils


def get_oss_address_with_retry(target_id, url, requestHeader, requestParam, **kwargs) -> str:
    """
    创建带有动态重试配置的获取 OSS 地址
    **kwargs 可传参：tries=10, delay=2, backoff=1
    :param requestParam:
    :param url:
    :param target_id:
    :param requestHeader:
    :return: 带有重试配置的获取 OSS 地址的
    """

    @retry(tries=10, delay=2, backoff=1)
    def get_oss_address():
        if StringUtils.is_empty(target_id):
            print(f"缺少参数:target_id")
            return
        try:
            response = requests.request(url=url, headers=requestHeader, data=json.dumps(requestParam), method="post")
            response.raise_for_status()
            result = response.json()
            id_url_dict = {item["id"]: item["url"] for item in result["resultData"]["datas"]}
            if target_id in id_url_dict:
                if len(id_url_dict[target_id]) == 1:
                    return id_url_dict[target_id][0]
                else:
                    raise ValueError(f"存在多条 id 为 {target_id} 的记录，记录为：{id_url_dict[target_id]}")
            else:
                raise ValueError(f"未找到 id 为 {target_id} 的记录，未包含有效的 OSS 地址,")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"响应数据格式错误,响应结果: {result},异常: {e}")
    return get_oss_address()