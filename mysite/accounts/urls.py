from django.urls import path
from . import views

urlpatterns = [
    path('loginworker',views.loginworker,name='loginworker'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('registerworker',views.registerworker,name='registerworker'),
    path('dashboardworker',views.dashboardworker,name='dashboardworker'),
    path('dashboardcustomer',views.dashboardcustomer,name='dashboardcustomer'),
    path('dashboarduser',views.dashboarduser,name='dashboarduser'),

]
