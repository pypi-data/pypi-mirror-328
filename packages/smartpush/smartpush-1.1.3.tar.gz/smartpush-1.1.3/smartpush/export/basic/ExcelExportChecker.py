import json
from urllib.parse import unquote

from smartpush.export.basic.ReadExcel import *

"""
用于excel校验
"""
warnings.simplefilter("ignore")


def check_excel(check_type="content", **kwargs):
    """对比excel
    :param: type: 需要对比类型，
            枚举：content：对比两表格内容
                方式1：传参actual_oss和expected_oss，参数类型str,url
                放松1：传参actual和expected，参数类型list or dict
            excelName: 对比两表格文件名称
            all: 对比所有内容
    """
    try:
        if check_type == "content":
            if "actual" in kwargs.keys() and "expected" in kwargs.keys():
                return check_excel_content(actual=kwargs["actual"], expected=kwargs["expected"])
            else:
                return check_excel_content(
                    actual=read_excel_and_write_to_list(excel_data=read_excel_from_oss(url=kwargs["actual_oss"])),
                    expected=read_excel_and_write_to_list(excel_data=read_excel_from_oss(url=kwargs["expected_oss"]))
                )
        elif check_type == "excelName":
            return check_excel_name(actual_oss=kwargs["actual_oss"], expected_oss=kwargs["expected_oss"])
        elif check_type == "all":
            actual_content = read_excel_and_write_to_list(excel_data=read_excel_from_oss(url=kwargs["actual_oss"]))
            expected_content = read_excel_and_write_to_list(excel_data=read_excel_from_oss(url=kwargs["expected_oss"]))
            flag1, content_result = check_excel_content(actual=actual_content, expected=expected_content)
            flag2, name_result = check_excel_name(actual_oss=kwargs["actual_oss"], expected_oss=kwargs["expected_oss"])
            flag3, header_result = check_excel_header(actual=actual_content, expected=expected_content)
            return all([flag1, flag2, flag3]), {"文件名称": name_result, "导出内容": content_result, "表头比较:": header_result}
        else:
            return False, f"不支持此类型: {check_type}"
    except Exception as e:
        print(f"对比excel异常：{e}")
        return False, [e]


# 定义比较类型和对应处理函数的映射
comparison_functions = {
    # 内容
    "content": lambda kwargs: check_excel_content(kwargs["actual"], kwargs["expected"]),
    # excelName
    "excelName": lambda kwargs: check_excel_name(kwargs["actual_oss"], kwargs["expected_oss"]),
    'header': lambda kwargs: check_excel_header(kwargs["actual"], kwargs["expected"]),
    # 全部
    "all": lambda kwargs: check_excel_all(kwargs["actual_oss"], kwargs["expected_oss"])
}


def check_excel_for_lu(check_type="content", **kwargs):
    """对比excel
    :param: type: 需要对比类型，
            枚举：
            content：对比两表格内容
                方式1：传参actual_oss和expected_oss，参数类型str,url
                放松1：传参actual和expected，参数类型list or dict
            excelName: 对比两表格文件名称，传oss链接
            all: 对比所有内容，传oss链接
    """
    try:
        # 根据 check_type 获取对应的处理函数
        compare_func = comparison_functions.get(check_type)
        if compare_func:
            return compare_func(kwargs)
        else:
            return False, f"不支持此类型: {check_type}"
    except KeyError as ke:
        # raise ke
        print(f"类型对应参数缺失异常：{ke}")
        return False, [str(ke)]
    except Exception as e:
        print(f"对比 Excel 异常：{e}")
        return False, [str(e)]


def check_excel_content_form_dict(actual, expected):
    """
    通过 OSS URL 比较 Excel 内容,支持多sheet并且包含表头
    """
    expected, actual = read_excel_and_write_to_dict(actual), read_excel_and_write_to_dict(
        expected)
    return check_excel_content(actual=actual, expected=expected)


def check_excel_content_form_list(actual, expected):
    """
    通过 内容 比较 Excel 内容,不包含表头
    """
    expected, actual = read_excel_and_write_to_list(actual), read_excel_and_write_to_list(expected)
    return check_excel_content(actual=actual, expected=expected)


def check_excel_all(actual_oss, expected_oss):
    """
    校验所有内容
    """
    expected, actual = read_excel_from_oss(expected_oss), read_excel_from_oss(actual_oss)
    flag1, content_result = check_excel_content_form_dict(actual, expected)
    flag2, name_result = check_excel_name(actual_oss, expected_oss)
    flag3, header_result = check_excel_header(actual, expected)
    return all([flag1, flag2, flag3]), json.dumps({f"文件名称-{flag1}": name_result, f"导出内容-{flag2}": content_result,
                                                   f"表头校验-{flag3}": header_result},
                                                  ensure_ascii=False)


