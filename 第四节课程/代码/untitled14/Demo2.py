import csv

# 需要声明全局变量
# 支出记录明细列表
payment_list = []
# 收入记录明细列表
income_list = []
# 支出多少笔数据
payment_num = 0
# 收入多少笔数据
income_num = 0


# 读取csv文件
def read_csv(filename):
    csv_file = csv.reader(open(filename, encoding="UTF-8"))
    count = 0
    for line in csv_file:
        if count >= 17:
            # 所有的详细信息
            # 嵌套函数
            bill_save_data(line)

        count += 1


# 区分收入和支出
def bill_save_data(line):
    global payment_num
    global income_num
    # 处理区分收入和支出，把数据源区分开
    print(line[4])
    if line[4] == '支出':
        payment_list.append(line)
        payment_num += 1
    else:
        income_list.append(line)
        income_num += 1
    # 列表是能直接追加数据的  但是数字不能直接追加数据


# 收入支出的求和


# 支出求和
def get_payment_list():
    # 思路
    # 1、遍历收入列表
    # 2、每行内容里面，获得多少钱
    # 3、求和的操作
    all = 0
    for item in payment_list:
        all += float(item[5][1:])
    return all


# 收入求和
def get_income_list():
    all = 0
    for item in income_list:
        all += float(item[5][1:])
    return all


# 支出明细归纳汇总
def get_payment_list_detail():
    # 保存在字典中
    payment_dict = {}
    for item in payment_list:
        x = payment_dict.get(item[2])
        if x == None:
            # 没有这个key，对字典进行赋值
            payment_dict[item[2]] = float(item[5][1:])
        else:
            # 字典中有key对应的value  取出value+现在的值
            payment_dict[item[2]] = payment_dict[item[2]] + float(item[5][1:])

    # 求支出的最大值
    max = 0
    max_title = ""
    for i in payment_dict:
        # print(i)
        # 遍历字典实际上是得到字典的key
        temp = payment_dict[i]
        if max < temp:
            max = temp
            max_title = i
    print("支出最大值:{},支付给:{}".format(max, max_title))


read_csv('jolin.csv')
print(payment_num)
print(income_num)
total_payment = get_payment_list()
print("账单支出: %s" % str(total_payment))
total_income = get_income_list()
print("账单收入: %s" % str(total_income))
get_payment_list_detail()
