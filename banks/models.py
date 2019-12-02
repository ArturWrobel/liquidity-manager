from datetime import timedelta
from django.db import models

YES_NO = (("YES", "YES"), ("NO", "NO"))


class Citi(models.Model):
    date = models.DateField(primary_key=True)
    start_balance = models.FloatField(default=0)
    end_balance = models.FloatField(default=0)
    inflows = models.FloatField(default=0)
    outflows = models.FloatField(default=0)
    transfer_in = models.FloatField(default=0)
    transfer_out = models.FloatField(default=0)
    depo = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    reconciliation = models.FloatField(default=0)
    reconciled = models.CharField(choices=YES_NO, max_length=3, default="NO")

    @property
    def result(self):
        return (
            self.inflows
            + self.outflows
            + self.transfer_in
            + self.transfer_out
            + self.depo
            + self.interest
        )

    @property
    def end(self):
        return self.start_balance + self.result


class mBank(models.Model):
    date = models.DateField(primary_key=True)
    start_balance = models.FloatField(default=0)
    end_balance = models.FloatField(default=0)
    inflows = models.FloatField(default=0)
    outflows = models.FloatField(default=0)
    transfer_in = models.FloatField(default=0)
    transfer_out = models.FloatField(default=0)
    depo = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    reconciliation = models.FloatField(default=0)
    reconciled = models.CharField(choices=YES_NO, max_length=3, default="NO")

    @property
    def result(self):
        return (
            self.inflows
            + self.outflows
            + self.transfer_in
            + self.transfer_out
            + self.depo
            + self.interest
        )

    @property
    def end(self):
        return self.start_balance + self.result


class Societe(models.Model):
    date = models.DateField(primary_key=True)
    start_balance = models.FloatField(default=0)
    end_balance = models.FloatField(default=0)
    inflows = models.FloatField(default=0)
    outflows = models.FloatField(default=0)
    transfer_in = models.FloatField(default=0)
    transfer_out = models.FloatField(default=0)
    depo = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    reconciliation = models.FloatField(default=0)
    reconciled = models.CharField(choices=YES_NO, max_length=3, default="NO")

    @property
    def result(self):
        return (
            self.inflows
            + self.outflows
            + self.transfer_in
            + self.transfer_out
            + self.depo
            + self.interest
        )

    @property
    def end(self):
        return self.start_balance + self.result


class Santander(models.Model):
    date = models.DateField(primary_key=True)
    start_balance = models.FloatField(default=0)
    end_balance = models.FloatField(default=0)
    inflows = models.FloatField(default=0)
    outflows = models.FloatField(default=0)
    transfer_in = models.FloatField(default=0)
    transfer_out = models.FloatField(default=0)
    depo = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    reconciliation = models.FloatField(default=0)
    reconciled = models.CharField(choices=YES_NO, max_length=3, default="NO")

    @property
    def result(self):
        return (
            self.inflows
            + self.outflows
            + self.transfer_in
            + self.transfer_out
            + self.depo
            + self.interest
        )

    @property
    def end(self):
        return self.start_balance + self.result


DEAL_KIND = (("DEPO", "DEPO"), ("TXFR", "TXFR"), ("FX", "FX"), ("FWD", "FWD"))

CURRENCY = (("PLN", "PLN"), ("EUR", "EUR"), ("USD", "USD"))

CROSS_CURRENCY = (
    ("EUR/PLN", "EUR/PLN"),
    ("USD/PLN", "USD/PLN"),
    ("EUR/USD", "EUR/USD"),
)

DEAL_SIDE = (("BUY", "BUY"), ("SELL", "SELL"))

COUNTERPARTY = (
    ("Citi", "Citi"),
    ("mBank", " mBank"),
    ("Societe", "Societe"),
    ("Santander", "Santander"),
)

"""class Counterparty(models.Model):
    name = models.CharField(max_length=20, null=False)
    short = models.CharField(max_length=10, null=False)
    pln_acc = models.CharField(max_length=20, null=True)"""


class Books(models.Model):
    date = models.DateField(primary_key=True)
    inflows = models.FileField(null=True, max_length=100)
    outflows = models.FileField(null=True, max_length=100)


