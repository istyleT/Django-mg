from sellmg.quotations_mod import *
from sellmg.models import *
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout;
from django.db.models import Q ;
from django.contrib.auth.decorators import login_required ;
from django.contrib.auth.models import User
from datetime import datetime

#########################นำ css / java static มาใช้งาน ##########################
def static_css (request):
    return render(request, 'static-css.html')
def static_js (request):
    return render(request, 'static-js.html')

################ฟังก์ขันลงชื่อเช้า-ออก#############################
def loginform(request):
    return render(request, 'login.html')
def log_user_out(request):
    # Log user out
    logout(request)
    return redirect(loginform)

##################### ฟังก์ชันฝั่งadmin #####################
@login_required(login_url='/firstdata') 
def pageaddcolor(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       idcolor = request.POST.get('idcolor')
       datacolor = Colorsubmodels.objects.filter(id = idcolor)
       return render(request,'addcolor.html',{'datacolor': datacolor})
    else :
       return render(request,'login.html')
@login_required(login_url='/firstdata')   
def pageaddregiscost(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       idregiscost = request.POST.get('idregiscost')
       dataregiscost = Regiscosts.objects.filter(id = idregiscost)
       return render(request,'addregiscost.html',{'dataregiscost':dataregiscost})
    else:
       return render(request,'login.html')
@login_required(login_url='/firstdata')       
def pageaddproduct(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       idproduct = request.POST.get('idproduct')
       dataproduct = Product.objects.filter(id = idproduct)
       return render(request,'addproduct.html',{'dataproduct':dataproduct})
    else:
       return render(request,'login.html')
@login_required(login_url='/firstdata')      
def pageaddacc(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       idacc = request.POST.get('idacc')
       dataacc = Accmgs.objects.filter(id = idacc)
       return render(request,'addacc.html',{'dataacc':dataacc})
    else:
       return render(request,'login.html')
@login_required(login_url='/firstdata')  
def dashboard (request):
    #เรียกหาข้อมูลจาก database ที่ต้องการดู เก็บไว้ในตัวเเปร
    dashproduct = Product.objects.all().order_by("mainmodel")
    dashregiscosts = Regiscosts.objects.all().order_by("regis_code")
    dashaccmgs = Accmgs.objects.all().order_by("acc_code")
    dashcolorsubmodels = Colorsubmodels.objects.all().order_by("submodel")
    dashmsacustomer = MSAcustomer.objects.all().order_by("-date")
    #สั่ง render เเละส่งค่าเข้าสุ่ Template                  
    return render(request,'dashboard.html',{'dashproduct':dashproduct,'dashregiscosts':dashregiscosts,'dashaccmgs':dashaccmgs,'dashcolorsubmodels':dashcolorsubmodels, 'dashhtrcustomer':dashmsacustomer})
def addcolor(request):
    #ตัวเเปรเงื่อนไข
    doit_add = request.POST.get('doit') 
    idcolor_add = request.POST.get('idcolor')                   
    #ตัวเเปรทั่วไป
    submodel_add = request.POST.get('submodel') 
    color_add = request.POST.get('color') 
    #สร้างเงื่อนไข
    if doit_add == 'create':
       Colorsubmodels.objects.create(submodel=submodel_add, color=color_add)
    elif doit_add == 'update':
       Colorsubmodels.objects.filter(id=idcolor_add).update(submodel=submodel_add, color=color_add)    
    elif doit_add == 'delete':
       Colorsubmodels.objects.filter(id=idcolor_add).delete() 
    return render(request, 'addcolor.html')
def addregiscost(request):
    #ตัวเเปรเงื่อนไข
    doit_add = request.POST.get('doit') 
    idregiscost_add = request.POST.get('idregiscost') 
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    regis_code_add = request.POST.get('regis_code') 
    regis_personal_add = request.POST.get('regis_personal') 
    regis_company_add = request.POST.get('regis_company') 
    #สร้างเงื่อนไข
    if doit_add == 'create':
       Regiscosts.objects.create(regis_code= regis_code_add, regis_personal=regis_personal_add, regis_company=regis_company_add)
    elif doit_add == 'update':
       Regiscosts.objects.filter(id=idregiscost_add).update(regis_code= regis_code_add, regis_personal=regis_personal_add, regis_company=regis_company_add)    
    elif doit_add == 'delete':
       Regiscosts.objects.filter(id=idregiscost_add).delete() 
    
    return render(request, 'addregiscost.html')
def addproduct(request):
    #ตัวเเปรเงื่อนไข
    doit_add = request.POST.get('doit') 
    idproduct_add = request.POST.get('idproduct') 
    #ตัวเเปรทั่วไป
    mainmodel_add = request.POST.get('mainmodel') 
    submodel_add = request.POST.get('submodel') 
    price_add = request.POST.get('price') 
    margin_add = request.POST.get('margin') 
    #สร้างเงื่อนไข
    if doit_add == 'create':
       Product.objects.create(mainmodel= mainmodel_add, submodel=submodel_add, price=price_add, margin=margin_add)
    elif doit_add == 'update':
       Product.objects.filter(id=idproduct_add).update(mainmodel= mainmodel_add, submodel=submodel_add, price=price_add, margin=margin_add)    
    elif doit_add == 'delete':
       Product.objects.filter(id=idproduct_add).delete()    
    return render(request, 'addproduct.html')
def addacc(request):
    #ตัวเเปรเงื่อนไข
    doit_add = request.POST.get('doit') 
    idacc_add = request.POST.get('idacc') 
    # general variable
    acc_code_add = request.POST.get('acc_code') 
    acc_name_add = request.POST.get('acc_name') 
    acc_price_add = request.POST.get('acc_price') 
    acc_type_add = request.POST.get('acc_type') 
    acc_model_add = request.POST.get('acc_model') 
    #condition
    if doit_add == 'create':
       Accmgs.objects.create(acc_code= acc_code_add, acc_name=acc_name_add, acc_price=acc_price_add, acc_type=acc_type_add, acc_model=acc_model_add)
    elif doit_add == 'update':
       Accmgs.objects.filter(id=idacc_add).update(acc_code= acc_code_add, acc_name=acc_name_add, acc_price=acc_price_add, acc_type=acc_type_add, acc_model=acc_model_add)    
    elif doit_add == 'delete':
       Accmgs.objects.filter(id=idacc_add).delete()    
    return render(request, 'addacc.html')

##########################ฟังก์ชั่นฝั่ง user ################################
def uploadpage(request):
    form = QuotationsForm()
    return render(request,'uploadpage.html',{'form':form})
def upload(request):
    if request.method == "POST":
       form = QuotationsForm(request.POST , request.FILES)
       if form.is_valid() and request.FILES is not None:
          form.save()
          form = QuotationsForm()
    data = Quotations.objects.order_by('-id') # เรียงตาม id เเบบย้อนกลับ
    return render(request,'filedata.html',{'data': data})
def collectdata(request): 
    # เก็บข้อมูลการ login จาก user 
    username = str(request.POST.get('username'))
    password = str(request.POST.get('password'))
    # เอาข้อมูลที่เก็บได้ไปเช็คมามีไหม
    user = authenticate(request, username=username, password=password)
    # ถ้ามี เข้า condition render หน้าต่อไป 
    if user is not None:
        # Log a user in
         login(request, user)
         # query เอาข้อมูลจาก table auth_user
         firstname_set = User.objects.filter(username = username).values_list('first_name','last_name','email',named=True)
         # for เอาข้อมูลจาก Queryset
         for i in firstname_set :
            firstname =  str(i.first_name)
            sellphone =  str(i.last_name)
            branchset = str(i.email) #e-mailจะเป็นคนกำหนดสิทธิ์ในการเข้าถึงข้อมูล
            #กำหนดค่าสาขาโดยการใช้ e-mail
            #sellbranch เป็นข้อมูลที่จะบันทึกเข้าฐานข้อมูลลูกค้า
            if branchset == "AD@mg.msa":
                sellbranch = "Admin"
            elif branchset == "HO@mg.msam":
                sellbranch = "HO"
            elif branchset == "RS@mg.msam":
                sellbranch = "RS"
            elif branchset == "HTR@mg.msam":
                sellbranch = "HTR"
            elif branchset == "HO@mg.msa":
                sellbranch = "HO"
            elif branchset == "RS@mg.msa":
                sellbranch = "RS"
            elif branchset == "HTR@mg.msa":
                sellbranch = "HTR"
         #ส่งข้อมูลออก
         request.session['username'] = username  #ส่งออกเผื่อเป็น admin จะมี menu พิเศษที่ navbar
         request.session['firstname'] = firstname
         request.session['sellphone'] = sellphone
         request.session['sellbranch'] = sellbranch
         request.session['branchset'] = branchset
         return render(request,'dataclient.html',{'username':username})
    # ถ้าไม่มี สั่ง render หน้าเดิม
    else:
        status_login = 'False'
        return render(request,'login.html',{"status_login":status_login})
@login_required(login_url='/firstdata') 
def dataclient(request): 
    #เก็บข้อมูล username
    username = str(request.session.get('username'))
    firstname = str(request.session.get('firstname'))
    sellbranch = str(request.session.get('sellbranch'))
    #เก็บข้อมูลหน้าตัวเอง
    teamsell = str(request.POST.get('teamsell'))
    mainmodel = str(request.POST.get('mainmodel'))
    customername = str(request.POST.get('customername'))
    contactcustomer = str(request.POST.get('contactcustomer') or '-')
    chanelcustomer = str(request.POST.get('chanelcustomer'))
    statuscustomer = str(request.POST.get('statuscustomer'))
    #ส่งข้อมูลออก
    request.session['mainmodel'] = mainmodel
    request.session['customername'] = customername
    request.session['contactcustomer'] = contactcustomer
    #เก็บข้อมลูลูกค้าเข้า database
    MSAcustomer.objects.create(msabranch=sellbranch,teamsell=teamsell ,firstname = firstname, mainmodel = mainmodel, customername = customername, contactcustomer= contactcustomer, chanelcustomer = chanelcustomer, statuscustomer = statuscustomer)
    if mainmodel == "MG5":
       return render(request ,'Model_A.html',{'username': username})
    elif mainmodel == "MGVSHEV" :
        return render(request ,'Model_B.html',{'username': username})
    elif mainmodel == "MGZS" :
        return render(request ,'Model_C.html',{'username': username})
    elif mainmodel == "MGETD" :
        return render(request ,'Model_D.html',{'username': username})
    elif mainmodel == "MGHSPHEV" :
        return render(request ,'Model_E.html',{'username': username})
    elif mainmodel == "MGHS" :
        return render(request ,'Model_F.html',{'username': username})
    elif mainmodel == "MG4" :
        return render(request ,'Model_G.html',{'username': username})
    elif mainmodel == "MGEP" :
        return render(request ,'Model_H.html',{'username': username})
@login_required(login_url='/firstdata') 
def statuscustomer(request):
    #เก็บข้อมูลทำเงื่อนในการมองเห็น
    firstname = str(request.session.get('firstname'))#กรณี sell ดูได้เเค่ชื่อตัวเอง
    branchset = str(request.session.get('branchset'))#กรณีไม่ใช่ sell กำหนดการเห็นข้อมูล
    #เงื่อนไขดูข้อมูลของ admin    
    if  branchset == "AD@mg.msa": 
        datacustomer = MSAcustomer.objects.all().values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    #เงื่อนไขดูข้อมูลผจก.
    elif branchset == "HO@mg.msam":
        datacustomer = MSAcustomer.objects.filter(msabranch = "HO").values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    elif branchset == "RS@mg.msam":
        datacustomer = MSAcustomer.objects.filter(msabranch = "RS").values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    elif branchset == "HTR@mg.msam":
        datacustomer = MSAcustomer.objects.filter(msabranch = "HTR").values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    #เงื่อนไขดูข้อมูลของ sell 
    else:
        datacustomer = MSAcustomer.objects.filter(firstname=firstname).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    countdatacustomer = datacustomer.count()
    #ส่งไปเเสดงค่าให้ตรงตามเงื่อนไขข้อมูลที่เเสดงเริ่มต้น
    querybranch_new = "ทั้งหมด"
    queryteam_new = "ทังหมด"
    querystatus_new ="ทั้งหมด"
    return render(request,'statuscustomer.html',{'datacustomer':datacustomer,'branchset':branchset,'countdatacustomer':countdatacustomer,'querystatus_new':querystatus_new,'queryteam_new':queryteam_new,'querybranch_new':querybranch_new})
@login_required(login_url='/firstdata') 
def editcard(request):
    #เก็บข้อมูลหน้าตัวเอง idcard = id ของ MSAcustomer
    idcard = request.POST.get('idcard') 
    #ส่งข้อมูลออก
    request.session['idcard'] = idcard
    #หาข้อมูลลูกค้าเพื่อไปเเสดง
    datacustomeredit = MSAcustomer.objects.filter(id=idcard).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    #หาข้อมูลประวัติลูกค้าไปเเสดง
    datapathstatus = Pathstatusmsa.objects.filter(id_msacustomer = idcard).values_list('date','statuscustomer','remark', named=True).order_by('-id')
    return render(request, 'editcard.html', {'datacustomeredit':datacustomeredit , 'datapathstatus':datapathstatus})
@login_required(login_url='/firstdata') 
def querydatacustomer(request):
    #เก็บข้อมูลทำเงื่อนในการมองเห็น
    firstname = str(request.session.get('firstname'))#กรณี sell ดูได้เเค่ชื่อตัวเอง
    branchset = str(request.session.get('branchset'))#กรณีไม่ใช่ sell กำหนดการเห็นข้อมูล
    #เก็บข้อมูลเงื่อนไขจากหน้าตัวเอง
    querybranch = str(request.POST.get('querybranch'))
    queryteam = str(request.POST.get('queryteam'))
    querystatus = str(request.POST.get('querystatus'))
    #เงื่อนไขดูข้อมูลของ admin ทั้งหมด มี 8 เงื่อนไข
    if  branchset == "AD@mg.msa":
        if querybranch == 'ทั้งหมด' and queryteam == 'ทั้งหมด' and querystatus == 'ทั้งหมด' :
           datacustomer = MSAcustomer.objects.all().values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif  querybranch != 'ทั้งหมด' and queryteam == 'ทั้งหมด' and querystatus == 'ทั้งหมด' :
           datacustomer = MSAcustomer.objects.filter(Q(msabranch=querybranch)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')   
        elif  querybranch == 'ทั้งหมด' and queryteam != 'ทั้งหมด' and querystatus == 'ทั้งหมด' :
           datacustomer = MSAcustomer.objects.filter(Q(teamsell=queryteam)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')  
        elif  querybranch == 'ทั้งหมด' and queryteam == 'ทั้งหมด' and querystatus != 'ทั้งหมด' :
           datacustomer = MSAcustomer.objects.filter(Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')   
        elif  querybranch == 'ทั้งหมด' and queryteam != 'ทั้งหมด' and querystatus != 'ทั้งหมด' : 
           datacustomer = MSAcustomer.objects.filter(Q(teamsell=queryteam)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id') 
        elif  querybranch != 'ทั้งหมด' and queryteam != 'ทั้งหมด' and querystatus == 'ทั้งหมด' : 
           datacustomer = MSAcustomer.objects.filter(Q(msabranch=querybranch)&Q(teamsell=queryteam)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')  
        elif  querybranch != 'ทั้งหมด' and queryteam == 'ทั้งหมด' and querystatus != 'ทั้งหมด' : 
           datacustomer = MSAcustomer.objects.filter(Q(msabranch=querybranch)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')  
        elif  querybranch != 'ทั้งหมด' and queryteam != 'ทั้งหมด' and querystatus != 'ทั้งหมด' : 
           datacustomer = MSAcustomer.objects.filter(Q(msabranch=querybranch)&Q(teamsell=queryteam)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')  
    #เงื่อนไขดูข้อมูลผจก.
    elif branchset == "HO@mg.msam":
        if queryteam == 'ทั้งหมด' and querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HO")).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam != 'ทั้งหมด' and querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HO")&Q(teamsell=queryteam)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam == 'ทั้งหมด' and querystatus != 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HO")&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam != 'ทั้งหมด' and querystatus != 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HO")&Q(teamsell=queryteam)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    elif branchset == "RS@mg.msam":
        if queryteam == 'ทั้งหมด' and querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "RS")).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam != 'ทั้งหมด' and querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "RS")&Q(teamsell=queryteam)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam == 'ทั้งหมด' and querystatus != 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "RS")&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam != 'ทั้งหมด' and querystatus != 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "RS")&Q(teamsell=queryteam)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    elif branchset == "HTR@mg.msam":
        if queryteam == 'ทั้งหมด' and querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HTR")).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam != 'ทั้งหมด' and querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HTR")&Q(teamsell=queryteam)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam == 'ทั้งหมด' and querystatus != 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HTR")&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        elif queryteam != 'ทั้งหมด' and querystatus != 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(msabranch = "HTR")&Q(teamsell=queryteam)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    #เงื่อนไขดูข้อมูลของ sell 
    else:
        if querystatus == 'ทั้งหมด':
           datacustomer = MSAcustomer.objects.filter(Q(firstname = firstname)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
        else :
           datacustomer = MSAcustomer.objects.filter(Q(firstname = firstname)&Q(statuscustomer=querystatus)).values_list('id','msabranch','teamsell','date','firstname','mainmodel','customername','contactcustomer','chanelcustomer','statuscustomer','remark','quotation',named=True).order_by('-id')
    #ตัวเเปรเเสดงค่าการค้นหา
    querybranch_new = querybranch
    queryteam_new = queryteam
    querystatus_new = querystatus
    #ตัวเเปรนับจำนวนข้อมูล
    countdatacustomer = datacustomer.count()
    return render(request,'statuscustomer.html',{'datacustomer':datacustomer,'branchset':branchset,'countdatacustomer':countdatacustomer,'querystatus_new':querystatus_new,'queryteam_new':queryteam_new,'querybranch_new':querybranch_new})
@login_required(login_url='/firstdata') 
def updatedatacustomer(request):
    if request.method == "POST":
        #ข้อมูลเงื่อนไข
        idcard = request.session.get('idcard')
        # เก็บข้อมูลหน้าตัวเอง/เงื่อนไขว่าจะทำอะไร
        doit = request.POST.get('doit')
        statuscustomerold = request.POST.get('statuscustomer-old') #ที่ไม่เเสดงเเต่ใส่ค่าเอาไว้
        customernameedit = request.POST.get('customername-edit')     
        contactcustomeredit = request.POST.get('contactcustomer-edit')     
        statuscustomeredit = request.POST.get('statuscustomer-edit')     
        customerremark = request.POST.get('customer-remark') 
        #update ข้อมูลทุกครั้งที่มีการเปลี่ยนเเปลง statuscustomer หรือ remark จะถูกบันทึกประวัติ
        if doit == 'update' :
            if customernameedit != "":
                MSAcustomer.objects.filter(id= idcard).update(customername = customernameedit)
            if contactcustomeredit != "":
                MSAcustomer.objects.filter(id= idcard).update(contactcustomer = contactcustomeredit)
            if customerremark != "":
                MSAcustomer.objects.filter(id= idcard).update(remark = customerremark)
            if statuscustomerold != statuscustomeredit :
                MSAcustomer.objects.filter(id= idcard).update(statuscustomer = statuscustomeredit)
            if customerremark != "" or statuscustomerold != statuscustomeredit :
                Pathstatusmsa.objects.create(id_msacustomer= idcard , statuscustomer=statuscustomeredit,remark=customerremark)
        elif doit == 'delete' :
            MSAcustomer.objects.filter(id= idcard).delete()   
            Pathstatusmsa.objects.filter(id_msacustomer = idcard).delete()
    return  redirect('/statuscustomer')
@login_required(login_url='/firstdata') 
def showprice(request): 
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน   
    submodel = request.POST.get('submodel')
    #ส่งข้อมูลออก
    request.session['submodel'] = submodel
    productdata = Product.objects.filter( submodel = submodel).values_list('price','margin', named=True)
    productcolor = Colorsubmodels.objects.filter(submodel = submodel).values_list('submodel','color', named=True)
    for i in productdata :
            productprice =  int(i.price)
            #productmargin = int(i.margin)               
    request.session['productprice'] = productprice     
    #request.session['productmargin'] = productmargin     
    return render(request, 'showprice.html',{"productprice": '{:,}'.format(productprice), "submodel": submodel, "productcolor": productcolor})
@login_required(login_url='/firstdata') 
def PaymentRegis(request):
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    submodel = request.session.get('submodel')
    mainmodel = request.session.get('mainmodel')
    productprice = int(request.session.get('productprice'))
    #productmargin = int(request.session.get('productmargin'))
    
    text_productprice = productprice
    
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    paytype = request.POST.get('paytype') 
    bodycolor = request.POST.get('bodycolor') 
    mgbranch = request.POST.get('mgbranch') 
    registype = request.POST.get('registype') 
   
    #ส่งข้อมูลออก
    request.session['paytype'] = paytype
    request.session['bodycolor'] = bodycolor
    request.session['mgbranch'] = mgbranch
    request.session['registype'] = registype
    regiscost = Regiscosts.objects.filter(regis_code = submodel).values_list('regis_personal','regis_company', named=True)
    for i in regiscost :
        if registype == 'person' :
           regiscost = int(i.regis_personal)
        elif registype == 'company' :
           regiscost = int(i.regis_company)
    request.session['regiscost'] = regiscost
    # query หา acc ตามเงื่อนไข ถ้าเป็น VS ใช้ของ ZS
    if mainmodel == 'MGVSHEV' :
        mainacc = Accmgs.objects.filter(Q(acc_model = 'MGZS') | Q(acc_model = 'ALL')).values_list('id', 'acc_code', 'acc_name','acc_price','acc_type', named=True).order_by('acc_code')
        if paytype == 'cash':
             return render(request, 'branchcash.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,})
    
        elif paytype == 'finance' :
            return render(request, 'branchadd.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,'productprice':productprice,'mainmodel': mainmodel})
    elif mainmodel == 'MGHSPHEV' :
        mainacc = Accmgs.objects.filter(Q(acc_model = 'MGHS') | Q(acc_model = 'ALL')).values_list('id', 'acc_code', 'acc_name','acc_price','acc_type', named=True).order_by('acc_code')
        if paytype == 'cash':
             return render(request, 'branchcash.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,})
    
        elif paytype == 'finance' :
            return render(request, 'branchadd.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,'productprice':productprice,'mainmodel': mainmodel})

    else :
        mainacc = Accmgs.objects.filter(Q(acc_model = mainmodel) | Q(acc_model = 'ALL')).values_list('id', 'acc_code', 'acc_name','acc_price','acc_type', named=True).order_by('acc_code')

        if paytype == 'cash':
             return render(request, 'branchcash.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,})
    
        elif paytype == 'finance' :
            return render(request, 'branchadd.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,'productprice':productprice,'mainmodel': mainmodel})
@login_required(login_url='/firstdata') 
def branceadd (request):
#สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    firstname = str(request.session.get('firstname'))
    sellphone = str(request.session.get('sellphone'))
    regiscost = int(request.session.get('regiscost'))
    productprice = int(request.session.get('productprice'))
    paytype = str(request.session.get('paytype'))
    customername = str(request.session.get('customername'))
    contactcustomer = str(request.session.get('contactcustomer'))
    #productmargin  = int(request.session.get('productmargin'))
    
#เก็บข้อมูลหน้าตัวเอง
    #เก็บค่าอุปกรณ์ตกเเต่งกรอกเอง
    text_acc_card = str(request.POST.get('text_acc_card')or "-")
    min_acc_card = int(request.POST.get('min_acc_card')or 0)
    text_acc_card_1 = str(request.POST.get('text_acc_card_1')or "-")
    min_acc_card_1 = int(request.POST.get('min_acc_card_1')or 0)
    text_acc_card_2 = str(request.POST.get('text_acc_card_2')or "-")
    min_acc_card_2 = int(request.POST.get('min_acc_card_2')or 0)
    text_acc_card_3 = str(request.POST.get('text_acc_card_3')or "-")
    min_acc_card_3 = int(request.POST.get('min_acc_card_3')or 0)
    text_acc_card_4 = str(request.POST.get('text_acc_card_4')or "-")
    min_acc_card_4 = int(request.POST.get('min_acc_card_4')or 0)
    text_acc_card_5 = str(request.POST.get('text_acc_card_5')or "-")
    min_acc_card_5 = int(request.POST.get('min_acc_card_5')or 0)
    text_acc_card_6 = str(request.POST.get('text_acc_card_6')or "-")
    min_acc_card_6 = int(request.POST.get('min_acc_card_6')or 0)
    text_acc_card_7 = str(request.POST.get('text_acc_card_7')or "-")
    min_acc_card_7 = int(request.POST.get('min_acc_card_7')or 0)
    text_acc_card_8 = str(request.POST.get('text_acc_card_8')or "-")
    min_acc_card_8 = int(request.POST.get('min_acc_card_8')or 0)
    text_acc_card_9 = str(request.POST.get('text_acc_card_9')or "-")
    min_acc_card_9 = int(request.POST.get('min_acc_card_9')or 0)
    min_acc_typing = [min_acc_card,min_acc_card_1,min_acc_card_2,min_acc_card_3
    ,min_acc_card_4,min_acc_card_5,min_acc_card_6,min_acc_card_7,min_acc_card_8
    ,min_acc_card_9]
    #รายการอุปกรณ์ตกเเต่งเเบบรายการ
    min_acc_1_code = str(request.POST.get('min_acc_1_code'))
    min_acc_2_code =str(request.POST.get('min_acc_2_code'))
    min_acc_3_code = str(request.POST.get('min_acc_3_code'))
    min_acc_4_code = str(request.POST.get('min_acc_4_code'))
    min_acc_5_code = str(request.POST.get('min_acc_5_code'))
    min_acc_6_code = str(request.POST.get('min_acc_6_code'))
    min_acc_7_code = str(request.POST.get('min_acc_7_code'))
    min_acc_8_code = str(request.POST.get('min_acc_8_code'))
    min_acc_9_code = str(request.POST.get('min_acc_9_code'))
    min_acc_10_code = str(request.POST.get('min_acc_10_code'))
    min_acc_11_code = str(request.POST.get('min_acc_11_code'))
    min_acc_12_code = str(request.POST.get('min_acc_12_code'))
    min_acc_13_code = str(request.POST.get('min_acc_13_code'))
    min_acc_14_code = str(request.POST.get('min_acc_14_code'))
    min_acc_15_code = str(request.POST.get('min_acc_15_code'))
    list_acc_code = [min_acc_1_code, min_acc_2_code, min_acc_3_code, min_acc_4_code
    ,min_acc_5_code, min_acc_6_code,min_acc_7_code, min_acc_8_code
    ,min_acc_9_code,min_acc_10_code,min_acc_11_code,min_acc_12_code
    ,min_acc_13_code,min_acc_14_code,min_acc_15_code]
    try :
       gen_inter= float(request.POST.get('gen_inter')or 0)
    except ValueError as gen_inter :
        error_code = "gen_inter"
        return render(request, 'err.html',{"error_code":error_code})
    try :
       gen_inter2= float(request.POST.get('gen_inter2')or 0)
    except ValueError as gen_inter2 :
        error_code = "gen_inter"
        return render(request, 'err.html',{"error_code":error_code})
    try :
       gen_inter3= float(request.POST.get('gen_inter3')or 0)
    except ValueError as gen_inter3 :
        error_code = "gen_inter"
        return render(request, 'err.html',{"error_code":error_code})
    try :
       min_inter = float(request.POST.get('min_inter')or gen_inter)
    except ValueError as min_inter : 
        error_code = "min_inter"
        return render(request, 'err.html',{"error_code":error_code})
    productmargin = int(request.POST.get('productmargin')or 0)
    gen_company = str(request.POST.get('gen_company'))
    gen_down = int(request.POST.get('gen_down') or 0)
    gen_month= int(request.POST.get('gen_month'))
    gen_month2= int(request.POST.get('gen_month2'))
    gen_month3= int(request.POST.get('gen_month3'))
    gen_prepay= int(request.POST.get('gen_prepay')or 0)
    add_eq = int(request.POST.get('add_eq')or 0) 
    add_kickback = int(request.POST.get('add_kickback')or 0)
    com_fi_percent = int(request.POST.get('com_fi_percent'))
    com_fi_month = int(request.POST.get('com_fi_month'))
    min_prosub = int(request.POST.get('min_prosub')or 0)
    min_reduce = int(request.POST.get('min_reduce')or 0)
    gen_remark = str(request.POST.get('gen_remark')or "-")
    min_subdown = int(request.POST.get('min_subdown')or 0)
    condition_finance = str(request.POST.get('condition_finance')) # BEGIN / END
    min_regis = str(request.POST.get('min_regis')or 'N') # Y = เเถม / N = ไม่เเถม
    min_subdown_vat = str(request.POST.get('min_subdown_vat')or 'N') # Y = เเถม / N = ไม่เเถม

#คำนวณค่า
    #ราคารถสุทธิ
    netproductprice = netproductprice_m(productprice,min_reduce,add_eq)
    #รายการเงินดาวน์
    down_data = costdown_m(netproductprice,gen_down,min_subdown)
    #เงินดาวน์ไฟเเนนซ์
    cost_down = down_data[0]
    #เงินดาวน๋วันออกรถ 
    exit_cost_down = down_data[1]
    # vat subdown 
    exit_cost_down_vat = down_data[2]
    #ยอดจัดไฟเเนนซ์
    cost_finance = costfinance_m(netproductprice,cost_down)
    #ซับดอกเบี้ย
    subsidy_inter = subsidy_inter_m(cost_finance,gen_month,gen_inter,min_inter)
    #การ subsidy ทั้งหมด
    sumsubsidy = sumsubsidy_m(subsidy_inter,min_prosub)
    #ดอกเบี้ยต่อปี
    interyear = interyear_m(cost_finance,min_inter)
    interyear2 = interyear_m(cost_finance,gen_inter2)
    interyear3 = interyear_m(cost_finance,gen_inter3)
    #ดอกเบี้ยทั้งหมด
    total_inter = totalinter_m(interyear,gen_month)
    total_inter2 = totalinter_m(interyear2,gen_month2)
    total_inter3 = totalinter_m(interyear3,gen_month3)
    #เงินที่ต้องผ่อนไฟเเนนซ์
    debt_fi = debt_fi_m(cost_finance,total_inter)
    debt_fi2 = debt_fi_m(cost_finance,total_inter2)
    debt_fi3 = debt_fi_m(cost_finance,total_inter3)
    #ค่างวด
    month_payment = monthpayment_m(debt_fi,gen_month)
    month_payment2 = monthpayment_m(debt_fi2,gen_month2)
    month_payment3 = monthpayment_m(debt_fi3,gen_month3)
    #ค่า com finance
    total_com_finance = total_com_finance_m(interyear,com_fi_percent,com_fi_month)
    #ค่าอุปกณณ์ตกเเต่ง
    dataacc = listacc_m(list_acc_code)
    minacc_code_name = dataacc[0]
    minacc_code_price = dataacc[1] 
    min_acc_typing = minacc_typing_m(min_acc_typing)
    min_acc = minacc_m(min_acc_typing,minacc_code_price)
    #รายการของเเถมอื่น
    gift_data = msa_gift_m(min_acc,min_subdown_vat,exit_cost_down_vat,min_regis,regiscost)
    #ของบังคับเเถม
    force_gift = gift_data[0]
    #ของเเถมเลือกได้
    choose_gift = gift_data[1]
    #รวมรายการของเเถมทั้งหมด
    total_gift = gift_data[2]
    #รวมส่วนลดส่วนลด
    total_minmargin = total_minmargin_m(min_reduce,min_subdown,sumsubsidy,total_gift)
    #ส่วนเพิ่มส่วนลด
    total_addmargin = totaladdmargin_m(total_com_finance,add_eq,add_kickback)
    #ส่วนลดสุทธิ
    total_margin = total_margin_m(productmargin,total_addmargin,total_minmargin)
    #ค่าใช้จ่ายวันออกรถ
    total_exit = total_exit_m(exit_cost_down,condition_finance,month_payment,min_regis,regiscost,min_subdown_vat,exit_cost_down_vat,gen_prepay)
    #ค่าใช้จ่ายทั้งหมดที่ลูกค้าต้องจ่าย
    net_total_payment = net_total_payment_m(debt_fi,exit_cost_down)
    net_total_payment2 = net_total_payment_m(debt_fi2,exit_cost_down)
    net_total_payment3 = net_total_payment_m(debt_fi3,exit_cost_down)
    #กระจายค่ารายการชื่ออุปกรณ์ตกเเต่งเเบบรายการ
    text_acc_1 = minacc_code_name[0]
    text_acc_2 = minacc_code_name[1]
    text_acc_3 = minacc_code_name[2]
    text_acc_4 = minacc_code_name[3]
    text_acc_5 = minacc_code_name[4]
    text_acc_6 = minacc_code_name[5]
    text_acc_7 = minacc_code_name[6]
    text_acc_8 = minacc_code_name[7]
    text_acc_9 = minacc_code_name[8]
    text_acc_10 = minacc_code_name[9]
    text_acc_11 = minacc_code_name[10]
    text_acc_12 = minacc_code_name[11]
    text_acc_13 = minacc_code_name[12]
    text_acc_14 = minacc_code_name[13]
    text_acc_15 = minacc_code_name[14]
#ส่งข้อมูลออก
    #ข้อมูลคำนวณ
    request.session['netproductprice'] = netproductprice
    request.session['cost_down'] = cost_down
    request.session['exit_cost_down'] = exit_cost_down
    request.session['exit_cost_down_vat'] = exit_cost_down_vat
    request.session['cost_finance'] = cost_finance
    request.session['month_payment'] = month_payment
    request.session['month_payment2'] = month_payment2
    request.session['month_payment3'] = month_payment3
    request.session['total_com_finance'] = total_com_finance
    request.session['total_addmargin'] = total_addmargin
    request.session['total_minmargin'] = total_minmargin
    request.session['total_margin'] = total_margin
    request.session['total_exit'] = total_exit
    request.session['subsidy_inter'] = subsidy_inter
    request.session['sumsubsidy'] = sumsubsidy
     #ข้อมูลออกตัวเเปร
    request.session['red_frame'] = red_frame
    request.session['gen_company'] = gen_company
    request.session['gen_prepay'] = gen_prepay
    request.session['gen_down'] = gen_down
    request.session['gen_month'] = gen_month
    request.session['gen_month2'] = gen_month2
    request.session['gen_month3'] = gen_month3
    request.session['condition_finance'] = condition_finance
    request.session['gen_inter'] = gen_inter
    request.session['gen_inter2'] = gen_inter2
    request.session['gen_inter3'] = gen_inter3
    request.session['add_eq'] = add_eq
    request.session['add_kickback'] = add_kickback
    request.session['com_fi_percent'] = com_fi_percent
    request.session['com_fi_monthl'] = com_fi_month
    request.session['min_reduce'] = min_reduce
    request.session['min_regis'] = min_regis
    request.session['min_pdi'] = min_pdi
    request.session['min_frame'] = min_frame
    request.session['min_polish'] = min_polish
    request.session['min_subdown'] = min_subdown
    request.session['min_subdown_vat'] = min_subdown_vat
    request.session['min_acc'] = min_acc
    request.session['gen_remark'] = gen_remark
    request.session['min_prosub'] = min_prosub
    request.session['min_inter'] = min_inter
    #ส่งชื่ออุปกรณ์ตกเเต่ง
    request.session['text_acc_card'] = text_acc_card
    request.session['text_acc_card_1'] = text_acc_card_1
    request.session['text_acc_card_2'] = text_acc_card_2
    request.session['text_acc_card_3'] = text_acc_card_3
    request.session['text_acc_card_4'] = text_acc_card_4
    request.session['text_acc_card_5'] = text_acc_card_5
    request.session['text_acc_card_6'] = text_acc_card_6
    request.session['text_acc_card_7'] = text_acc_card_7
    request.session['text_acc_card_8'] = text_acc_card_8
    request.session['text_acc_card_9'] = text_acc_card_9
    request.session['text_acc_1'] = text_acc_1
    request.session['text_acc_2'] = text_acc_2
    request.session['text_acc_3'] = text_acc_3
    request.session['text_acc_4'] = text_acc_4
    request.session['text_acc_5'] = text_acc_5
    request.session['text_acc_6'] = text_acc_6
    request.session['text_acc_7'] = text_acc_7
    request.session['text_acc_8'] = text_acc_8
    request.session['text_acc_9'] = text_acc_9
    request.session['text_acc_10'] = text_acc_10
    request.session['text_acc_11'] = text_acc_11
    request.session['text_acc_12'] = text_acc_12
    request.session['text_acc_13'] = text_acc_13
    request.session['text_acc_14'] = text_acc_14
    request.session['text_acc_15'] = text_acc_15
    #ข้อมูลส่งหน้าถัดไป
    data = {#ส่วนลดคงเหลือ
        'total_margin':'{:,.0f}'.format(total_margin),
        'productmargin':'{:,}'.format(productmargin), 
        'total_addmargin':'{:,.0f}'.format(total_addmargin),
        'total_minmargin':'{:,.0f}'.format(total_minmargin),
        #ส่วนเพิ่มส่วนลด
        'add_eq':'{:,}'.format(add_eq), 
        'add_kickback':'{:,}'.format(add_kickback),
        'total_com_finance':'{:,.0f}'.format(total_com_finance),
        #การใช้ส่วนลด
        'min_reduce':'{:,}'.format(min_reduce),
        'total_gift':'{:,}'.format(total_gift),
        'min_subdown':'{:,}'.format(min_subdown),
        'sumsubsidy':'{:,}'.format(sumsubsidy), 
        #ค่าใช้จ่ายวันออกรถ
        'paytype':paytype,
        'total_exit':'{:,}'.format(total_exit),
        'exit_cost_down':'{:,}'.format(exit_cost_down),
        'gen_prepay':'{:,}'.format(gen_prepay),
        'min_regis':min_regis,
        'regiscost':'{:,}'.format(regiscost),
        'min_subdown_vat':min_subdown_vat,
        'exit_cost_down_vat':'{:,}'.format(exit_cost_down_vat),
        'condition_finance':condition_finance,   
        #รายละเอียดเพิ่มเติม
        'month_payment':'{:,.0f}'.format(month_payment),
        'month_payment2':'{:,.0f}'.format(month_payment2),
        'month_payment3':'{:,.0f}'.format(month_payment3),
        'total_inter' :'{:,}'.format(total_inter),
        'total_inter2' :'{:,}'.format(total_inter2),
        'total_inter3' :'{:,}'.format(total_inter3),
        'net_total_payment':'{:,}'.format(net_total_payment),
        'net_total_payment2':'{:,}'.format(net_total_payment2),
        'net_total_payment3':'{:,}'.format(net_total_payment3),
        #ข้อมูลการติดต่อ
        'firstname':firstname,
        'customername':customername,
        'sellphone':sellphone,
        'contactcustomer':contactcustomer,
    }
    return render(request, 'showdatafinance.html', data)
@login_required(login_url='/firstdata') 
def branchcash (request):
#สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    firstname = str(request.session.get('firstname'))
    sellphone = str(request.session.get('sellphone'))
    regiscost = int(request.session.get('regiscost'))
    productprice = int(request.session.get('productprice'))
    paytype = str(request.session.get('paytype'))
    customername = str(request.session.get('customername'))
    contactcustomer = str(request.session.get('contactcustomer'))
    #productmargin  = int(request.session.get('productmargin'))
    
#เก็บข้อมูลหน้าตัวเอง
    #เก็บค่าอุปกรณ์ตกเเต่งกรอกเอง
    text_acc_card = str(request.POST.get('text_acc_card')or "-")
    min_acc_card = int(request.POST.get('min_acc_card')or 0)
    text_acc_card_1 = str(request.POST.get('text_acc_card_1')or "-")
    min_acc_card_1 = int(request.POST.get('min_acc_card_1')or 0)
    text_acc_card_2 = str(request.POST.get('text_acc_card_2')or "-")
    min_acc_card_2 = int(request.POST.get('min_acc_card_2')or 0)
    text_acc_card_3 = str(request.POST.get('text_acc_card_3')or "-")
    min_acc_card_3 = int(request.POST.get('min_acc_card_3')or 0)
    text_acc_card_4 = str(request.POST.get('text_acc_card_4')or "-")
    min_acc_card_4 = int(request.POST.get('min_acc_card_4')or 0)
    text_acc_card_5 = str(request.POST.get('text_acc_card_5')or "-")
    min_acc_card_5 = int(request.POST.get('min_acc_card_5')or 0)
    text_acc_card_6 = str(request.POST.get('text_acc_card_6')or "-")
    min_acc_card_6 = int(request.POST.get('min_acc_card_6')or 0)
    text_acc_card_7 = str(request.POST.get('text_acc_card_7')or "-")
    min_acc_card_7 = int(request.POST.get('min_acc_card_7')or 0)
    text_acc_card_8 = str(request.POST.get('text_acc_card_8')or "-")
    min_acc_card_8 = int(request.POST.get('min_acc_card_8')or 0)
    text_acc_card_9 = str(request.POST.get('text_acc_card_9')or "-")
    min_acc_card_9 = int(request.POST.get('min_acc_card_9')or 0)
    min_acc_typing = [min_acc_card,min_acc_card_1,min_acc_card_2,min_acc_card_3
    ,min_acc_card_4,min_acc_card_5,min_acc_card_6,min_acc_card_7,min_acc_card_8
    ,min_acc_card_9]
    #รายการอุปกรณ์ตกเเต่งเเบบรายการ
    min_acc_1_code = str(request.POST.get('min_acc_1_code'))
    min_acc_2_code =str(request.POST.get('min_acc_2_code'))
    min_acc_3_code = str(request.POST.get('min_acc_3_code'))
    min_acc_4_code = str(request.POST.get('min_acc_4_code'))
    min_acc_5_code = str(request.POST.get('min_acc_5_code'))
    min_acc_6_code = str(request.POST.get('min_acc_6_code'))
    min_acc_7_code = str(request.POST.get('min_acc_7_code'))
    min_acc_8_code = str(request.POST.get('min_acc_8_code'))
    min_acc_9_code = str(request.POST.get('min_acc_9_code'))
    min_acc_10_code = str(request.POST.get('min_acc_10_code'))
    min_acc_11_code = str(request.POST.get('min_acc_11_code'))
    min_acc_12_code = str(request.POST.get('min_acc_12_code'))
    min_acc_13_code = str(request.POST.get('min_acc_13_code'))
    min_acc_14_code = str(request.POST.get('min_acc_14_code'))
    min_acc_15_code = str(request.POST.get('min_acc_15_code'))
    list_acc_code = [min_acc_1_code, min_acc_2_code, min_acc_3_code, min_acc_4_code
    ,min_acc_5_code, min_acc_6_code,min_acc_7_code, min_acc_8_code
    ,min_acc_9_code,min_acc_10_code,min_acc_11_code,min_acc_12_code
    ,min_acc_13_code,min_acc_14_code,min_acc_15_code]
       
    gen_inter= 0
    min_inter = 0
    productmargin = int(request.POST.get('productmargin')or 0)
    gen_company = '-'
    gen_down = 100
    gen_month= 1
    gen_prepay= int(request.POST.get('gen_prepay')or 0)
    add_eq = 0
    add_kickback = 0
    com_fi_percent = 0
    com_fi_month = 0
    min_prosub = 0
    min_reduce = int(request.POST.get('min_reduce')or 0)
    gen_remark = str(request.POST.get('gen_remark')or "-")
    min_subdown = 0
    condition_finance = str(request.POST.get('condition_finance')) # BEGIN / END
    min_regis = str(request.POST.get('min_regis')or 'N') # Y = เเถม / N = ไม่เเถม
    min_subdown_vat = str(request.POST.get('min_subdown_vat')or 'N') # Y = เเถม / N = ไม่เเถม

#คำนวณค่า
    #ราคารถสุทธิ
    netproductprice = netproductprice_m(productprice,min_reduce,add_eq)
    #รายการเงินดาวน์
    down_data = costdown_m(netproductprice,gen_down,min_subdown)
    #เงินดาวน์ไฟเเนนซ์
    cost_down = down_data[0]
    #เงินดาวน๋วันออกรถ 
    exit_cost_down = down_data[1]
    # vat subdown 
    exit_cost_down_vat = down_data[2]
    #ยอดจัดไฟเเนนซ์
    cost_finance = costfinance_m(netproductprice,cost_down)
    #ซับดอกเบี้ย
    subsidy_inter = subsidy_inter_m(cost_finance,gen_month,gen_inter,min_inter)
    #การ subsidy ทั้งหมด
    sumsubsidy = sumsubsidy_m(subsidy_inter,min_prosub)
    #ดอกเบี้ยต่อปี
    interyear = interyear_m(cost_finance,min_inter)
    #ดอกเบี้ยทั้งหมด
    total_inter = totalinter_m(interyear,gen_month)
    #เงินที่ต้องผ่อนไฟเเนนซ์
    debt_fi = debt_fi_m(cost_finance,total_inter)
    #ค่างวด
    month_payment = monthpayment_m(debt_fi,gen_month)
    #ค่า com finance
    total_com_finance = total_com_finance_m(interyear,com_fi_percent,com_fi_month)
    #ค่าอุปกณณ์ตกเเต่ง
    dataacc = listacc_m(list_acc_code)
    minacc_code_name = dataacc[0]
    minacc_code_price = dataacc[1] 
    min_acc_typing = minacc_typing_m(min_acc_typing)
    min_acc = minacc_m(min_acc_typing,minacc_code_price)
    #รายการของเเถมอื่น
    gift_data = msa_gift_m(min_acc,min_subdown_vat,exit_cost_down_vat,min_regis,regiscost)
    #ของบังคับเเถม
    force_gift = gift_data[0]
    #ของเเถมเลือกได้
    choose_gift = gift_data[1]
    #รวมรายการของเเถมทั้งหมด
    total_gift = gift_data[2]
    #รวมส่วนลดส่วนลด
    total_minmargin = total_minmargin_m(min_reduce,min_subdown,sumsubsidy,total_gift)
    #ส่วนเพิ่มส่วนลด
    total_addmargin = totaladdmargin_m(total_com_finance,add_eq,add_kickback)
    #ส่วนลดสุทธิ
    total_margin = total_margin_m(productmargin,total_addmargin,total_minmargin)
    #ค่าใช้จ่ายวันออกรถ
    total_exit = total_exit_m(exit_cost_down,condition_finance,month_payment,min_regis,regiscost,min_subdown_vat,exit_cost_down_vat,gen_prepay)
    #ค่าใช้จ่ายทั้งหมดที่ลูกค้าต้องจ่าย
    net_total_payment = net_total_payment_m(debt_fi,exit_cost_down)
    #กระจายค่ารายการชื่ออุปกรณ์ตกเเต่งเเบบรายการ
    text_acc_1 = minacc_code_name[0]
    text_acc_2 = minacc_code_name[1]
    text_acc_3 = minacc_code_name[2]
    text_acc_4 = minacc_code_name[3]
    text_acc_5 = minacc_code_name[4]
    text_acc_6 = minacc_code_name[5]
    text_acc_7 = minacc_code_name[6]
    text_acc_8 = minacc_code_name[7]
    text_acc_9 = minacc_code_name[8]
    text_acc_10 = minacc_code_name[9]
    text_acc_11 = minacc_code_name[10]
    text_acc_12 = minacc_code_name[11]
    text_acc_13 = minacc_code_name[12]
    text_acc_14 = minacc_code_name[13]
    text_acc_15 = minacc_code_name[14]
#ส่งข้อมูลออก
    #ข้อมูลคำนวณ
    request.session['netproductprice'] = netproductprice
    request.session['cost_down'] = cost_down
    request.session['exit_cost_down'] = exit_cost_down
    request.session['exit_cost_down_vat'] = exit_cost_down_vat
    request.session['cost_finance'] = cost_finance
    request.session['month_payment'] = month_payment
    request.session['total_com_finance'] = total_com_finance
    request.session['total_addmargin'] = total_addmargin
    request.session['total_minmargin'] = total_minmargin
    request.session['total_margin'] = total_margin
    request.session['total_exit'] = total_exit
    request.session['subsidy_inter'] = subsidy_inter
    request.session['sumsubsidy'] = sumsubsidy
    #ข้อมูลออกตัวเเปร
    request.session['red_frame'] = red_frame
    request.session['gen_company'] = gen_company
    request.session['gen_prepay'] = gen_prepay
    request.session['gen_down'] = gen_down
    request.session['gen_month'] = gen_month
    request.session['condition_finance'] = condition_finance
    request.session['gen_inter'] = gen_inter
    request.session['add_eq'] = add_eq
    request.session['add_kickback'] = add_kickback
    request.session['com_fi_percent'] = com_fi_percent
    request.session['com_fi_monthl'] = com_fi_month
    request.session['min_reduce'] = min_reduce
    request.session['min_regis'] = min_regis
    request.session['min_pdi'] = min_pdi
    request.session['min_frame'] = min_frame
    request.session['min_polish'] = min_polish
    request.session['min_subdown'] = min_subdown
    request.session['min_subdown_vat'] = min_subdown_vat
    request.session['min_acc'] = min_acc
    request.session['gen_remark'] = gen_remark
    request.session['min_prosub'] = min_prosub
    request.session['min_inter'] = min_inter
    #ส่งชื่ออุปกรณ์ตกเเต่ง
    request.session['text_acc_card'] = text_acc_card
    request.session['text_acc_card_1'] = text_acc_card_1
    request.session['text_acc_card_2'] = text_acc_card_2
    request.session['text_acc_card_3'] = text_acc_card_3
    request.session['text_acc_card_4'] = text_acc_card_4
    request.session['text_acc_card_5'] = text_acc_card_5
    request.session['text_acc_card_6'] = text_acc_card_6
    request.session['text_acc_card_7'] = text_acc_card_7
    request.session['text_acc_card_8'] = text_acc_card_8
    request.session['text_acc_card_9'] = text_acc_card_9
    request.session['text_acc_1'] = text_acc_1
    request.session['text_acc_2'] = text_acc_2
    request.session['text_acc_3'] = text_acc_3
    request.session['text_acc_4'] = text_acc_4
    request.session['text_acc_5'] = text_acc_5
    request.session['text_acc_6'] = text_acc_6
    request.session['text_acc_7'] = text_acc_7
    request.session['text_acc_8'] = text_acc_8
    request.session['text_acc_9'] = text_acc_9
    request.session['text_acc_10'] = text_acc_10
    request.session['text_acc_11'] = text_acc_11
    request.session['text_acc_12'] = text_acc_12
    request.session['text_acc_13'] = text_acc_13
    request.session['text_acc_14'] = text_acc_14
    request.session['text_acc_15'] = text_acc_15
    #ข้อมูลส่งหน้าถัดไป
    data = {#ส่วนลดคงเหลือ
        'total_margin':'{:,.0f}'.format(total_margin),
        'productmargin':'{:,}'.format(productmargin), 
        'total_addmargin':'{:,.0f}'.format(total_addmargin),
        'total_minmargin':'{:,.0f}'.format(total_minmargin),
        #ส่วนเพิ่มส่วนลด
        'add_eq':'{:,}'.format(add_eq), 
        'add_kickback':'{:,}'.format(add_kickback),
        'total_com_finance':'{:,.0f}'.format(total_com_finance),
        #การใช้ส่วนลด
        'min_reduce':'{:,}'.format(min_reduce),
        'total_gift':'{:,}'.format(total_gift),
        'min_subdown':'{:,}'.format(min_subdown),
        'sumsubsidy':'{:,}'.format(sumsubsidy), 
        #ค่าใช้จ่ายวันออกรถ
        'paytype':paytype,
        'total_exit':'{:,}'.format(total_exit),
        'exit_cost_down':'{:,}'.format(exit_cost_down),
        'gen_prepay':'{:,}'.format(gen_prepay),
        'min_regis':min_regis,
        'regiscost':'{:,}'.format(regiscost),
        'min_subdown_vat':min_subdown_vat,
        'exit_cost_down_vat':'{:,}'.format(exit_cost_down_vat),
        'condition_finance':condition_finance,   
        #รายละเอียดเพิ่มเติม
        'month_payment':'{:,.0f}'.format(month_payment),
        'total_inter' :'{:,}'.format(total_inter),
        'net_total_payment':'{:,}'.format(net_total_payment),
        #ข้อมูลการติดต่อ
        'firstname':firstname,
        'customername':customername,
        'sellphone':sellphone,
        'contactcustomer':contactcustomer,
    }
    return render(request, 'showdatafinance.html', data)
@login_required(login_url='/firstdata') 
def showdata(request):
   #ข้อมูลทั่วไป
   now = datetime.today()
   submodel = str(request.session.get('submodel'))
   bodycolor = str(request.session.get('bodycolor'))
   paytype = str(request.session.get('paytype'))
   registype = str(request.session.get('registype'))
   mgbranch = str(request.session.get('mgbranch'))
   #รายละเอียดการซื้อรถยนต์
   productprice = int(request.session.get('productprice'))
   add_eq = int(request.session.get('add_eq'))
   min_reduce = int(request.session.get('min_reduce'))
   netproductprice = int(request.session.get('netproductprice'))
   gen_down = int(request.session.get('gen_down'))
   cost_down = int(request.session.get('cost_down'))
   min_subdown = int(request.session.get('min_subdown'))
   exit_cost_down = int(request.session.get('exit_cost_down'))
   cost_finance = int(request.session.get('cost_finance'))
   gen_month = int(request.session.get('gen_month'))
   gen_month2 = (request.session.get('gen_month2'))
   gen_month3 = (request.session.get('gen_month3'))
   add_kickback = int(request.session.get('add_kickback'))#ยังไม่นำเสดง
   gen_inter = float(request.session.get('gen_inter'))#ยังไม่นำเสดง
   gen_inter2 = float(request.session.get('gen_inter2'))
   gen_inter3 = float(request.session.get('gen_inter3'))
   min_inter = float(request.session.get('min_inter'))
   min_prosub = int(request.session.get('min_prosub'))
   month_payment = int(request.session.get('month_payment'))
   month_payment2 = int(request.session.get('month_payment2'))
   month_payment3 = int(request.session.get('month_payment3'))
   condition_finance = str(request.session.get('condition_finance'))
   gen_company = str(request.session.get('gen_company'))
   #รายละเอียดวันออกรถ
   gen_prepay = int(request.session.get('gen_prepay'))
   total_exit = int(request.session.get('total_exit'))
   min_regis = str(request.session.get('min_regis'))
   regiscost = int(request.session.get('regiscost'))
   min_subdown_vat = str(request.session.get('min_subdown_vat'))
   exit_cost_down_vat = int(request.session.get('exit_cost_down_vat'))      
   #รายการของเเถมอุปกรณ์ตกเเต่ง 
   text_acc_card = str(request.session.get('text_acc_card'))
   text_acc_card_1 = str(request.session.get('text_acc_card_1'))
   text_acc_card_2 = str(request.session.get('text_acc_card_2'))
   text_acc_card_3 = str(request.session.get('text_acc_card_3'))
   text_acc_card_4 = str(request.session.get('text_acc_card_4'))
   text_acc_card_5 = str(request.session.get('text_acc_card_5'))
   text_acc_card_6 = str(request.session.get('text_acc_card_6'))
   text_acc_card_7 = str(request.session.get('text_acc_card_7'))
   text_acc_card_8 = str(request.session.get('text_acc_card_8'))
   text_acc_card_9 = str(request.session.get('text_acc_card_9'))
   text_acc_1 = str(request.session.get('text_acc_1'))
   text_acc_2 = str(request.session.get('text_acc_2'))
   text_acc_3 = str(request.session.get('text_acc_3'))
   text_acc_4 = str(request.session.get('text_acc_4'))
   text_acc_5 = str(request.session.get('text_acc_5'))
   text_acc_6 = str(request.session.get('text_acc_6'))
   text_acc_7 = str(request.session.get('text_acc_7'))
   text_acc_8 = str(request.session.get('text_acc_8'))
   text_acc_9 = str(request.session.get('text_acc_9'))
   text_acc_10 = str(request.session.get('text_acc_10'))
   text_acc_11 = str(request.session.get('text_acc_11'))
   text_acc_12 = str(request.session.get('text_acc_12'))
   text_acc_13 = str(request.session.get('text_acc_13'))
   text_acc_14 = str(request.session.get('text_acc_14'))
   text_acc_15 = str(request.session.get('text_acc_15'))
   #หมายเหตุ
   gen_remark = str(request.session.get('gen_remark'))
   #ข้อมูลการติดต่อ
   firstname = str(request.session.get('firstname'))
   sellphone = str(request.session.get('sellphone'))
   customername = str(request.session.get('customername'))
   contactcustomer = str(request.session.get('contactcustomer'))
   # รวมข้อมูลเพื่อส่งไปหน้าใบเสนอราคา
   dataquo = {
      'now':now,
      'submodel':submodel,
      'gen_remark':gen_remark,
      'bodycolor':bodycolor,
      'mgbranch':mgbranch,
      'registype':registype,
      'paytype':paytype, 
      'gen_month':gen_month, 
      'gen_month2':gen_month2, 
      'gen_month3':gen_month3, 
      'gen_company':gen_company, 
      'condition_finance':condition_finance, 
      'min_regis':min_regis, 
      'regiscost':'{:,.0f}'.format(regiscost), 
      'productprice':'{:,.0f}'.format(productprice), 
      'exit_cost_down':'{:,.0f}'.format(exit_cost_down), 
      'cost_down':'{:,.0f}'.format(cost_down), 
      'total_exit':'{:,.0f}'.format(total_exit), 
      'min_prosub':'{:,.0f}'.format(min_prosub), 
      'netproductprice':'{:,.0f}'.format(netproductprice), 
      'gen_down':'{:,.0f}'.format(gen_down), 
      'add_eq':'{:,.0f}'.format(add_eq), 
      'gen_prepay':'{:,.0f}'.format(gen_prepay), 
      'min_subdown':'{:,.0f}'.format(min_subdown), 
      'min_reduce':'{:,.0f}'.format(min_reduce), 
      'add_kickback':'{:,.0f}'.format(add_kickback), 
      'cost_finance':'{:,}'.format(cost_finance), 
      'month_payment':'{:,}'.format(month_payment), 
      'month_payment2':'{:,}'.format(month_payment2), 
      'month_payment3':'{:,}'.format(month_payment3), 
      'min_inter':'{:,.2f}'.format(min_inter), 
      'gen_inter2':'{:,.2f}'.format(gen_inter2),
      'gen_inter3':'{:,.2f}'.format(gen_inter3), 
      'min_subdown_vat': min_subdown_vat, 
      'exit_cost_down_vat':'{:,.0f}'.format(exit_cost_down_vat), 
      'text_acc_card':text_acc_card,  
      'text_acc_card_1':text_acc_card_1,  
      'text_acc_card_2':text_acc_card_2,  
      'text_acc_card_3':text_acc_card_3,  
      'text_acc_card_4':text_acc_card_4,  
      'text_acc_card_5':text_acc_card_5,  
      'text_acc_card_6':text_acc_card_6,  
      'text_acc_card_7':text_acc_card_7,  
      'text_acc_card_8':text_acc_card_8,  
      'text_acc_card_9':text_acc_card_9,  
      'text_acc_1':text_acc_1,  
      'text_acc_2':text_acc_2,  
      'text_acc_3':text_acc_3,  
      'text_acc_4':text_acc_4,  
      'text_acc_5':text_acc_5,  
      'text_acc_6':text_acc_6,  
      'text_acc_7':text_acc_7,  
      'text_acc_8':text_acc_8,  
      'text_acc_9':text_acc_9,  
      'text_acc_10':text_acc_10,  
      'text_acc_11':text_acc_11,  
      'text_acc_12':text_acc_12,  
      'text_acc_13':text_acc_13,  
      'text_acc_14':text_acc_14,  
      'text_acc_15':text_acc_15, 
      #ข้อมูลการติดต่อ
      'customername':customername,
      'contactcustomer':contactcustomer,
      'firstname':firstname, 
      'sellphone':sellphone,
   }
   return render(request, 'quotation.html', dataquo)

###############ใบสรุปการขาย#######################
@login_required(login_url='/firstdata')
def sellsummaryHead(request):
    return render(request,'sellsummary.html')
