import unittest
from tools3 import ParamsGenerator

from tools3 import Caller
from tools3 import generate_test_params_to_php_data_provider


class TestParamsGenerator(unittest.TestCase):
    def test_parse(self):

        # 定义参数
        params = {
            "clearingForm": ["forward", "prepaid", "postpaid"],
            "clientNowPaySubmitOrderControl": ["T", "F"],
            "pay_status": [
                "oblig",
                "unoblig",
                "uncollect",
                "paided",
                "cancelled",
                "wait",
                "part",
            ],
            "pay_status_count": [0, 1],
        }

        # 用户自定义参数值格式化规则
        value_formatters = {
            "clearingForm": {
                "format": "default",
                "values": {
                    "forward": "现付",  # 将 "forward" 映射为 "正向"
                    "prepaid": "预付",  # 将 "prepaid" 映射为 "预付费"
                    "postpaid": "后付",  # 将 "postpaid" 映射为 "后付费"
                }
            },
            "clientNowPaySubmitOrderControl": {
                "format": "default",
                "values": {
                    "T": "启用",  # 将 "T" 映射为 "True"
                    "F": "禁用",  # 将 "F" 映射为 "False"
                }
            },
            "pay_status": {
                "format": "default",
                "values": {
                    "oblig": "待付款",  # 将 "oblig" 映射为 "待付款"
                    "unoblig": "待核销",  # 将 "unoblig" 映射为 "待核销"
                    "uncollect": "待收款",  # 将 "uncollect" 映射为 "待收款"
                    "paided": "已付款",  # 将 "paided" 映射为 "已付款"
                    "cancelled": "已取消",  # 将 "cancelled" 映射为 "已取消"
                    "wait": "待确认",  # 将 "wait" 映射为 "待确认"
                    "part": "部分确认",  # 将 "part" 映射为 "待处理"
                }
            },
            "pay_status_count": {
                "format": "default",
                "values": {
                    0: "没有订单",
                    1: "有订单"
                }
            }
        }

        # 定义预期结果（可以是固定值或动态生成函数）
        def dynamic_expected(case_data):
            """
            动态生成预期结果的函数
            :param case_data: 测试用例数据
            :return: 预期结果
            """
            if case_data["pay_status"] == "paided" and case_data["pay_status_count"] == 1:
                return {"has": True}
            else:
                return {"has": False}

        # 创建 TestCaseGenerator 实例
        params_generator = ParamsGenerator(
            params=params,
            value_formatters=value_formatters,
            expected=dynamic_expected,  # 传入动态生成函数
            include_field_names=False,
            separator="_",
        )

        # 生成测试用例
        params_generator.generate_cases()
        caller = Caller()
        file_name = caller.get_caller_filepath(".json")
        # 保存测试用例到 JSON 文件
        params_generator.save_to_json(file_name)
        self.assertTrue(True)

    def test_parse(self):

        params = {
            "can_use_integral": [None, "", "0", "1", "2"],
            "can_use_rebate": [None, "", "0", "1", "2"],
            "enable_integral": [None, "T", "F", "E"],
            "enable_rebate": [None, "T", "F", "E"],
        }

        # 用户自定义参数值格式化规则
        value_formatters = {
            "can_use_integral": {
                "format": "default",
                "values": {
                    None: "积分_null",
                    "": "积分_空字符串",
                    "0": "积分_数字零",
                    "1": "积分_是",
                    "2": "积分_否",
                }
            },
            "can_use_rebate": {
                "format": "default",
                "values": {
                    None: "返利_null",
                    "": "返利_空字符串",
                    "0": "返利_数字零",
                    "1": "返利_是",
                    "2": "返利_否",
                }
            },
            "enable_integral": {
                "format": "default",
                "values": {
                    None: "积分应用未安装",
                    "T": "积分应用已启用",
                    "F": "积分应用禁用",
                    "E": "积分应用已过期",
                }
            },
            "enable_rebate": {
                "format": "default",
                "values": {
                    None: "返利应用未安装",
                    "T": "返利应用已启用",
                    "F": "返利应用禁用",
                    "E": "返利应用已过期",
                }
            },
        }

        # 定义预期结果（可以是固定值或动态生成函数）
        def dynamic_expected(case_data):
            """
            动态生成预期结果的函数
            :param case_data: 测试用例数据
            :return: 预期结果
            """
            if case_data["enable_integral"] == "T" or case_data["enable_rebate"] == "T":
                return {
                    "hasException": True,
                }
            else:
                return {
                    "hasException": True,
                }

        generate_test_params_to_php_data_provider(
            params=params,
            value_formatters=value_formatters,
            expected=dynamic_expected,  # 传入动态生成函数
            include_field_names=False,
            separator="_",
        )