class Deals(models.Model):
    deal_number = models.AutoField(primary_key=True)
    deal_date = models.DateField(null=True)
    value_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    deal_kind = models.CharField(choices=DEAL_KIND, max_length=20, null=True)
    currency_base = models.CharField(choices=CURRENCY, null=True, max_length=3)
    currency_side = models.CharField(choices=CURRENCY, null=True, max_length=3)
    currency_cross = models.CharField(choices=CROSS_CURRENCY, null=True, max_length=7)
    side = models.CharField(choices=DEAL_SIDE, null=True, max_length=20)
    counterparty = models.CharField(choices=COUNTERPARTY, null=True, max_length=30)
    counterparty_another = models.CharField(choices=COUNTERPARTY, null=True, max_length=30)
    amount_in_base_cur = models.FloatField(null=True)
    amount_in_side_cur = models.FloatField(null=True)
    exchange_rate = models.FloatField(null=True)
    forward_rate = models.FloatField(null=True)
    interest_rate = models.FloatField(null=True)
    interest_rate_amount = models.FloatField(null=True)
    basis = models.CharField(null=True, max_length=20)
    frontoffice = models.CharField(null=True, max_length=10)
    fronttime = models.DateTimeField(null=True)
    middleoffice = models.CharField(null=True, max_length=10)
    middletime = models.DateTimeField(null=True)
    backoffice = models.CharField(null=True, max_length=10)
    backtime = models.DateTimeField(null=True)
    entity = models.CharField(null=True, max_length=20)
    status = models.CharField(null=True, max_length=10)
    cancel_user = models.CharField(null=True, max_length=10)
    cancel_time = models.DateTimeField(null=True)
    strategy_code = models.CharField(null=True, max_length=32)
    comment = models.CharField(null=True, max_length=160)

    @property
    def name(self):
        return "{} | {} | {} | {} | {} | {}".format(
            self.deal_number,
            self.counterparty,
            self.deal_kind,
            self.deal_date,
            self.value_date,
            self.amount_in_base_cur,
        )

    def __str__(self):
        return self.name


class PlnCurve(models.Model):
    date = models.DateField(primary_key=True)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)
    y12 = models.FloatField(default=0)
    y15 = models.FloatField(default=0)
    y20 = models.FloatField(default=0)


class EurCurve(models.Model):
    date = models.DateField(primary_key=True)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)
    y12 = models.FloatField(default=0)
    y15 = models.FloatField(default=0)
    y20 = models.FloatField(default=0)
    y30 = models.FloatField(default=0)
    y50 = models.FloatField(default=0)


class UsdCurve(models.Model):
    date = models.DateField(primary_key=True)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)
    y12 = models.FloatField(default=0)
    y15 = models.FloatField(default=0)
    y20 = models.FloatField(default=0)
    y30 = models.FloatField(default=0)
    y50 = models.FloatField(default=0)

class PLN1M (models.Model):
    date = models.DateField(primary_key=True)
    d1 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)

class PLN3M (models.Model):
    date = models.DateField(primary_key=True)
    d1 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)

class PLN6M (models.Model):
    date = models.DateField(primary_key=True)
    d1 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)

class EUR3M (models.Model):
    date = models.DateField(primary_key=True)
    d1 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)

class EUR6M (models.Model):
    date = models.DateField(primary_key=True)
    d1 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)

class USD3M (models.Model):
    date = models.DateField(primary_key=True)
    d1 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)
    y5 = models.FloatField(default=0)
    y6 = models.FloatField(default=0)
    y7 = models.FloatField(default=0)
    y8 = models.FloatField(default=0)
    y9 = models.FloatField(default=0)
    y10 = models.FloatField(default=0)

class EURPLN (models.Model):
    date = models.DateField(primary_key=True)
    spot = models.FloatField(default=0)
    on = models.FloatField(default=0)
    tn = models.FloatField(default=0)
    sn = models.FloatField(default=0)
    w1 = models.FloatField(default=0)
    w2 = models.FloatField(default=0)
    w3 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m2 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m4 = models.FloatField(default=0)
    m5 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)

class USDPLN (models.Model):
    date = models.DateField(primary_key=True)
    spot = models.FloatField(default=0)
    on = models.FloatField(default=0)
    tn = models.FloatField(default=0)
    sn = models.FloatField(default=0)
    w1 = models.FloatField(default=0)
    w2 = models.FloatField(default=0)
    w3 = models.FloatField(default=0)
    m1 = models.FloatField(default=0)
    m2 = models.FloatField(default=0)
    m3 = models.FloatField(default=0)
    m4 = models.FloatField(default=0)
    m5 = models.FloatField(default=0)
    m6 = models.FloatField(default=0)
    m9 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)