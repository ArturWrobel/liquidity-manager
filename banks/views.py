from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import (
    render,
    get_object_or_404,
    Http404,
    redirect,
    render_to_response,
)

from banks.models import *
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView,
    TemplateView,
    FormView,
)
from datetime import *
from .forms import *
import numpy as np
import xlrd
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from banks.serializers import *

from .filters import *

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

from django.db.models import F, Value
from django.db.models.functions import Lag
from django.db.models.expressions import Window

from django.utils.datastructures import MultiValueDictKeyError


class Start(View):
    def get(self, request):
        out = {"title": "Start"}
        return render(request, "index.html", out)


class Home(View):
    def get(self, request):
        out = {"title": "Home"}
        return render(request, "home.html", out)


class Account(LoginRequiredMixin, View):
    login_url = "/accounts/login/"
    # redirect_field_name = '/login/'

    start_date = date.today() - timedelta(days=1)

    def pick_bank(bank_acc):
        if bank_acc == "Citi":
            return Citi
        elif bank_acc == "mBank":
            return mBank
        elif bank_acc == "Societe":
            return Societe
        elif bank_acc == "Santander":
            return Santander

    def get(self, request, bank_acc):
        acc = bank_acc
        daysrange = 60

        salda = (Account.pick_bank(bank_acc)
            .objects.filter(date__range=[str(Account.start_date),str(Account.start_date + timedelta(days=daysrange)),]).order_by("pk"))


        bal = Account.pick_bank(bank_acc).objects.annotate(balance=Window(expression=Lag("end_balance", 1), order_by=F("date").asc()))
        first_item = Account.pick_bank(bank_acc).objects.filter()[:1].get()
        lastreconciled = Account.pick_bank(bank_acc).objects.filter(reconciled="YES").last()
        num = (lastreconciled.pk - first_item.pk).days + 1
        
        if (Account.start_date + timedelta(days=daysrange)) <= lastreconciled.date:
            out = {"salda": salda, "title": acc}
            return render(request, "accountrec.html", out)
                      
        if Account.start_date <= lastreconciled.date:
            tog = {
                "{}".format(Account.start_date): {
                    "start": salda[0].start_balance,
                    "end": salda[0].start_balance + salda[0].result,
                    "inflows": salda[0].inflows,
                    "outflows": salda[0].outflows,
                    "transfer_in": salda[0].transfer_in,
                    "transfer_out": salda[0].transfer_out,
                    "depo": salda[0].depo,
                    "interest": salda[0].interest,
                    "reconciliation": salda[0].reconciliation,
                    "reconciled": salda[0].reconciled,
                }
            }
            daysrange = 65
            salda = (Account.pick_bank(bank_acc).objects.filter(date__range=[str(Account.start_date),str(Account.start_date + timedelta(days=daysrange)),]).order_by("pk"))

            sstart = Account.start_date
            eend = Account.start_date + timedelta(days=60)
            delta = timedelta(days=1)
            i = 0
            while sstart <= eend:
                sstart += delta
                tog["{}".format(sstart)] = {
                "start": tog["{}".format(sstart - timedelta(days=1))]["end"],
                "end": tog["{}".format(sstart - timedelta(days=1))]["end"]
                + salda[i+1].result,
                "reco_start": salda[i+1].start_balance,
                "reco_end": salda[i+1].end_balance,
                "inflows": salda[i + 1].inflows,
                "outflows": salda[i + 1].outflows,
                "transfer_in": salda[i + 1].transfer_in,
                "transfer_out": salda[i + 1].transfer_out,
                "depo": salda[i + 1].depo,
                "interest": salda[i + 1].interest,
                "reconciliation": salda[i + 1].reconciliation,
                "reconciliation": salda[i + 1].reconciled,}
                i += 1

            out = {"tog": tog, "title": acc}
            return render(request, "account.html", out)

        tog = {
            "{}".format(lastreconciled.date + timedelta(days=1)): {
                "start": bal[num].balance,
                "end": bal[num].balance + bal[num].result,
                "inflows": bal[num].inflows,
                "outflows": bal[num].outflows,
                "transfer_in": bal[num].transfer_in,
                "transfer_out": bal[num].transfer_out,
                "depo": bal[num].depo,
                "interest": bal[num].interest,
                "reconciliation": bal[num].reconciliation,
                "reconciled": bal[num].reconciled,
            }
        }

        salda = (Account.pick_bank(bank_acc)
            .objects.filter(date__range=[str(lastreconciled.pk),str(Account.start_date + timedelta(days=daysrange+(Account.start_date-lastreconciled.pk).days+1)),])
            .order_by("pk"))

        sstart = lastreconciled.pk + timedelta(days=1)
        eend = Account.start_date + timedelta(days=60)
        delta = timedelta(days=1)
        i = 1
        while sstart <= eend:
            # print (sstart.strftime("%Y-%m-%d"))
            sstart += delta
            tog["{}".format(sstart)] = {
                "start": tog["{}".format(sstart - timedelta(days=1))]["end"],
                "end": tog["{}".format(sstart - timedelta(days=1))]["end"]
                + bal[num + i].result,
                #"reco_start": salda[i+1].start_balance,
                #"reco_end": salda[i+1].end_balance,
                "inflows": salda[i + 1].inflows,
                "outflows": salda[i + 1].outflows,
                "transfer_in": salda[i + 1].transfer_in,
                "transfer_out": salda[i + 1].transfer_out,
                "depo": salda[i + 1].depo,
                "interest": salda[i + 1].interest,
                "reconciliation": salda[i + 1].reconciliation,
                "reconciliation": salda[i + 1].reconciled,
            }
            i += 1

        keys = ()
        for i in range (62):
            a = ("{}".format(Account.start_date + timedelta(days=i)),)
            keys += a

        tog = {k: tog[k] for k in keys}

        out = {"tog": tog, "title": acc}
        return render(request, "account.html", out)



    def post(self, request, bank_acc):
        acc = bank_acc

        if request.POST.get("ok") == "week up":
            Account.start_date = Account.start_date - timedelta(days=7)
           
        elif request.POST.get("ok") == "week down":
            Account.start_date = Account.start_date + timedelta(days=7)
            
        elif request.POST.get("ok") == "month up":
            Account.start_date = Account.start_date - timedelta(days=30)
            
        elif request.POST.get("ok") == "month down":
            Account.start_date = Account.start_date + timedelta(days=30)
           
        elif request.POST.get("ok") == "today":
            Account.start_date = date.today()

        elif request.POST.get("ok") == "chart":
            return redirect("/chart2/{}".format(bank_acc))

        
        acc = bank_acc
        daysrange = 60

        salda = (Account.pick_bank(bank_acc)
            .objects.filter(date__range=[str(Account.start_date),str(Account.start_date + timedelta(days=daysrange)),]).order_by("pk"))


        bal = Account.pick_bank(bank_acc).objects.annotate(balance=Window(expression=Lag("end_balance", 1), order_by=F("date").asc()))
        first_item = Account.pick_bank(bank_acc).objects.filter()[:1].get()
        lastreconciled = Account.pick_bank(bank_acc).objects.filter(reconciled="YES").last()
        num = (lastreconciled.pk - first_item.pk).days + 1
        
        if (Account.start_date + timedelta(days=daysrange)) <= lastreconciled.date:
            out = {"salda": salda, "title": acc}
            return render(request, "accountrec.html", out)
                      
        if Account.start_date <= lastreconciled.date:
            tog = {
                "{}".format(Account.start_date): {
                    "start": salda[0].start_balance,
                    "end": salda[0].start_balance + salda[0].result,
                    "inflows": salda[0].inflows,
                    "outflows": salda[0].outflows,
                    "transfer_in": salda[0].transfer_in,
                    "transfer_out": salda[0].transfer_out,
                    "depo": salda[0].depo,
                    "interest": salda[0].interest,
                    "reconciliation": salda[0].reconciliation,
                    "reconciled": salda[0].reconciled,
                }
            }
            daysrange = 65
            salda = (Account.pick_bank(bank_acc).objects.filter(date__range=[str(Account.start_date),str(Account.start_date + timedelta(days=daysrange)),]).order_by("pk"))

            sstart = Account.start_date
            eend = Account.start_date + timedelta(days=60)
            delta = timedelta(days=1)
            i = 0
            while sstart <= eend:
                sstart += delta
                tog["{}".format(sstart)] = {
                "start": tog["{}".format(sstart - timedelta(days=1))]["end"],
                "end": tog["{}".format(sstart - timedelta(days=1))]["end"]
                + salda[i+1].result,
                "reco_start": salda[i+1].start_balance,
                "reco_end": salda[i+1].end_balance,
                "inflows": salda[i + 1].inflows,
                "outflows": salda[i + 1].outflows,
                "transfer_in": salda[i + 1].transfer_in,
                "transfer_out": salda[i + 1].transfer_out,
                "depo": salda[i + 1].depo,
                "interest": salda[i + 1].interest,
                "reconciliation": salda[i + 1].reconciliation,
                "reconciliation": salda[i + 1].reconciled,}
                i += 1

            out = {"tog": tog, "title": acc}
            return render(request, "account.html", out)

        tog = {
            "{}".format(lastreconciled.date + timedelta(days=1)): {
                "start": bal[num].balance,
                "end": bal[num].balance + bal[num].result,
                "inflows": bal[num].inflows,
                "outflows": bal[num].outflows,
                "transfer_in": bal[num].transfer_in,
                "transfer_out": bal[num].transfer_out,
                "depo": bal[num].depo,
                "interest": bal[num].interest,
                "reconciliation": bal[num].reconciliation,
                "reconciled": bal[num].reconciled,
            }
        }

        salda = (Account.pick_bank(bank_acc)
            .objects.filter(date__range=[str(lastreconciled.pk),str(Account.start_date + timedelta(days=daysrange+(Account.start_date-lastreconciled.pk).days+1)),])
            .order_by("pk"))

        sstart = lastreconciled.pk + timedelta(days=1)
        eend = Account.start_date + timedelta(days=60)
        delta = timedelta(days=1)
        i = 1
        while sstart <= eend:
            # print (sstart.strftime("%Y-%m-%d"))
            sstart += delta
            tog["{}".format(sstart)] = {
                "start": tog["{}".format(sstart - timedelta(days=1))]["end"],
                "end": tog["{}".format(sstart - timedelta(days=1))]["end"]
                + bal[num + i].result,
                #"reco_start": salda[i+1].start_balance,
                #"reco_end": salda[i+1].end_balance,
                "inflows": salda[i + 1].inflows,
                "outflows": salda[i + 1].outflows,
                "transfer_in": salda[i + 1].transfer_in,
                "transfer_out": salda[i + 1].transfer_out,
                "depo": salda[i + 1].depo,
                "interest": salda[i + 1].interest,
                "reconciliation": salda[i + 1].reconciliation,
                "reconciliation": salda[i + 1].reconciled,
            }
            i += 1

        keys = ()
        for i in range (62):
            a = ("{}".format(Account.start_date + timedelta(days=i)),)
            keys += a

        tog = {k: tog[k] for k in keys}

        out = {"tog": tog, "title": acc}
        return render(request, "account.html", out)


