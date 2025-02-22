# from retry import retry
import json

import requests
import tenacity
from tenacity import retry, stop_after_attempt, wait_fixed

from smartpush.utils.StringUtils import StringUtils


# 用于技术第几次重试，无需修改
def log_attempt(retry_state):
    """
    回调函数，在每次重试时记录并打印重试次数
    """
    attempt_number = retry_state.attempt_number
    print(f"当前重试次数: {attempt_number}")


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
    tries = kwargs.get('tries', 10)  # 重试次数
    delay = kwargs.get('delay', 2)


    @retry(stop=stop_after_attempt(tries), wait=wait_fixed(delay), after=log_attempt)
    def get_oss_address():
        _url = url + '/bulkOps/query'
        result = None
        if StringUtils.is_empty(target_id):
            print(f"缺少参数:target_id")
            return
        try:
            response = requests.request(url=_url, headers=requestHeader, data=json.dumps(requestParam),
                                        method="post")
            response.raise_for_status()
            result = response.json()
            id_url_dict = {item["id"]: item["url"] for item in result["resultData"]["datas"]}
            if target_id in id_url_dict:
                if len(id_url_dict[target_id]) == 1:
                    print(f"{target_id} oss链接为：{id_url_dict[target_id][0]}")
                    return id_url_dict[target_id][0]
                else:
                    raise ValueError(f"存在多条 id 为 {target_id} 的记录，记录为：{id_url_dict[target_id]}")
            else:
                raise ValueError(f"未找到 id 为 {target_id} 的记录，未包含有效的 OSS 地址,")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"响应数据格式错误,响应结果: {result},异常: {e}")
        except requests.RequestException as e:
            print(f"请求发生异常: {e}，正在重试...")
            raise

    def cancel_export_file(_target_id):
        """
        用于失败后取消导出
        :param _target_id:
        :return:
        """
        cancel_url = url + '/bulkOps/cancel'
        response = requests.request(url=cancel_url, headers=requestHeader, params={'id': _target_id}, method="get")
        response.raise_for_status()
        result = response.json()
        print(f"获取Oss Url失败，取消 {_target_id} 的导出记录，响应：{result}")
        return result

    try:
        return get_oss_address()
    except Exception as e:
        # print(f"最终失败，错误信息: {e}")
        if isinstance(e, tenacity.RetryError):
            cancel_export_file(target_id)
        return None


if __name__ == '__main__':
    url = "https://test.smartpushedm.com/api-em-ec2"
    requestHeader = {
        "cookie": "osudb_appid=SMARTPUSH;osudb_oar=#01#SID0000122BBLon+0gwvStide+qtdJAK57ZSK1ty+iW8b7tv/Uwl6Zo4gDfUg6B83n+jgqTVjoZ5qRGyRsuLaXc9woDN2WRh3mu1yn7anglBmaFoemhCy/ttS8nqv/y0kj8khbu6mtBmQrseNfnO/Mir8PQP+S;osudb_subappid=1;osudb_uid=4213785247;ecom_http_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI1Mjk2NTQsImp0aSI6ImM2MTA4MGJkLTU4MGUtNDJiNi05NzU5LTU0ZTNmZDExZDA4OSIsInVzZXJJbmZvIjp7ImlkIjowLCJ1c2VySWQiOiI0MjEzNzg1MjQ3IiwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImZlbGl4LnNoYW9Ac2hvcGxpbmVhcHAuY29tIiwidXNlclJvbGUiOiJvd25lciIsInBsYXRmb3JtVHlwZSI6Nywic3ViUGxhdGZvcm0iOjEsInBob25lIjoiIiwibGFuZ3VhZ2UiOiJ6aC1oYW5zLWNuIiwiYXV0aFR5cGUiOiIiLCJhdHRyaWJ1dGVzIjp7ImNvdW50cnlDb2RlIjoiQ04iLCJjdXJyZW5jeSI6IkpQWSIsImN1cnJlbmN5U3ltYm9sIjoiSlDCpSIsImRvbWFpbiI6InNtYXJ0cHVzaDQubXlzaG9wbGluZXN0Zy5jb20iLCJsYW5ndWFnZSI6ImVuIiwibWVyY2hhbnRFbWFpbCI6ImZlbGl4LnNoYW9Ac2hvcGxpbmUuY29tIiwibWVyY2hhbnROYW1lIjoiU21hcnRQdXNoNF9lYzJf6Ieq5Yqo5YyW5bqX6ZO6IiwicGhvbmUiOiIiLCJzY29wZUNoYW5nZWQiOmZhbHNlLCJzdGFmZkxhbmd1YWdlIjoiemgtaGFucy1jbiIsInN0YXR1cyI6MCwidGltZXpvbmUiOiJBc2lhL01hY2FvIn0sInN0b3JlSWQiOiIxNjQ0Mzk1OTIwNDQ0IiwiaGFuZGxlIjoic21hcnRwdXNoNCIsImVudiI6IkNOIiwic3RlIjoiIiwidmVyaWZ5IjoiIn0sImxvZ2luVGltZSI6MTczOTkzNzY1NDc2Mywic2NvcGUiOlsiZW1haWwtbWFya2V0IiwiY29va2llIiwic2wtZWNvbS1lbWFpbC1tYXJrZXQtbmV3LXRlc3QiLCJlbWFpbC1tYXJrZXQtbmV3LWRldi1mcyIsImFwaS11Yy1lYzIiLCJhcGktc3UtZWMyIiwiYXBpLWVtLWVjMiIsImZsb3ctcGx1Z2luIl0sImNsaWVudF9pZCI6ImVtYWlsLW1hcmtldCJ9.X2Birt-jiWILAvEjjwknUchil2ys8Y11omeRYgZ3K0I;",
        "Content-Type": "application/json"
    }
    requestParam = {
        "page": 1,
        "pageSize": 20,
        "type": "EXPORT",
        "status": None,
        "startTime": 1740033265288,
        "endTime": 1740044065288
    }
    id = "2334659"
    get_oss_address_with_retry(2334659, url, requestHeader, requestParam)
