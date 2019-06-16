from pyecharts import Bar, Line
from BillDetail import read_csv, get_payment_list, get_income_list, get_payment_list_detail
from pyecharts.engine import create_default_environment

read_csv('jolin.csv')
total_payment = get_payment_list()
print("账单支出: %s" % str(total_payment))
total_income = get_income_list()
print("账单收入: %s" % str(total_income))
get_payment_list_detail()

attr = ["收入", "支出"]
v1 = [total_income, total_payment]
# v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
# bar.add("商家B", attr, v2, is_stack=True)
bar.render("./bar.html")
# env = create_default_environment("html")
# env.render_chart_to_file(bar, path="./bar.html")
print("执行结束")
