# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 9:35 AM
# 文件名称: file_util.PY

def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常 原因是{e}")
    finally:
        if f:         #如果变量是None 表示false，如果有任何内容 true
            f.close()

def append_to_file(file_name,data):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("d:/test.txt")
    append_to_file("d:/test.txt","haha")