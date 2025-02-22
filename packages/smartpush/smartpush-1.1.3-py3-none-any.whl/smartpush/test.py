# -*- codeing = utf-8 -*-
# @Time :2025/2/20 00:27
# @Author :luzebin
from smartpush.export.basic.ExcelExportChecker import check_excel_all

if __name__ == '__main__':
    oss1 = "https://cdn.smartpushedm.com/material_ec2/2025-02-19/4d98418295524ab1b52340c2ed2afa4a/AutoTest-%E5%9B%BA%E5%AE%9AB-2025-02-14%20%E5%88%9B%E5%BB%BA%E7%9A%84Email33%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    oss2 = "https://cdn.smartpushedm.com/material_ec2/2025-02-19/ddbe9965d83840199e678a66dc414518/%E8%90%A5%E9%94%80%E4%BB%BB%E5%8A%A1%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    print(check_excel_all(oss2, oss1))