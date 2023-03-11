# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 10:06 AM
# 文件名称: 综合练习使用自定义工具包.PY
import my_utils.str_util
from my_utils import file_util

file_util.print_file_info("d:/test.txt")

print(my_utils.str_util.str_reverse("aaaabbbb"))