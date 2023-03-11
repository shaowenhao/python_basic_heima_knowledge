# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 9:35 AM
# 文件名称: str_util.PY


def str_reverse(s):
    '''
    功能是字符串翻转
    :param s: 将被翻转的字符串
    :return: 翻转后的字符串
    '''
    return s[::-1]

def substr(s,x,y):
    """
    :param s: 将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return:  切片完成后的字符串
    """
    return s[x:y]

# 自测
if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("nihao", 2, 5))