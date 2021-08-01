import django_tables2 as tables
from .models import *


class DataTable(tables.Table):
    Hshd_num = tables.Column(accessor="hshd_num.pk")
    Loyalty_flag = tables.Column(accessor="hshd_num.l")
    Age_range = tables.Column(accessor="hshd_num.age_range")
    Marital_status = tables.Column(accessor="hshd_num.marital")
    Income_range = tables.Column(accessor="hshd_num.income_range")
    Homeowner_desc = tables.Column(accessor="hshd_num.homeowner")
    Hshd_composition = tables.Column(accessor="hshd_num.hshd_composition")
    Hshd_size = tables.Column(accessor="hshd_num.hh_size")
    Children = tables.Column(accessor="hshd_num.children")

    Product_num = tables.Column(accessor="product_num.pk")
    Department = tables.Column(accessor="product_num.department")
    Commodity = tables.Column(accessor="product_num.commodity")

    class Meta:
        model = Transactions
        exclude = ("product_num", "hshd_num")
        sequence = (
            "Hshd_num",
            "...",
            "Department",
            "Commodity",
            "Loyalty_flag",
            "Age_range",
            "Marital_status",
            "Income_range",
            "Homeowner_desc",
            "Hshd_composition",
            "Hshd_size",
            "Children",
        )
