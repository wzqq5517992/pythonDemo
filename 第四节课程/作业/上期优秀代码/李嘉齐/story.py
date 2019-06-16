import json
from story_utils import *

elements_file = open("elements.txt", 'r')
elements = json.loads(elements_file.read())
elements_file.close()
while True:
    nums = read_nums(elements)
    story = make_story(elements, nums)
    print("生成的故事为" + story)
    story_file = open("story.txt", 'a')
    story_file.write(json.dumps(nums) + ':' + story + '\n')
    story_file.close()
    print("故事已存到story.txt")
    print("是否继续？'q'退出,回车继续")
    ans = input()
    if ans == 'q':
        break

