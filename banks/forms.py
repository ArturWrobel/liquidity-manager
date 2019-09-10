from django import forms
from .models import *
from django.contrib.auth.models import User

DEAL_KIND = (("DEPO", "DEPO"), ("TXFR", "TXFR"), ("FX", "FX"))

CURRENCY = (("PLN", "PLN"), ("EUR", "EUR"), ("USD", "USD"))

CROSS_CURRENCY = (
    ("EUR/PLN", "EUR/PLN"),
    ("USD/PLN", "USD/PLN"),
    ("EUR/USD", "EUR/USD"),
)

DEAL_SIDE = (("BUY", "BUY"), ("SELL", "SELL"))

COUNTERPARTY = (
    ("", ""),
    ("Citi", "Citi"),
    ("mBank", " mBank"),
    ("Societe", "Societe"),
    ("Santander", "Santander"),
)
DATE_CHOICE = (("value_date", "value date"), ("deal_date", "deal date"))


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Citi
        fields = ["date", "start_balance", "end_balance", "inflows", "outflows"]


class TestForm(forms.ModelForm):
    class Meta:
        model = Citi
        fields = ["date", "start_balance", "end_balance", "inflows", "outflows"]


class RawTestForm(forms.Form):
    date = forms.DateField()
    start_balance = forms.FloatField()
    end_balance = forms.FloatField()
    inflows = forms.FloatField()
    outflows = forms.FloatField()


class EditForm(forms.ModelForm):

    inflows = forms.FloatField()
    outflows = forms.FloatField()

    class Meta:
        model = Citi
        fields = [
            "inflows",
            "outflows",
            "transfer_in",
            "transfer_out",
            "depo",
            "interest",
            "reconciliation",
        ]


class SpotForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            "counterparty",
            "deal_date",
            "value_date",
            "currency_cross",
            "side",
            "amount_in_base_cur",
            "amount_in_side_cur",
            "exchange_rate",
        ]


class EditSpotForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            "counterparty",
            "deal_date",
            "value_date",
            "currency_cross",
            "side",
            "amount_in_base_cur",
            "amount_in_side_cur",
            "exchange_rate",
        ]


class TransferForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            "counterparty",
            "counterparty_another",
            "deal_date",
            "value_date",
            "currency_base",
            "amount_in_base_cur",
        ]


class EditTransferForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            "counterparty",
            "counterparty_another",
            "deal_date",
            "value_date",
            "currency_base",
            "amount_in_base_cur",
        ]


class DepoForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            "counterparty",
            "deal_date",
            "value_date",
            "expiry_date",
            "currency_base",
            "amount_in_base_cur",
            "interest_rate",
        ]


class EditDepoForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            "counterparty",
            "deal_date",
            "value_date",
            "expiry_date",
            "currency_base",
            "amount_in_base_cur",
            "interest_rate",
        ]


class DealSearchForm(forms.Form):
    number_contains = forms.CharField(strip=True, required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    date_choice = forms.CharField(
        label="Search by: ",
        widget=forms.RadioSelect(choices=DATE_CHOICE),
        initial="value_date",
    )
    counterparty = forms.ChoiceField(choices=COUNTERPARTY, required=False, initial="")


class DealSearchIdForm(forms.Form):
    number_contains = forms.CharField(strip=True, required=False)
    number_from = forms.IntegerField(required=False)
    number_upto = forms.IntegerField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(strip=True)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class AddUserForm(UserForm):
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        if User.objects.filter(username=self.data["username"]).exists():
            self.add_error("username", error="Użytkownik już istnieje w bazie")
        return self.data["username"]

    def clean(self):
        if self.data["password_1"] != self.data["password_2"]:
            self.add_error(None, error="Hasła nie pasują do siebie")
        return super().clean()

    def save(self):
        user_data = self.cleaned_data
        user = User.objects.create_user(
            username=user_data["username"],
            password=user_data["password_1"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
        )
        return user

    class Meta(UserForm.Meta):
        fields = UserForm.Meta.fields + ("password_1", "password_2")


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    repeated_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if self.data["new_password"] != self.data["repeated_new_password"]:
            self.add_error(None, error="Hasła nie pasują do siebie")
        return super().clean()