def check_excel_name(actual_oss, expected_oss):
    """校验excel文件名称
    :param actual_oss:实际oss链接
    :param actual_oss:预期oss链接
    """
    try:
        actual_name = unquote(actual_oss.split("/")[-1])
        expected_name = unquote(expected_oss.split("/")[-1])
        if actual_name == expected_name:
            return True, "excel文件名称-完成匹配"
        else:
            return False, f"excel文件名称-不匹配, 实际: {actual_name}, 预期: {expected_name}"
    except BaseException as msg:
        return False, f"excel文件名称-服务异常: {msg}"


def check_excel_content(actual, expected):
    """校验excel内容
       :param actual: 实际内容，list或dict类型
       :param expected:预期内容：list或dict类型
     """
    try:
        if actual == expected:
            return True, ["excel内容-完全匹配"]
        else:
            errors = []
            # 断言1：校验行数
            actual_num = len(actual)
            expected_num = len(expected)
            check_row = actual_num - expected_num
            if check_row == 0:
                errors.append("excel内容-预期和实际行数相等，为" + str(actual_num) + "行")
            else:
                errors.append(
                    "excel内容-行数和预期对比差" + check_row.__str__() + "行" + ", 实际:" + str(
                        actual_num) + "预期: " + str(
                        expected_num))
            # 断言不匹配行
            if check_row >= 0:
                num = len(expected)
            else:
                num = len(actual)
            if isinstance(actual, list) and isinstance(expected, list):
                for i in range(num):
                    if actual[i] == expected[i]:
                        continue
                    else:
                        errors.append(
                            "excel内容-第" + str(i + 1) + "行不匹配，预期为：" + str(expected[i]) + ", 实际为: " + str(
                                actual[i]))
                return False, errors
            else:
                return False, compare_dicts(actual, expected)
    except Exception as e:
        print(f"：excel内容-服务异常{e}")
        return False, [e]


def check_excel_header(actual, expected):
    """
    比较两个文档第一列的header是否一致
    @param actual:
    @param expected:
    @return:
    @return:
    """
    try:
        if all([isinstance(actual, str), isinstance(expected, str)]):
            actual, expected = read_excel_header(read_excel_from_oss(actual)), read_excel_from_oss(
                expected)
        else:
            actual, expected = read_excel_header(actual), read_excel_header(
                expected)
        if actual == expected:
            return True, "表头校验值与顺序一致"
        else:
            return False,"表头校验值与顺序失败"
    except:
        return False, "表头校验异常"


def del_temp_file(file_name=""):
    """删除temp下临时文件"""
    file_path = os.path.join(os.path.dirname(os.getcwd()) + "/temp_file/" + file_name)
    try:
        os.remove(file_path)
        print(f"文件 {file_path} 已成功删除。")
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    except Exception as e:
        print(f"删除文件 {file_path} 时出错：{e}")


def compare_dicts(dict1, dict2):
    diff = {}
    # 找出只在 dict1 中存在的键
    only_in_dict1 = set(dict1.keys()) - set(dict2.keys())
    if only_in_dict1:
        diff['only_in_dict1'] = {key: dict1[key] for key in only_in_dict1}
    # 找出只在 dict2 中存在的键
    only_in_dict2 = set(dict2.keys()) - set(dict1.keys())
    if only_in_dict2:
        diff['only_in_dict2'] = {key: dict2[key] for key in only_in_dict2}
    # 处理两个字典都有的键
    common_keys = set(dict1.keys()) & set(dict2.keys())
    for key in common_keys:
        value1 = dict1[key]
        value2 = dict2[key]
        if isinstance(value1, dict) and isinstance(value2, dict):
            # 如果值是字典，递归比较
            sub_diff = compare_dicts(value1, value2)
            if sub_diff:
                diff[f'different_sub_dicts_at_{key}'] = sub_diff
        elif isinstance(value1, list) and isinstance(value2, list):
            # 如果值是列表，比较列表元素
            if value1 != value2:
                diff[f'different_lists_at_{key}'] = (value1, value2)
        else:
            # 其他情况，直接比较值
            if value1 != value2:
                diff[f'different_values_at_{key}'] = (value1, value2)
    return diff
