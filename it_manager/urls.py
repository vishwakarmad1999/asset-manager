"""it_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from items.views import ItemsListView
from django.contrib import admin
from django.contrib.auth.views import (PasswordResetView, 
                               PasswordResetCompleteView,
                                PasswordResetConfirmView, 
                                PasswordResetDoneView,
                                PasswordChangeView,
                                PasswordChangeDoneView
                                )

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', ItemsListView.as_view(), name = 'home'),
    # url(r'^add-excel', add_from_excel, name = 'add-excel'),
    url(r'logout/$', LogoutView.as_view(), name = 'logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^a/', include('items.urls', namespace = 'asset')),
    url(r'^login/', LoginView.as_view(), name = 'login'),
    url(r'^password-change/$', PasswordChangeView.as_view(), name = 'password_change'),
    url(r'^password-change/done$', PasswordChangeDoneView.as_view(), name = 'password_change_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset$', PasswordResetView.as_view(), name = 'password_reset'),
    url(r'^reset-sent', PasswordResetDoneView.as_view(), name = 'password_reset_done'),    
    url(r'^reset-complete/', PasswordResetCompleteView.as_view() , name = 'password_reset_complete'),
]
