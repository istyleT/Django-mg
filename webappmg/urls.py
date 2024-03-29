"""webappmg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from sellmg import views #นำเข้า view จาก app ย่อย
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('static-css',views.static_css), #นำเข้า static css มาใช้ใน webappmg
    path('static-js',views.static_js), #นำเข้า static js มาใช้ใน webappmg
    path('',views.loginform),
    path('firstdata',views.collectdata),  
    path('Payment',views.PaymentRegis),
    path('branchadd',views.branceadd),
    path('branchcash',views.branchcash),
    path('showdata',views.showdata),
    path('logout', views.log_user_out),
    path('dataclient',views.dataclient),
    path('statuscustomer',views.statuscustomer),
    path('editcard',views.editcard),
    path('updatedatacustomer',views.updatedatacustomer),
    path ('querydatacustomer',views.querydatacustomer),
    #path ของหน้าทดสอบ
    path('cookie1',views.cookie_test),
    #path ของส่วน admin
    path('pageaddcolor', views.pageaddcolor),
    path('addcolor', views.addcolor),
    path('pageaddregiscost', views.pageaddregiscost),
    path('addregiscost', views.addregiscost),
    path('pageaddacc', views.pageaddacc),
    path('addacc', views.addacc),
    path('pageaddproduct', views.pageaddproduct),
    path('addproduct', views.addproduct),
    path('dashboard', views.dashboard),
    
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
