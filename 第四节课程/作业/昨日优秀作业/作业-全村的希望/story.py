# 时间
def time(param):
    time = ['早上', '中午', '半夜']
    return time[param]
# 人物
def people(param):
    people = ['小明', '小李', '小白', '小黑']
    return people[param]
# 地点
def site(param):
    site = ['再房上', '在地下', '在电梯里', '在厕所里']
    return site[param]
# 时间
def event(param):
    event = ['吃饭', '遛狗', '飞翔', '看书']
    return event[param]
# 函数入口
def main():
    # 打印提示信息
    print('******************************************')
    print('  欢迎使用小说器，请按照提示输入数字^_^')
    print('******************************************')
    # 获取用户输入结果
    t = int(input('请选择时间(请随机输入0-2的数字)：'))
    p = int(input('请选择人物(请随机输入0-3的数字)：'))
    s = int(input('请选择地点(请随机输入0-3的数字)：'))
    e = int(input('请选择地点(请随机输入0-3的数字)：'))
    # 输入数据组装结果
    print("%s %s %s %s" %(time(t), people(p), site(s), event(e)))

if __name__ == "__main__":
    main()
