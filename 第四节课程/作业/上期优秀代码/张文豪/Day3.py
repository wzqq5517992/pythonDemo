"""
第三天作业
"""
import pickle
import os
import element


def gen_story(numin):
    """
    生成故事
    :param numin:
    :return 生成的故事:
    """
    try:
        f = None
        f = open("file.pkl", "rb")
        dic1 = pickle.load(f)
    except IOError:
        print("程序读取故事数据文件出错，请重新生成！")
        return
    except pickle.UnpicklingError:
        print("程序读取故事数据文件出错，请重新生成！")
        return

    finally:
        if f:
            f.close()
    t_story = ""
    s_time = dic1.get("时间")
    # 确保不会发生找不到故事元素的问题
    t_story += s_time[int(numin[0]) % len(s_time)]
    s_person = dic1.get("人物")
    t_story += s_person[int(numin[1]) % len(s_person)]
    s_site = dic1.get("地点")
    t_story += s_site[int(numin[2]) % len(s_site)]
    s_event = dic1.get("事件")
    t_story += s_event[int(numin[3]) % len(s_event)]
    return t_story


def save_story(story_str):
    # print(os.getcwd())
    if not os.path.exists("./storys"):
        os.mkdir("./storys")
    with open("./storys/story.txt", "a", encoding="utf-8") as f:
        f.write(story_str+"\n")
        f.flush()
        print("当前故事已保存")


if __name__ == '__main__':
    print("--------抽签游戏---------")
    element.write_element()
    while True:
        num_in = input("请出入四个数字开始游戏,输入q退出游戏:")
        if "q" == num_in.lower():
            break
        is_valid = num_in.isdigit() and len(num_in) == 4
        # 输入的是四位数字
        if is_valid:
            story = gen_story(num_in)
            if story:
                print(story)
                save_story(story)
        else:
            print("输入不符合规则，请重新输入！")
