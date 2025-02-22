# -*- codeing = utf-8 -*-
# @Time :2025/2/20 00:27
# @Author :luzebin
from smartpush.export.basic.ExcelExportChecker import *
from smartpush.export.basic.ReadExcel import *

if __name__ == '__main__':
    oss1 = "https://cdn.smartpushedm.com/material_ec2/2025-02-20/ad9e1534b8134dd098e96813f17d4b4d/%E6%B5%8B%E8%AF%95flow%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%91%8A%E5%AF%BC%E5%87%BA%E5%8B%BF%E5%8A%A8%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    oss2 = "https://cdn.smartpushedm.com/material_ec2/2025-02-21/bbe660950493411d88b4a75ed0893ec8/%E6%B5%8B%E8%AF%95flow%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%91%8A%E5%AF%BC%E5%87%BA%E5%8B%BF%E5%8A%A8%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    # print(json.dumps(read_excel_and_write_to_dict(read_excel_csv_data(read_excel_from_oss(oss1))),ensure_ascii=False))

    # print((oss1, oss1))

    # expected_oss ="https://cdn.smartpushedm.com/material_ec2_prod/2025-02-20/dae941ec20964ca5b106407858676f89/%E7%BE%A4%E7%BB%84%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    # actual_oss = "https://cdn.smartpushedm.com/material_ec2_prod/2025-02-20/dae941ec20964ca5b106407858676f89/%E7%BE%A4%E7%BB%84%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    # #actual_oss= get_oss_address_with_retry("23161","https://cdn.smartpushedm.com/material_ec2_prod/2025-02-20/dae941ec20964ca5b106407858676f89/%E7%BE%A4%E7%BB%84%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx","",'{"page":1,"pageSize":10,"type":null,"status":null,"startTime":null,"endTime":null}')
    # res=read_excel_and_write_to_dict(read_excel_from_oss(actual_oss))
    # print(res)
    # print(check_excel_all(actual_oss,expected_oss))
    print(check_excel("all", actual_oss=oss1, expected_oss=oss2, skiprows=1))
    print(check_excel_all(oss2, oss1, skiprows=1))