@login_required(login_url="/accounts/login/")
def update_view(request, bank_acc, date):

    obj = Account.pick_bank(bank_acc).objects.get(date="{}".format(date))
    form = EditForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        # recalculate(date, bank_acc, 365)
        return redirect("/bank_acc/{}".format(bank_acc))

    context = {"form": form, "obj": obj}

    return render(request, "update_acc.html", context)


# from django.db import transaction

# @transaction.atomic

def recalculate(date, bank_acc, days):
    date = datetime.strptime(date, "%Y-%m-%d")
    sdate = date - timedelta(days=1)
    edate = sdate + timedelta(days=days)
    sdate = datetime.date(sdate)
    edate = datetime.date(edate)

    salda = list(
        Account.pick_bank(bank_acc).objects.filter(
            date__range=["{}".format(sdate), "{}".format(edate)]
        )
    )

    for i in range(len(salda) - 1):
        salda[i + 1].start_balance = salda[i].end_balance
        salda[i + 1].save()
        salda[i + 1].end_balance = salda[i + 1].start_balance + salda[i + 1].result
        salda[i + 1].save()
        i += 1

    return print(
        "------------------------------- base recalculated -------------------------------"
    )


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart1.html")


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {"labels": labels, "default": default_items}
        return Response(data)


class ChartView2(View):
    def get(self, request, bank_acc):
        return render(request, "chart2.html")


