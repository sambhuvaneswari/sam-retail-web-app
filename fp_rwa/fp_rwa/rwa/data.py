# File for containing any additional data processing for graphs/charts
# Each should return a dict containing 'data' and 'label' fields
# All remaining configuration should be handled within views

import calendar
import re

from django.db.models import Sum, Count, F, DecimalField, ExpressionWrapper
from django.db.models.functions import TruncMonth

from .models import Households, Products, Transactions

# == Util methods ==


def sort_income_ranges(income_ranges):
    new_list = []

    for ir in income_ranges:
        num_re = re.search("[0-9]+", ir)

        if num_re is None:
            print("WARNING: Invalid income range ", ir)
            continue

        num_str = num_re.group(0)
        num_start = num_re.start()

        added = False
        num = int(num_str)
        ir_dict = {
            "text": ir,
            "val": num,
            "start": num_start,
        }

        for i, x in enumerate(new_list):
            if num < x["val"] or (num == x["val"] and num_start > x["start"]):
                new_list.insert(i, ir_dict)
                added = True
                break

        if not added:
            new_list.append(ir_dict)

    return [x["text"] for x in new_list]


# == Data retrieval methods ==


def get_monthly_transaction_amt(transactions=None):
    if transactions is None:
        transactions = Transactions.objects.all()

    grouped = (
        transactions.annotate(month=TruncMonth("purchase"))
        .values("month")
        .annotate(total=Sum("spend"))
        .order_by("month")
    )

    raw_data = grouped.values_list("total", flat=True)
    raw_dates = grouped.values_list("month", flat=True)

    data = [float(x) for x in raw_data]
    labels = ["%s %d" % (calendar.month_name[d.month], d.year) for d in raw_dates]

    return {
        "data": data,
        "labels": labels,
    }


def get_monthly_transaction_amt_by_hshd(hshd_vals, transactions=None):
    if transactions is None:
        transactions = Transactions.objects.all()

    ret_dict = {}
    for hshd in hshd_vals:
        print("Retrieving transactions for HSHD:", hshd)
        this_hshd_transactions = transactions.filter(hshd_num=hshd)
        ret_dict[hshd] = get_monthly_transaction_amt(this_hshd_transactions)

    return ret_dict


def get_comm_transaction_amt(transactions=None):
    if transactions is None:
        transactions = Transactions.objects.all()

    grouped = (
        transactions.select_related("product_num")
        .annotate(commodity=F("product_num__commodity"))
        .values("commodity")
        .annotate(total=Sum("spend"), households=Count("hshd_num", distinct=True))
        .annotate(
            spend_per_house=ExpressionWrapper(
                F("total") / F("households"), output_field=DecimalField()
            )
        )
        .order_by("commodity")
    )

    raw_data = grouped.values_list("spend_per_house", flat=True)
    raw_commodities = grouped.values_list("commodity", flat=True)

    data = [float(x) for x in raw_data]
    labels = [c.strip() for c in raw_commodities]

    return {
        "data": data,
        "labels": labels,
    }


def get_comm_transaction_amt_by_income(transactions=None):
    if transactions is None:
        transactions = Transactions.objects.all()

    income_ranges = (
        Households.objects.values_list("income_range", flat=True)
        .distinct()
        .exclude(income_range__isnull=True)
        .exclude(income_range__contains="null")
    )

    income_ranges_sorted = sort_income_ranges(income_ranges)

    ret_dict = {}
    for ir in income_ranges_sorted:
        print("Retrieving transactions for income range:", ir.strip())
        this_ir_transactions = transactions.select_related("hshd_num").filter(
            hshd_num__income_range=ir
        )
        ret_dict[ir] = get_comm_transaction_amt(this_ir_transactions)

    return ret_dict
