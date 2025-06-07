def add(a :int|float, b: int | float) -> int | float:
    """
    功能：实现a+b的结果，并将结果返回
    a:数字类型，加数
    b:数字类型，被加数
    return: a+b的结果
    """
    return a + b


# print(add('a', 'b'))
# int()
# list()
# zip()



# 字符串创建的使用场景
# ''  ""  ''' '''  """ """

# 语法上，这四种方式都表示为字符串
str_1 = '''123456'''
print(str_1)


# 表示为一行字符串时，使用''  ""

str_2 = "hello' world"
str_3 = 'hello" world'

print(str_3)

# ''' '''  表示为注释

'''


'''
result = 1
def fun():
    result = 10
    def fun1():
        result = 20
        def fun2():
            result = 30
            def fun3():
                print(result)
            fun3()
        fun2()
    fun1()
fun()




'''

# 表示为多行字符串
str_4 = '''
西游记第一章
XXXXXX
xxxxxx
xxxxxx
xxxxxx
'''
print(str_4)