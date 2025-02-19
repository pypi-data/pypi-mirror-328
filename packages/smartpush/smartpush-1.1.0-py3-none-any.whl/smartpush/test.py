from smartpush.export.basic.ExcelExportChecker import check_excel_for_lu
from smartpush.export.basic.GetOssUrl import get_oss_address_with_retry
import urllib3

if __name__ == '__main__':
    # print(check_excel_for_lu("content",actual_oss="https://sl-smartfile.oss-ap-southeast-1.aliyuncs.com/material_ec2_prod/2025-01-20/fcb98e2965314ef2862db65760dcce1f/ab%E5%BC%B9%E7%AA%97%E6%B4%BB%E5%8A%A8-%E8%BD%AC%E5%8C%96%E7%8E%87%E8%8E%B7%E8%83%9C%E9%94%80%E5%94%AE%E9%A2%9D%E6%98%8E%E7%BB%86%E6%95%B0%E6%8D%AE.xlsx",expected_oss="https://sl-smartfile.oss-ap-southeast-1.aliyuncs.com/material_ec2_prod/2025-01-20/fcb98e2965314ef2862db65760dcce1f/ab%E5%BC%B9%E7%AA%97%E6%B4%BB%E5%8A%A8-%E8%BD%AC%E5%8C%96%E7%8E%87%E8%8E%B7%E8%83%9C%E9%94%80%E5%94%AE%E9%A2%9D%E6%98%8E%E7%BB%86%E6%95%B0%E6%8D%AE.xlsx"))


    _id = 10901
    url = "https://test.smartpushedm.com/api-em-ec2/bulkOps/query"
    requestHeaders = {
            'cookie': 'osudb_appid=SMARTPUSH;osudb_oar=#01#SID0000121BJe/0W0PdWQj0Wo/Cr4G9H5S58u/YpvUYbOxsyvHQXmU5iToD8h3GX0+/3Af1efOroDv2jIwJIPVx2F1/XCP08l/NOaWMIZ/xm1/ugKB7eA1k1akIdCSTOHJcJ95Ahp7Yz0cBgOwtr8OgF77WNxX;osudb_subappid=1;osudb_uid=4213785247;ecom_http_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDIwMTEyNDcsImp0aSI6IjY4M2E1NDg1LTEwYjAtNDRhZS04MGMxLWQ1MmFkN2YxNmViNCIsInVzZXJJbmZvIjp7ImlkIjowLCJ1c2VySWQiOiI0MjEzNzg1MjQ3IiwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImZlbGl4LnNoYW9Ac2hvcGxpbmVhcHAuY29tIiwidXNlclJvbGUiOiJvd25lciIsInBsYXRmb3JtVHlwZSI6Nywic3ViUGxhdGZvcm0iOjEsInBob25lIjoiIiwibGFuZ3VhZ2UiOiJ6aC1oYW5zLWNuIiwiYXV0aFR5cGUiOiIiLCJhdHRyaWJ1dGVzIjp7ImNvdW50cnlDb2RlIjoiQ04iLCJjdXJyZW5jeSI6IkpQWSIsImN1cnJlbmN5U3ltYm9sIjoiSlDCpSIsImRvbWFpbiI6InNtYXJ0cHVzaDQubXlzaG9wbGluZXN0Zy5jb20iLCJsYW5ndWFnZSI6ImVuIiwibWVyY2hhbnRFbWFpbCI6ImZlbGl4LnNoYW9Ac2hvcGxpbmUuY29tIiwibWVyY2hhbnROYW1lIjoiU21hcnRQdXNoNF9lYzJf6Ieq5Yqo5YyW5bqX6ZO6IiwicGhvbmUiOiIiLCJzY29wZUNoYW5nZWQiOmZhbHNlLCJzdGFmZkxhbmd1YWdlIjoiemgtaGFucy1jbiIsInN0YXR1cyI6MCwidGltZXpvbmUiOiJBc2lhL01hY2FvIn0sInN0b3JlSWQiOiIxNjQ0Mzk1OTIwNDQ0IiwiaGFuZGxlIjoic21hcnRwdXNoNCIsImVudiI6IkNOIiwic3RlIjoiIiwidmVyaWZ5IjoiIn0sImxvZ2luVGltZSI6MTczOTQxOTI0Nzg2OSwic2NvcGUiOlsiZW1haWwtbWFya2V0IiwiY29va2llIiwic2wtZWNvbS1lbWFpbC1tYXJrZXQtbmV3LXRlc3QiLCJlbWFpbC1tYXJrZXQtbmV3LWRldi1mcyIsImFwaS11Yy1lYzIiLCJhcGktc3UtZWMyIiwiYXBpLWVtLWVjMiIsImZsb3ctcGx1Z2luIl0sImNsaWVudF9pZCI6ImVtYWlsLW1hcmtldCJ9.PJGM1sSZyvxTriMK4e1g90krqBUq9OVNc5vEyKxsXyQ;',
            'Content-Type': 'application/json'}
    requestParams = {'page': 1, 'pageSize': 10, 'type': 'EXPORT', 'status': None, 'startTime': None, 'endTime': None}
    oss=get_oss_address_with_retry(_id, url, requestHeaders, requestParams, tries=1, delay=1, backoff=1)
    eexcelxcel = check_excel_for_lu("all",
                                    expected_oss=oss,
                                    actual_oss=oss)
    print(eexcelxcel)