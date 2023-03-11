# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/14/2023 7:31 PM
# 文件名称: 函数体验.PY

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len("abc")
my_len("1234")
my_len("abcdefg")

