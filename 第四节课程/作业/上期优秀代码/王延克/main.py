
#导入获取资源文件的module
from module_resource import *

def main():
    """程序的主方法"""
    while True:
        time=get_num("请输入时间（1-4）,输入q退出程序：")
        if time == 0 :
            print("谢谢使用，程序退出。。。。。。")
            break
        time_str=get_time(time)
        person = get_num("请输人物（1-4）,输入q退出程序：")
        if person == 0:
            print("谢谢使用，程序退出。。。。。。")
            break
        person_str = get_person(person)
        addr = get_num("请输入地点（1-4）,输入q退出程序：")
        if addr == 0:
            print("谢谢使用，程序退出。。。。。。")
            break
        addr_str = get_addr(addr)
        event = get_num("请输入事件（1-4）,输入q退出程序：")
        if event == 0:
            print("谢谢使用，程序退出。。。。。。")
            break
        event_str = get_event(event)
        content = time_str + person_str + addr_str+event_str
        print(content)
        # 写入文件
        write_file(content+"\n")


def get_num(msg):
    """获取合法的数字"""
    while True:
        num = input(msg)
        if "1"==num or "2"==num or "3"==num or "4"==num :
            return int(num)
            break
        elif "q" == num or "Q"==num :
            return  0
            break
        else:
            print("输入有误，请重新输入")
            get_num(msg)



main()



