'''
功能：读取输入的数字，并进行校验
参数：故事组成元素的dict
返回值：读取数字的list
'''
def read_nums(elements):
    # 获取故事的组成部分
    elements_keys = list(elements.keys())
    # 输入的数字
    nums = []
    # 每个组成部分元素的个数
    key_len = []
    # 输入样例
    exp = ""
    # 获取每个构成部分有多少元素
    for element in elements:
        key_len.append(len(elements[element]))
    print("请输入%d个数字空格隔开，分别代表%s，且分别不超过" % (len(elements_keys), elements_keys), end='')
    for i in key_len:
        print(i, end=' ')
        exp += "1 "
    print("如:"+exp)
    # 循环输入直到输入合法数据
    while True:
        read = input().split()
        if len(read) != len(elements_keys):
            print("请输入%d个随机数" % (len(elements_keys)))
            continue
        flag = True
        for i in range(0, len(read)):
            # 判断是否输入的是数字
            if read[i].isnumeric():
                n = int(read[i])
                # 判断输入数字有代表的元素
                if n <= 0 or n > key_len[i]:
                    flag = False
                    break
                else:
                    nums.append(n)
            # 输入非数字情况下的反馈
            else:
                flag = False
                break
        if flag:
            break
        else:
            # 如果本次输入不合法清空nums
            nums.clear()
            print("代表\"%s\"的位置得到一个%s，请保证为大于0且不超过%d的数字" % (elements_keys[i], read[i], key_len[i]))
            print("请重新输入")
    return nums


'''
功能：根据输入的数字拼接出特定故事
参数：故事组成元素的dict，输入的数字的list
返回值：故事字符串
'''
def make_story(elements, nums):
    # 获取故事的组成部分
    elements_keys = list(elements.keys())
    # 生成的故事
    story = ""
    # 循环拼接每一个组成部分
    for i in range(0, len(nums)):
        # 元素dict[key][value list下标]
        story += elements[elements_keys[i]][nums[i]-1]
    return story