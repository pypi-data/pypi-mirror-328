import io
import json
import os
import re
import warnings
from io import BytesIO
from typing import Dict, Any

import pandas as pd
from pandas import DataFrame
from requests import request

warnings.simplefilter("ignore")


def read_excel_from_oss(url="", method="get"):
    """读取oss的excel内容转为io流数据"""
    try:
        result = request(method=method, url=url)
        excel_data = BytesIO(result.content)
        print(f"成功读取oss文件内容: {url}")
        return excel_data
    except Exception as e:
        print(f"读取oss报错 {url} 时出错：{e}")


def read_excel_header(excel_data, **kwargs) -> list:
    """
    1、根据oss link 直接读出excel的头列 list
    """
    try:
        dfs = read_excel_data(excel_data)
        result = []
        for sheet_name, df in dfs.items():
            result.append(df.keys().values.tolist())
        return result
    except Exception as e:
        print(f"excel生成header-list出错：{e}")


def read_excel_data(excel_data, **kwargs):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning, module=re.escape('openpyxl.styles.stylesheet'))
        dfs = pd.read_excel(excel_data, sheet_name=None, na_filter=False, **kwargs) if isinstance(excel_data,io.BytesIO) \
            else excel_data
        return dfs


def read_excel_and_write_to_dict(excel_data=None, file_name=None, **kwargs):
    """excel内容并写入到内存dict中
    :param excel_data：excel的io对象, 参数和file_name互斥
    :file_name: excel文件名称，目前读取check_file目录下文件，参数和excel_data互斥
    """
    try:
        if excel_data is not None and file_name is not None:
            pass
        elif file_name is not None:
            excel_data = os.path.join(os.path.dirname(os.getcwd()) + "/check_file/" + file_name)
        dfs = read_excel_data(excel_data)
        # 将DataFrame转换为字典，以行为单位存储数据
        row_dict = {}  # 创建一个空字典来存储按行转换的数据
        for sheet_name, row in dfs.items():
            row_dict[sheet_name] = row.to_dict(orient='records')
        return row_dict
    except Exception as e:
        print(f"excel写入dict时出错：{e}")


def read_excel_and_write_to_list(excel_data=None, sheet_name=None, file_name=None, **kwargs):
    """excel内容并写入到内存list中
    :param excel_data：excel的io对象, 参数和file_name互斥
    :file_name: excel文件名称，目前读取check_file目录下文件，参数和excel_data互斥
    """
    try:
        if excel_data is not None and file_name is not None:
            pass
        elif file_name is not None:
            excel_data = os.path.join(os.path.dirname(os.getcwd()) + "/check_file/" + file_name)
        dfs = read_excel_data(excel_data)
        rows_list = []
        # 多sheet处理
        for name, df in dfs.items():
            rows_list.append(df.values.tolist())
        if len(dfs) <= 1:
            rows_list = rows_list[0]
        return rows_list
    except Exception as e:
        print(f"excel写入list时出错：{e}")


def read_excel_and_write_to_csv(excel_data, file_name, **kwargs):
    """excel内容并写入到csv中"""
    try:
        df = pd.read_excel(excel_data, engine="openpyxl")
        local_csv_path = os.path.join(os.path.dirname(os.getcwd()) + "/temp_file/" + file_name)
        df.to_csv(local_csv_path, index=False, **kwargs)
        return local_csv_path
    except Exception as e:
        print(f"excel写入csv时出错：{e}")


def read_excel_data_for_oss_write_to_dict(oss, **kwargs) -> dict:
    """
    1、根据oss link 直接读出 dict-list
    2、支持多sheet，默认sheet_name =None查全部
    3、返回dict结构 {'sheet_name':[rows_list]}
    """
    try:
        dfs = read_excel_data(read_excel_from_oss(oss))
        result = {}
        for sheet_name, df in dfs.items():
            rows_list = df.values.tolist()
            result[sheet_name] = rows_list
        return result
    except Exception as e:
        print(f"excel生成dict出错：{e}")
