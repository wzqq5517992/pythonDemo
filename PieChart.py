from pyecharts import Pie
import pyecharts_snapshot

from pyecharts.engine import create_default_environment

from BillDetail import read_csv, get_payment_list, get_income_list, get_payment_list_detail, payment_month_list

read_csv('jolin.csv')
total_payment = get_payment_list()
print("账单支出: %s" % str(total_payment))
total_income = get_income_list()
print("账单收入: %s" % str(total_income))
# payment_dict = get_payment_list_detail()
payment_dict = payment_month_list()
pie1 = Pie("2019第二季度个人账单支出饼图")
pie1.add("", list(payment_dict.keys()), list(payment_dict.values()), is_label_show=True)


attr = ["收入", "支出"]
v1 = [total_income, total_payment]
pie2 = Pie("2019个人账单收支饼图")
pie2.add("", attr, v1, is_label_show=True)

pie1.render("./pie.html")
# env = create_default_environment("html")
# env.render_chart_to_file(pie, path="./pie.html")
print("运行成功")
