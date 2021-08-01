from datetime import datetime
import csv

from .models import *


def upload_households(households_file):
    """
    Method to upload household csv file

    :param households_file:
    :return:
    """

    rows = [
        {k: v for k, v in row.items()}
        for row in csv.DictReader(households_file.split("\n"), delimiter=",")
    ]

    households = []
    for row in rows:
        row_cleaned = {
            x.strip(): v for x, v in row.items()
        }  # Remove trailing spaces from keys so that they're easier to work with

        h = Households(
            hshd_num=int(row_cleaned["HSHD_NUM"].strip()),
            l=row_cleaned["L"],
            age_range=row_cleaned["AGE_RANGE"],
            marital=row_cleaned["MARITAL"],
            income_range=row_cleaned["INCOME_RANGE"],
            homeowner=row_cleaned["HOMEOWNER"],
            hshd_composition=row_cleaned["HSHD_COMPOSITION"],
            hh_size=row_cleaned["HH_SIZE"],
            children=row_cleaned["CHILDREN"],
        )

        households.append(h)

    Households.objects.bulk_update_or_create(
        households,
        [
            "l",
            "age_range",
            "marital",
            "income_range",
            "homeowner",
            "hshd_composition",
            "hh_size",
            "children",
        ],
        match_field="hshd_num",
    )  # Update outdated household info or insert if it doesn't already exists


def upload_products(products_file):
    """
    Method to upload products csv file

    :param products_file:
    :return:
    """
    rows = [
        {k: v for k, v in row.items()}
        for row in csv.DictReader(products_file.split("\n"), delimiter=",")
    ]

    products = []
    for row in rows:
        row_cleaned = {
            x.strip(): v for x, v in row.items()
        }  # Remove trailing spaces from keys so that they're easier to work with

        p = Products(
            product_num=int(row_cleaned["PRODUCT_NUM"].strip()),
            department=row_cleaned["DEPARTMENT"],
            commodity=row_cleaned["COMMODITY"],
            brand_ty=row_cleaned["BRAND_TY"],
            natural_organic_flag=row_cleaned["NATURAL_ORGANIC_FLAG"],
        )

        products.append(p)

    Products.objects.bulk_create(products, ignore_conflicts=True)


def upload_transactions(transactions_file):
    """
    Method to upload transactions csv file

    :param transactions_file:
    :return:
    """
    rows = [
        {k: v for k, v in row.items()}
        for row in csv.DictReader(transactions_file.split("\n"), delimiter=",")
    ]

    transactions = []
    for row in rows:
        row_cleaned = {
            x.strip().rstrip("_"): v for x, v in row.items()
        }  # Remove trailing spaces/underscores from keys so that they're easier to work with

        t = Transactions(
            basket_num=int(row_cleaned["BASKET_NUM"].strip()),
            hshd_num_id=row_cleaned["HSHD_NUM"],
            purchase=datetime.strptime(row_cleaned["PURCHASE"], "%d-%b-%y"),
            product_num_id=row_cleaned["PRODUCT_NUM"],
            spend=row_cleaned["SPEND"],
            units=row_cleaned["UNITS"],
            store_r=row_cleaned["STORE_R"],
            week_num=row_cleaned["WEEK_NUM"],
            year=row_cleaned["YEAR"],
        )

        transactions.append(t)

    Transactions.objects.bulk_create(
        transactions
    )  # bulk_create - insert the new ones.