class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, bank_acc, format=None):
        start_date = Account.start_date

        salda = Account.pick_bank(bank_acc).objects.filter(
            date__range=[str(start_date), str(start_date + timedelta(days=30))]
        ).order_by('date')

        # serializer = CitiSerializer(salda, many=True)
        # serializer = CitiSerializer()

        labels = []
        for i in range(len(salda) - 1):
            labels.append(salda[i].date)
            i += 1

        default_items = []
        for i in range(len(salda) - 1):
            default_items.append(salda[i].start_balance)
            i += 1

        end_bal = []
        for i in range(len(salda) - 1):
            end_bal.append(salda[i].end_balance)
            i += 1

        infl = []
        for i in range(len(salda) - 1):
            infl.append(salda[i].inflows)
            i += 1

        outf = []
        for i in range(len(salda) - 1):
            outf.append(salda[i].outflows)
            i += 1

        data = {
            "labels": labels,
            "default": default_items,
            "end_bal": end_bal,
            "infl": infl,
            "outf": outf,
            "bank_acc": bank_acc,
        }
        return Response(data)


class DepoDeal(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        form = DepoForm(request.GET)
        ctx = {"form": form, "title": "Depo"}
        return render(request, "depo.html", ctx)

    def post(self, request):
        form = DepoForm(request.POST or None)
        if form.is_valid():
            dd = form.cleaned_data["deal_date"]
            vd = form.cleaned_data["value_date"]
            ed = form.cleaned_data["expiry_date"]
            cb = form.cleaned_data["currency_base"]
            cp = form.cleaned_data["counterparty"]
            am = form.cleaned_data["amount_in_base_cur"]
            ir = form.cleaned_data["interest_rate"]

            ira = am * ir / 100 / 365

            username = request.user.username
            time = datetime.now()

            new_deal = Deals.objects.create(
                deal_date=dd,
                value_date=vd,
                expiry_date=ed,
                currency_base=cb,
                counterparty=cp,
                amount_in_base_cur=am,
                interest_rate=ir,
                deal_kind="DEPO",
                interest_rate_amount=ira,
                frontoffice=username,
                fronttime=time,
            )

            before1 = Account.pick_bank(cp).objects.get(date="{}".format(vd))
            before2 = Account.pick_bank(cp).objects.get(date="{}".format(ed))

            before1.depo = before1.transfer_out - am
            before2.depo = before2.transfer_in + am
            before2.interest = round((before2.interest + ira), 2)

            before1.save()
            before2.save()

            return HttpResponseRedirect("/depo/".format(new_deal.pk))

        ctx = {"form": form, "title": "Depo"}
        return render(request, "depo.html", ctx)


class SpotDeal(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        form = SpotForm(request.GET)
        ctx = {"form": form, "title": "Spot"}
        return render(request, "spot.html", ctx)

    def post(self, request):
        form = SpotForm(request.POST)

        username = request.user.username
        time = datetime.now()

        if form.is_valid():
            dd = form.cleaned_data["deal_date"]
            vd = form.cleaned_data["value_date"]
            cc = form.cleaned_data["currency_cross"]
            sd = form.cleaned_data["side"]
            cp = form.cleaned_data["counterparty"]
            am = form.cleaned_data["amount_in_base_cur"]
            amt = form.cleaned_data["amount_in_side_cur"]
            ex = form.cleaned_data["exchange_rate"]

            amt = am * ex

            new_deal = Deals.objects.create(
                deal_date=dd,
                value_date=vd,
                currency_cross=cc,
                side=sd,
                counterparty=cp,
                amount_in_base_cur=am,
                amount_in_side_cur=amt,
                deal_kind="FX",
                exchange_rate=ex,
                frontoffice=username,
                fronttime=time,
            )

            return HttpResponseRedirect("/spot/".format(new_deal.pk))

        ctx = {"form": form, "title": "Spot"}
        return render(request, "spot.html", ctx)


class TransferDeal(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        form = TransferForm(request.GET)
        ctx = {"form": form, "title": "Transfer"}
        return render(request, "transfer.html", ctx)

    def post(self, request):
        form = TransferForm(request.POST)

        username = request.user.username
        time = datetime.now()

        if form.is_valid():
            dd = form.cleaned_data["deal_date"]
            vd = form.cleaned_data["value_date"]
            cb = form.cleaned_data["currency_base"]
            cp = form.cleaned_data["counterparty"]
            am = form.cleaned_data["amount_in_base_cur"]
            ca = form.cleaned_data["counterparty_another"]

            new_deal = Deals.objects.create(
                deal_date=dd,
                value_date=vd,
                currency_base=cb,
                counterparty=cp,
                counterparty_another=ca,
                amount_in_base_cur=am,
                deal_kind="TXFR",
            )

            before1 = Account.pick_bank(cp).objects.get(date="{}".format(vd))
            before2 = Account.pick_bank(ca).objects.get(date="{}".format(vd))

            print("-----------------------------------", before1)
            print("-----------------------------------", before2)

            before1.transfer_out = before1.transfer_out - am
            before2.transfer_in = before2.transfer_in + am

            before1.save()
            before2.save()

            return HttpResponseRedirect("/txfr/".format(new_deal.pk))

        ctx = {"form": form, "title": "Transfer"}
        return render(request, "transfer.html", ctx)


class DealSearch(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        if request.GET:
            form = DealSearchForm(request.GET)
        else:
            form = DealSearchForm()
        number_contains = request.GET.get("number_contains")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        date_choice = request.GET.get("date_choice")
        counterparty = request.GET.get("counterparty")

        deals = []

        if (
            date_choice == "value_date"
            and (
                number_contains or number_from or number_upto or start_date or end_date
            )
            or counterparty
        ):
            if start_date:
                start_date = datetime.strptime(start_date, "%m/%d/%Y").date()
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(value_date__gte=start_date)
                    .filter(counterparty=counterparty)
                    .order_by("pk")
                )
            elif end_date:
                end_date = datetime.strptime(end_date, "%m/%d/%Y").date()
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(value_date__lte=end_date)
                    .filter(counterparty=counterparty)
                    .order_by("pk")
                )
            elif not start_date and not end_date:
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(counterparty=counterparty)
                    .order_by("pk")
                )
            else:
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(value_date__lte=end_date)
                    .filter(value_date__gte=start_date)
                    .filter(counterparty=counterparty)
                    .order_by("pk")
                )

        elif date_choice == "deal_date" and (
            number_contains or number_from or number_upto or start_date or end_date
        ):
            if start_date:
                start_date = datetime.strptime(start_date, "%m/%d/%Y").date()
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(deal_date__gte=start_date)
                    .order_by("pk")
                )
            elif end_date:
                end_date = datetime.strptime(end_date, "%m/%d/%Y").date()
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(deal_date__lte=end_date)
                    .order_by("pk")
                )
            elif not start_date and not end_date:
                deals = Deals.objects.filter(
                    deal_number__icontains=number_contains
                ).order_by("pk")
            else:
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(deal_date__lte=end_date)
                    .filter(deal_date__gte=start_date)
                    .order_by("pk")
                )

        if request.GET.get("view_type") == "ajax":
            a = deals[0]
            ctx = {"deals": deals, "a": a}
            return render(request, "one_div.html", ctx)

        ctx = {"form": form, "deals": deals, "title": "Deal search"}

        return render(request, "deal_search.html", ctx)


