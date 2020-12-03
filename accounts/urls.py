from django.urls import path,include
from . import views
urlpatterns = [
    path('accounts/signup/',views.signup, name='signup'),
    path('accounts/login',views.login,name='login'),
    path('account/logout',views.logout,name='logout'),

]