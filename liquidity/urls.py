from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

from banks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Start.as_view()),

    path('home/', Home.as_view()),
    path('bank_acc/<bank_acc>', Account.as_view(), name = 'account'),
    path('update/<bank_acc>/<date>',update_view),
    path('updatedeal/<deal_number>',update_deal),
    path('depo/', DepoDeal.as_view()),
    path('spot/', SpotDeal.as_view()),
    path('txfr/', TransferDeal.as_view()),
    path('dealsearch/', DealSearch.as_view(), name = 'search'),
    path('dealsearch_id/', DealSearchId.as_view(), name = 'search_id'),
    path('dealsfilter/', dealsfilter),
    path('dataimport/', DataImport.as_view(), name = 'data-import'),
    path('marketdataimport/', MarketDataImport.as_view(), name = 'market-data-import'),
    path('upload/', upload, name = 'upload'),
       
    url(r'^api/chart/data/$', ChartData.as_view()),
    path('chart/', ChartView.as_view()),
    path('api/chart/data2/<bank_acc>', ChartData2.as_view()),
    path('chart2/<bank_acc>', ChartView2.as_view()),
    path('api/yieldchart/data/', YieldChartData.as_view()),
    path('yieldchart/', YieldChartView.as_view()),

    url(r'^list_users/$', ListUsers.as_view(), name='list-users'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^add_user/$', AddUser.as_view(), name='add-user'),
    url(r'^reset_password/(?P<user_id>\d+)$', ResetPassword.as_view(), name='reset-password'),

    path('curves/', YieldCurves.as_view(), name = 'curves'),

    url(r'^accounts/', include('allauth.urls')),

    path('przelicznik/', Przelicznik.as_view()),
    path('', include('banks.urls')),
    url(r'^deals/', deals),
]