class DealSearchId(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        if request.GET:
            form = DealSearchForm(request.GET)
        else:
            form = DealSearchIdForm()
        number_contains = request.GET.get("number_contains")
        number_from = request.GET.get("number_from")
        number_upto = request.GET.get("number_upto")

        deals = []

        if number_contains:
            if number_from and number_upto:
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(deal_number__lte=number_upto)
                    .filter(deal_number__gte=number_from)
                    .order_by("pk")
                )
            elif number_from:
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(deal_number__gte=number_from)
                    .order_by("pk")
                )
            elif number_upto:
                deals = (
                    Deals.objects.filter(deal_number__icontains=number_contains)
                    .filter(deal_number__lte=number_upto)
                    .order_by("pk")
                )
            else:
                deals = Deals.objects.filter(
                    deal_number__icontains=number_contains
                ).order_by("pk")

        else:
            if number_from and number_upto:
                deals = (
                    Deals.objects.filter(deal_number__lte=number_upto)
                    .filter(deal_number__gte=number_from)
                    .order_by("pk")
                )
            elif number_from:
                deals = Deals.objects.filter(deal_number__gte=number_from).order_by(
                    "pk"
                )
            elif number_upto:
                deals = Deals.objects.filter(deal_number__lte=number_upto).order_by(
                    "pk"
                )

        if request.GET.get("view_type") == "ajax":
            a = deals[0]
            ctx = {"deals": deals, "a": a}
            return render(request, "one_div.html", ctx)

        ctx = {"form": form, "deals": deals, "title": "Deal search by number"}

        return render(request, "deal_search_id.html", ctx)

