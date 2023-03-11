# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/16/2023 2:38 PM
# 文件名称: 字典.PY


my_dict = {"shaowenhao":100,"duxaiodan":99}
my_dict2 = {}
my_dict3 = dict()

print(f"字典1的内容{my_dict}它的类型{type(my_dict)}")
print(f"字典1的内容{my_dict2}它的类型{type(my_dict2)}")
print(f"字典1的内容{my_dict3}它的类型{type(my_dict3)}")

value = my_dict["shaowenhao"]
print(value)

#定义嵌套字典

stu_score_dict = {
    "shaowenhao":{
        "语文":100,
        "数学":120
    },
    "duxiaodan":{
        "语文": 99,
        "数学":118
    }
}

value = stu_score_dict["duxiaodan"]["语文"]
print(value)

