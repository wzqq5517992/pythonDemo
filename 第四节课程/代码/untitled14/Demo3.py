# 全局变量的修改

# 列表本身用于装在数据
list1 = []
# a是变量 数据依赖别人复制
a = 0

print(id(list1))
print(id(a))
list1.append('1')
a = 1
print(id(list1))
print(id(a))

# list1 是一个水杯，追加数据是append  相当于是注水
# a本身就是一个水，如果换了，就不是原来的水
list1 = []
a = 2
print(id(list1))
print(id(a))
# 总结来说，通过等号赋值的时候，id会改变，id改变了，原有变量就改变了

# 在函数中，是否使用global 取决于你对这个变量是否改变，也就是看等于号
# 如果用了等于号 改变了原有内容，就需要进行使用global进行声明
