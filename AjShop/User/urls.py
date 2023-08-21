
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('login',views.login),
    path('ShowGad/<id>',views.ShowGad),
    path('ViewDetails/<id>',views.ViewDetails),
    path('signup',views.signup),
    path('signout',views.signout),
    path('addcart',views.addcart),
    path('ShowItems',views.ShowItems),
    path('MakePayment',views.MakePayment),
    path('remove',views.remove),
]
