regex_cache = {}


def checkarg(**args):
    u'''参数检测装饰器'''

    def _checkarg(function):

        def __checkarg(**func_kw):
            for key in func_kw:
                if key in args:

                    # 要验证的值
                    value = func_kw[key]

                    # 验证规则
                    valid_rules = args[key]

                    # 检测空
                    allow_empty = valid_rules.get('allow_empty')
                    if not allow_empty:
                        if not value or not value.strip():
                            return Result(key + "_empty")
                    elif not value:
                        # 如果是空的并且忽略空检测,那么下面的就不需要检查了
                        continue;

                    # 检测长度
                    if 'min-length' in valid_rules:
                        min_length = valid_rules['min-length']
                        if min_length > len(value):
                            return Result(key + "_length")

                    if 'max-length' in valid_rules:
                        max_length = valid_rules['max-length']
                        if max_length < len(value):
                            return Result(key + "_length")

                    # 检测正则
                    if 'regex' in valid_rules:
                        # 获取编译后的正则
                        regex = valid_rules['regex']
                        regexcmp = regex_cache.get(regex)
                        if not regexcmp:
                            regexcmp = re.compile(regex)
                            regex_cache[regex] = regexcmp
                        if not regexcmp.search(value):
                            return Result(key + "_format")

                    # 检测其他逻辑
                    check_logics = valid_rules.get('check_logic')
                    if check_logics:
                        for logic in check_logics:
                            result = logic(**func_kw)
                            if not result[0]:
                                return Result(result[1])

            function(**func_kw)

        return __checkarg

    return _checkarg