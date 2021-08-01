from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class Households(models.Model):
    """
    Household model used for loading and visualizing data
    """

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    hshd_num = models.SmallIntegerField(
        db_column="HSHD_NUM", primary_key=True
    )  # Field name made lowercase.
    l = models.CharField(
        db_column="L", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    age_range = models.CharField(
        db_column="AGE_RANGE", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    marital = models.CharField(
        db_column="MARITAL", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    income_range = models.CharField(
        db_column="INCOME_RANGE", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    homeowner = models.CharField(
        db_column="HOMEOWNER", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    hshd_composition = models.CharField(
        db_column="HSHD_COMPOSITION", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    hh_size = models.CharField(
        db_column="HH_SIZE", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    children = models.CharField(
        db_column="CHILDREN", max_length=250, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "households"


class Products(models.Model):
    """
    Product model used for loading and visualizing data
    """

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    product_num = models.IntegerField(
        db_column="PRODUCT_NUM", primary_key=True
    )  # Field name made lowercase.
    department = models.CharField(
        db_column="DEPARTMENT", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    commodity = models.CharField(
        db_column="COMMODITY", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    brand_ty = models.CharField(
        db_column="BRAND_TY", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    natural_organic_flag = models.CharField(
        db_column="NATURAL_ORGANIC_FLAG", max_length=10, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "products"


class Transactions(models.Model):
    """
    Transaction model used for loading and visualizing data
    """

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    basket_num = models.CharField(
        db_column="BASKET_NUM", max_length=250
    )  # Field name made lowercase.
    hshd_num = models.ForeignKey(
        Households,
        on_delete=models.CASCADE,
        db_column="HSHD_NUM",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    purchase = models.DateField(
        db_column="PURCHASE", blank=True, null=True
    )  # Field name made lowercase.
    product_num = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        db_column="PRODUCT_NUM",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    spend = models.DecimalField(
        db_column="SPEND", max_digits=5, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    units = models.IntegerField(
        db_column="UNITS", blank=True, null=True
    )  # Field name made lowercase.
    store_r = models.CharField(
        db_column="STORE_R", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    week_num = models.IntegerField(
        db_column="WEEK_NUM", blank=True, null=True
    )  # Field name made lowercase.
    year = models.IntegerField(
        db_column="YEAR", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "transactions"
