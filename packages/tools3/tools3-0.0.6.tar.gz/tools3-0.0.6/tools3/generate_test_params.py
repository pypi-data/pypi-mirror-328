from tools3 import ParamsGenerator, Caller
import json

def generate_test_params_json(params, value_formatters, expected, include_field_names=False, separator="_"):
    # 创建 TestCaseGenerator 实例
    params_generator = ParamsGenerator(
        params=params,
        value_formatters=value_formatters,
        expected=expected,  # 传入动态生成函数
        include_field_names=include_field_names,
        separator=separator,
    )

    # 生成测试用例
    params_generator.generate_cases()
    caller = Caller()
    file_name = caller.get_caller_filepath(".json", True, True, 2)
    # 保存测试用例到 JSON 文件
    params_generator.save_to_json(file_name)


def json_to_php_array(obj, indent=0):
    """
    将Python/JSON对象转换为PHP数组语法字符串,使用方括号语法

    参数:
        obj: Python对象(dict, list, str, int, float, bool, None)
        indent: 缩进级别(默认为0)

    返回:
        str: PHP数组语法的字符串
    """
    # 缩进字符串
    indent_str = "    " * indent

    # 处理None
    if obj is None:
        return "null"

    # 处理布尔值
    if isinstance(obj, bool):
        return "true" if obj else "false"

    # 处理数字
    if isinstance(obj, (int, float)):
        return str(obj)

    # 处理字符串
    if isinstance(obj, str):
        return f"'{obj}'"  # 使用单引号包裹字符串

    # 处理列表/数组
    if isinstance(obj, list):
        if not obj:  # 空列表
            return "[]"
        items = [f"{indent_str}    {json_to_php_array(item, indent + 1)}" for item in obj]
        return "[\n" + ",\n".join(items) + "\n" + indent_str + "]"

    # 处理字典/对象
    if isinstance(obj, dict):
        if not obj:  # 空字典
            return "[]"
        items = [f"{indent_str}    '{key}' => {json_to_php_array(value, indent + 1)}"
                for key, value in obj.items()]
        return "[\n" + ",\n".join(items) + "\n" + indent_str + "]"

    raise TypeError(f"Unsupported type: {type(obj)}")

def generate_test_params_to_php_data_provider(params, value_formatters, expected, include_field_names=False, separator="_"):
    # 创建 TestCaseGenerator 实例
    params_generator = ParamsGenerator(
        params=params,
        value_formatters=value_formatters,
        expected=expected,  # 传入动态生成函数
        include_field_names=include_field_names,
        separator=separator,
    )

    # 生成测试用例
    params_generator.generate_cases()
    caller = Caller()
    file_name = caller.get_caller_filepath(".json", True, True, 2)

    # 保存测试用例到 JSON 文件
    params_generator.save_to_json(file_name)

    # 从文件加载 JSON 数据
    with open(file_name, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 将 JSON 数据转换为 PHP 数组格式的字符串
    php_array = json_to_php_array(json_data)

    # PHP 模板
    php_template = '''
    function getDataProvider() {{
        $data = {php_array};  // 直接使用 PHP 数组
        $dataNew = [];
        foreach ($data as $item) {{
            $testcase = $item['case'];
            $data = $item['data'];
            $expected = $item['expected'];
            $dataNew[] = [
                $testcase,
                $data,
                $expected,
            ];
        }}
        return $dataNew;
    }}
    /**
     * @param string $testcase
     * @param $data
     * @param $expected
     * @return void
     * @dataProvider getDataProvider
     */
    public function testOk($testcase, $data, $expected)
    {{
        $this->assertEquals(true, true, $testcase);
    }}
    '''

    # 格式化并插入 PHP 数组
    php_code = php_template.format(php_array=php_array)
    php_file_name = caller.get_caller_filepath(".php.tpl", True, True, 2)

    # 将生成的 PHP 代码写入到 PHP 文件
    with open(php_file_name, 'w', encoding='utf-8') as php_file:
        php_file.write(php_code)

    print(f"PHP测试用例文件已生成并保存到： {php_file_name}")
