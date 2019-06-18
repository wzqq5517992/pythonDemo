from pyecharts import Gauge
from BillDetail import read_csv, get_payment_list, get_income_list, get_payment_list_detail, payment_month_list, \
    income_month_list
from pyecharts.engine import create_default_environment

read_csv('jolin.csv')
total_payment = get_payment_list()
print("账单支出: %s" % str(total_payment))
total_income = get_income_list()
print("账单收入: %s" % str(total_income))

payment_dict = payment_month_list()
income_dict = income_month_list()
income_dict["总收入"] = income_dict["四月"] + income_dict["六月"] + income_dict["五月"]

percentage = round(total_income / total_payment * 100, 2)
print(percentage)

gauge = Gauge("2019第二季度收入/支出仪表盘示例图")
gauge.add("个人盈亏指标", "盈亏率", percentage)
gauge.render("./gauge.html")
