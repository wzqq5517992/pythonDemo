from pyecharts import Funnel
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

from pyecharts import Funnel

funnel = Funnel("2019第二季度个人账单收入漏斗图")
funnel.add(
    "账单",
    list(income_dict.keys()),
    list(income_dict.values()),
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
)
funnel.render("./funnel.html")