@login_required(login_url="/accounts/login/")
def dealsfilter(request):

    deals_list = Deals.objects.all().order_by("deal_number")
    deals_filter = DealsFilter(request.GET, queryset=deals_list)
    title = "Deal search page"

    if request.GET.get("view_type") == "ajax":

        ctx = {"filter": deals_filter, "title": title}
        return render(request, "one_search_clean.html", ctx)

    return render(request, "dealsfilter.html", {"filter": deals_filter, "title": title})


@login_required(login_url="/accounts/login/")
def update_deal(request, deal_number):

    obj = Deals.objects.get(deal_number="{}".format(deal_number))

    if obj.deal_kind == "DEPO":
        form = EditDepoForm(request.POST or None, instance=obj)
        file = "update_depo.html"
    elif obj.deal_kind == "TXFR":
        form = EditTransferForm(request.POST or None, instance=obj)
        file = "update_transfer.html"
    elif obj.deal_kind == "FX":
        form = EditSpotForm(request.POST or None, instance=obj)
        file = "update_spot.html"

    if form.is_valid():
        form.save()
        return redirect("/dealsearch/")

    context = {"form": form, "obj": obj}

    return render(request, file, context)


class DataImport(LoginRequiredMixin, View):
    login_url = "/accounts/login/"
    
    def get(self, request):
        try:
            file_location = "C:/Users/ARW/Dev/Liquidity/src/media/flows.xlsx"
            data = xlrd.open_workbook(file_location)

            ci = data.sheet_by_index(0)
            mb = data.sheet_by_index(1)
            so = data.sheet_by_index(2)
            sa = data.sheet_by_index(3)

            all = [[ci, Citi],[mb, mBank],[so, Societe],[sa, Santander]]

            j = 0
            for j in range(len(all)):
                i = 0
                for row in range((all[j][0]).nrows - 1):
                    first_date =  xlrd.xldate_as_tuple((all[j][0]).cell_value(1,0), data.datemode)
                    first_date = datetime(first_date[0], first_date[1], first_date[2])
                    first_date = first_date.date()
                    # format first_date: tuple => datetime => date

                    dat = first_date + timedelta(days=i)
                    flows = all[j][1].objects.get(date="{}".format(dat))
                    flows.inflows = all[j][0].cell_value(row + 1, 1)
                    flows.outflows = all[j][0].cell_value(row + 1, 2)
                    flows.save()
                    i += 1
                j += 1
        except FileNotFoundError as error:
            return render(request, "alert.html", {"alert": "Error: there is no file Flows.xlsx uploaded."})
        
        # recalculate(str(date.today()), Citi, 365) /// do zastanowienia

        out = {"title": "Import"}
        return render(request, "dataimport.html", out)


