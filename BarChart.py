from pyecharts import Bar, Line
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

bar = Bar("2019第二季度个人账单柱状图")
bar.add("支出", list(payment_dict.keys()), list(payment_dict.values()), is_stack=True)
bar.add("收入", list(income_dict.keys()), list(income_dict.values()), is_stack=True)
bar.render("./bar.html")
# env = create_default_environment("html")
# env.render_chart_to_file(bar, path="./bar.html")
print("执行结束")
