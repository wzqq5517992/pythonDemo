from pyecharts import Pie
import pyecharts_snapshot

from pyecharts.engine import create_default_environment

from BillDetail import read_csv, get_payment_list, get_income_list, get_payment_list_detail

read_csv('jolin.csv')
total_payment = get_payment_list()
print("账单支出: %s" % str(total_payment))
total_income = get_income_list()
print("账单收入: %s" % str(total_income))
get_payment_list_detail()

attr = ["收入", "支出"]
v1 = [total_income, total_payment]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.render("./pie.html")
# env = create_default_environment("html")
# env.render_chart_to_file(pie, path="./pie.html")
print("运行成功")