@login_required(login_url="/accounts/login/")
def upload(request):
    ctx = {"title": "Upload"}
    try:
        if request.method == "POST":
            uploaded_file = request.FILES["document"]
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            ctx["url"] = fs.url(name)
    except MultiValueDictKeyError as error:
        return render(request, "alert.html", {"alert": "Error: please specify file before we proceed."})
    
    return render(request, "upload.html", ctx)

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST["username"], password=request.POST["password"])

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/home/")
            else:
                text = "Account not active"

        else:
            text = "There is no such user"

        return render(request, "login.html", {"text": text, "form": form})


class LogoutView(View):
    def get(self, request):
        return render(request, "logout.html", {"title": "Logout"})

    def post(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class AddUser(CreateView):
    template_name = "user_form.html"
    form_class = AddUserForm
    success_url = reverse_lazy("list-users")


class ResetPassword(PermissionRequiredMixin, FormView):
    permission_required = "auth.change_user"

    form_class = ResetPasswordForm
    template_name = "reset_password.html"
    success_url = reverse_lazy("list-users")

    def get_context_data(self):
        ctx = super().get_context_data()
        password_owner = get_object_or_404(User, id=self.kwargs.get("user_id"))
        ctx.update({"password_owner": password_owner})
        return ctx

    def form_valid(self, form):
        user_id = self.request.resolver_match.kwargs["user_id"]  # FIXME
        user = get_object_or_404(User, id=user_id)
        user.set_password(form.cleaned_data["new_password"])
        user.save()
        return super().form_valid(form)


class YieldCurves(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):

        title = "Yield curves"
        pcurve = PlnCurve.objects.last()
        ecurve = EurCurve.objects.last()
        ucurve = UsdCurve.objects.last()

        out = {"pcurve": pcurve, "ecurve": ecurve, "ucurve": ucurve, "title": title}
        return render(request, "curves.html", out)


class MarketDataImport(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        file_location = "C:/Users/ARW/Dev/Liquidity/src/media/market_data.xlsx"
        data = xlrd.open_workbook(file_location)

        pln = data.sheet_by_index(0)
        eur = data.sheet_by_index(1)
        usd = data.sheet_by_index(2)
        fx = data.sheet_by_index(3)

        pln_date =  xlrd.xldate_as_tuple(pln.cell_value(0,0), data.datemode)
        pln_date = datetime(pln_date[0], pln_date[1], pln_date[2])
        pln_date = pln_date.date()

        eur_date =  xlrd.xldate_as_tuple(eur.cell_value(0,0), data.datemode)
        eur_date = datetime(eur_date[0], eur_date[1], eur_date[2])
        eur_date = eur_date.date()

        usd_date =  xlrd.xldate_as_tuple(usd.cell_value(0,0), data.datemode)
        usd_date = datetime(usd_date[0], usd_date[1], usd_date[2])
        usd_date = usd_date.date()

        last_PLN_date = PlnCurve.objects.last()
        last_EUR_date = EurCurve.objects.last()
        last_USD_date = UsdCurve.objects.last()

        if pln_date == last_PLN_date.date or eur_date == last_EUR_date.date or usd_date == last_USD_date:
            out = {"title": "Alert", "alert": "Market Data in loaded file have wrong value date. Data for {} already exist in database.".format(last_PLN_date.date)}
            return render(request, "alert.html", out)
                
        pln_query = PlnCurve.objects.create(
            date=pln_date,
            m1=pln.cell_value(1, 1),
            m3=pln.cell_value(2, 1),
            m6=pln.cell_value(3, 1),
            y1=pln.cell_value(4, 1),
            y2=pln.cell_value(5, 1),
            y3=pln.cell_value(6, 1),
            y4=pln.cell_value(7, 1),
            y5=pln.cell_value(8, 1),
            y6=pln.cell_value(9, 1),
            y7=pln.cell_value(10, 1),
            y8=pln.cell_value(11, 1),
            y9=pln.cell_value(12, 1),
            y10=pln.cell_value(13, 1),
            y12=pln.cell_value(14, 1),
            y15=pln.cell_value(15, 1),
            y20=pln.cell_value(16, 1),
        )
        pln_query.save()
      
        eur_query = EurCurve.objects.create(
            date=eur_date,
            m1=eur.cell_value(1, 1),
            m3=eur.cell_value(2, 1),
            m6=eur.cell_value(3, 1),
            y1=eur.cell_value(4, 1),
            y2=eur.cell_value(5, 1),
            y3=eur.cell_value(6, 1),
            y4=eur.cell_value(7, 1),
            y5=eur.cell_value(8, 1),
            y6=eur.cell_value(9, 1),
            y7=eur.cell_value(10, 1),
            y8=eur.cell_value(11, 1),
            y9=eur.cell_value(12, 1),
            y10=eur.cell_value(13, 1),
            y12=eur.cell_value(14, 1),
            y15=eur.cell_value(15, 1),
            y20=eur.cell_value(16, 1),
            y30=eur.cell_value(17, 1),
            y50=eur.cell_value(18, 1),
        )
        eur_query.save()
        
        usd_query = UsdCurve.objects.create(
            date=usd_date,
            m1=usd.cell_value(1, 1),
            m3=usd.cell_value(2, 1),
            m6=usd.cell_value(3, 1),
            y1=usd.cell_value(4, 1),
            y2=usd.cell_value(5, 1),
            y3=usd.cell_value(6, 1),
            y4=usd.cell_value(7, 1),
            y5=usd.cell_value(8, 1),
            y6=usd.cell_value(9, 1),
            y7=usd.cell_value(10, 1),
            y8=usd.cell_value(11, 1),
            y9=usd.cell_value(12, 1),
            y10=usd.cell_value(13, 1),
            y12=usd.cell_value(14, 1),
            y15=usd.cell_value(15, 1),
            y20=usd.cell_value(16, 1),
            y30=usd.cell_value(17, 1),
            y50=usd.cell_value(18, 1),
        )
        eur_query.save()

        out = {"title": "Market Data Import", "date": last_PLN_date.date}
        return render(request, "marketdataimport.html", out)


class YieldChartView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        return render(request, "yieldchart.html")


class YieldChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        pln = PlnCurve.objects.last()
        eur = EurCurve.objects.last()
        usd = UsdCurve.objects.last()

        labels = [
            "1M",
            "3M",
            "6M",
            "1Y",
            "2Y",
            "3Y",
            "4Y",
            "5Y",
            "6Y",
            "7Y",
            "8Y",
            "9Y",
            "10Y",
            "12Y",
            "15Y",
            "20Y",
            "30Y",
            "50Y",
        ]

        pln = [
            pln.m1,
            pln.m3,
            pln.m6,
            pln.y1,
            pln.y2,
            pln.y3,
            pln.y4,
            pln.y5,
            pln.y6,
            pln.y7,
            pln.y8,
            pln.y9,
            pln.y10,
            pln.y12,
            pln.y15,
            pln.y20,
        ]
        eur = [
            eur.m1,
            eur.m3,
            eur.m6,
            eur.y1,
            eur.y2,
            eur.y3,
            eur.y4,
            eur.y5,
            eur.y6,
            eur.y7,
            eur.y8,
            eur.y9,
            eur.y10,
            eur.y12,
            eur.y15,
            eur.y20,
            eur.y30,
            eur.y50,
        ]
        usd = [
            usd.m1,
            usd.m3,
            usd.m6,
            usd.y1,
            usd.y2,
            usd.y3,
            usd.y4,
            usd.y5,
            usd.y6,
            usd.y7,
            usd.y8,
            usd.y9,
            usd.y10,
            usd.y12,
            usd.y15,
            usd.y20,
            usd.y30,
            usd.y50,
        ]

        data = {"labels": labels, "pln": pln, "eur": eur, "usd": usd}
        return Response(data)


def deals(request):
    return render(request, "accounts1.html", {"deals": Deals.objects.all()})


def graph(request):
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")

    script, div = components(plot)

    return render(request, "graph.html", {"script": script, "div": div})


def graph1(request):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2, 4, 5, -10, 5, 7, -2, 11, 1]
    title = "liniowy"

    plot = figure(
        title=title,
        x_axis_label="Highs and Lows",
        y_axis_label="dane dane",
        plot_width=1400,
        plot_height=700,
        tools="",
        toolbar_location=None,
    )

    # formating graph
    cr = plot.circle(
        x,
        y,
        size=10,
        color="blue",
        fill_color="grey",
        hover_fill_color="firebrick",
        fill_alpha=0.05,
        hover_alpha=0.3,
        line_color=None,
        hover_line_color="white",
    )

    plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode="hline"))
    plot.title.text_font_size = "20pt"
    plot.line(
        x,
        y,
        legend="Leaning Line",
        line_width=4,
        line_color="brown",
        line_dash="dashed",
    )
    plot.background_fill_color = "lightgrey"
    plot.border_fill_color = "whitesmoke"
    plot.min_border_left = 40
    plot.min_border_right = 40
    plot.outline_line_width = 7
    plot.outline_line_alpha = 0.2
    plot.outline_line_color = "purple"

    script, div = components(plot)

    return render(request, "graph1.html", {"script": script, "div": div})


class Przelicznik(View):
    def get(self, request):
        return render(request, "przelicznik_temp.html")

    def post(self, request):

        temp = int(request.POST.get("degrees"))

        if request.POST.get("convertionType") == "celcToFahr":
            value = 5 / 9 * (temp - 32)
            napis = "Temperatura: {} stopni".format(value)
            ctx = {"napis": napis}
            return render(request, "przelicznik_temp.html", ctx)

        elif request.POST.get("convertionType") == "FahrToCelc":
            value = 32 + 9 / 5 * temp
            napis = "Temperatura: {} stopni".format(value)
            ctx = {"napis": napis}
            return render(request, "przelicznik_temp.html", ctx)
