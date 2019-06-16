import pickle
import json

"""
管理故事元素,练习json使用
"""


def write_element():
    with open("./story.json", encoding="utf-8") as f:
        # loads 只完成了反序列化，
        # load 只接收文件描述符，完成了读取文件和反序列化
        dic1 = json.load(f)
        # print(type(aa)) 字典类型
        with open("file.pkl", "wb") as f1:
            pickle.dump(dic1, f1)


if __name__ == '__main__':
    write_element()
