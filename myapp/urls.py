"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from core import views as core_views
from core import views
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login, logout
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import RedirectView

#
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    #url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
    #url(r'^logout/', logout, {'next_page': reverse_lazy('login')}, name='logout'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #url(r'^logout/$', RedirectView.as_view(url=reverse_lazy('login')), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    #url(r'^getdata/$',  core_views.getdata, name='getdata'),
    url(r'^pagination/$',  core_views.pagination, name='pagination'),
    url(r'^get_offset/$', core_views.get_offset, name='get_offset'),
    url(r'^upload_excel/$', core_views.upload_excel, name='upload_excel'),
    url(r'^upload_pdf/$', core_views.upload_pdf, name='upload_pdf')
    #url(r'^logout/$', views.LogoutView.as_view(next_page= 'login'), name='logout'),
    #url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]

# from django.conf.urls import url
# from core import views as core_views
#
# urlpatterns = [
#     url(r'^signup/$', core_views.signup, name='signup'),
#     url(r'^login/$', core_views.login, name='login'),
#]

#bgfghbgh
#gxdshdcsj
#fdfhjd
#gfdj


