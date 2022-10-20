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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('static-css',views.static_css), #นำเข้า static css มาใช้ใน webappmg
    path('static-js',views.static_js), #นำเข้า static js มาใช้ใน webappmg
    path('',views.firstpage), #ตังค่า path เเละ function ที่จะทำงาน
    path('firstdata',views.collectdata), # ถ้า method POST ไม่ต้องต่อ url ด้วย/
    path('queryprice',views.showprice),
    path('Payment',views.PaymentRegis),
    path('branchadd',views.branceadd),
    path('branchcash',views.branchcash),
    path('showdata',views.showdata),

]
