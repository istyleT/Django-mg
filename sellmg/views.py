from django.shortcuts import render, redirect ;
from django.contrib.auth import authenticate, login, logout;
from sellmg.models import Product ;
from sellmg.models import Regiscosts ;
from sellmg.models import Accmgs ;
from sellmg.models import Colorsubmodels ;
from django.db.models import Q ;
from django.contrib.auth.decorators import login_required ;
import math

#########################นำ css / java static มาใช้งาน ##########################
def static_css (request):
    return render(request, 'static-css.html')

def static_js (request):
    return render(request, 'static-js.html')
#################################################################################

################ฟังก์ขันลงชื่อเช้า-ออก#############################
def loginform(request):
    return render(request, 'login.html')

# ฟังก์ชัน logout 
def log_user_out(request):
    # Log user out
    logout(request)
    return redirect(loginform)
#############################################################

##################### ฟังก์ชันฝั่งadmin #####################
@login_required(login_url='/firstdata')
def pageaddcolor(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       return render(request,'addcolor.html')
    else :
       return render(request,'login.html')

@login_required(login_url='/firstdata')   
def pageaddregiscost(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       return render(request,'addregiscost.html')
    else:
       return render(request,'login.html')

@login_required(login_url='/firstdata')       
def pageaddproduct(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       return render(request,'addproduct.html')
    else:
       return render(request,'login.html')

@login_required(login_url='/firstdata')      
def pageaddacc(request):
    username = request.session.get('username')
    if username == 'istyletoon':
       return render(request,'addacc.html')
    else:
       return render(request,'login.html')
       
def addcolor(request):
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    submodel_add = request.POST.get('submodel') 
    color_add = request.POST.get('color') 
    # เชื่อมต่อ database
    Colorsubmodels.objects.create(submodel=submodel_add, color=color_add)
    return render(request, 'addcolor.html')

def addregiscost(request):
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    regis_code_add = request.POST.get('regis_code') 
    regis_personal_add = request.POST.get('regis_personal') 
    regis_company_add = request.POST.get('regis_company') 
    # เชื่อมต่อ database
    Regiscosts.objects.create(regis_code= regis_code_add, regis_personal=regis_personal_add, regis_company=regis_company_add)
    return render(request, 'addregiscost.html')

def addproduct(request):
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    mainmodel_add = request.POST.get('mainmodel') 
    submodel_add = request.POST.get('submodel') 
    price_add = request.POST.get('price') 
    margin_add = request.POST.get('margin') 
    # เชื่อมต่อ database
    Product.objects.create(mainmodel= mainmodel_add, submodel=submodel_add, price=price_add, margin=margin_add)
    return render(request, 'addproduct.html')

def addacc(request):
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    acc_code_add = request.POST.get('acc_code') 
    acc_name_add = request.POST.get('acc_name') 
    acc_price_add = request.POST.get('acc_price') 
    acc_type_add = request.POST.get('acc_type') 
    acc_model_add = request.POST.get('acc_model') 
    # เชื่อมต่อ database
    Accmgs.objects.create(acc_code= acc_code_add, acc_name=acc_name_add, acc_price=acc_price_add, acc_type=acc_type_add, acc_model=acc_model_add)
    return render(request, 'addacc.html')

###############################################################



##########################ฟังก์ชั่นฝั่ง user ################################
def collectdata(request): 
    # เก็บข้อมูลการ login จาก user 
    username = str(request.POST.get('username'))
    password = str(request.POST.get('password'))
    
    #ส่งข้อมูลออก
    request.session['username'] = username
    # เอาข้อมูลที่เก็บได้ไปเช็ค
    user = authenticate(request, username=username, password=password)
    # ถ้ามี เข้า condition render หน้าต่อไป 
    if user is not None:
        # Log a user in
         login(request, user)
         return render(request,'index.html')
    # ถ้าไม่มี สั่ง render หน้าเดิม
    else:
        return render(request,'login.html')

@login_required(login_url='/firstdata') 
def findsubmodel(request):
    mainmodel = str(request.POST.get('mainmodel'))
    request.session['mainmodel'] = mainmodel
    if mainmodel == "MG5":
       return render(request ,'Model_A.html')
    elif mainmodel == "MGVSHEV" :
        return render(request ,'Model_B.html')
    elif mainmodel == "MGZS" :
        return render(request ,'Model_C.html')
    elif mainmodel == "MGETD" :
        return render(request ,'Model_D.html')
    elif mainmodel == "MGHSPHEV" :
        return render(request ,'Model_E.html')
    elif mainmodel == "MGHS" :
        return render(request ,'Model_F.html')

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
        mainacc = Accmgs.objects.filter(Q(acc_model = 'MGZS') | Q(acc_model = 'ALL')).values_list('id', 'acc_code', 'acc_name','acc_price','acc_type', named=True)
        if paytype == 'cash':
             return render(request, 'branchcash.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,})
    
        elif paytype == 'finance' :
            return render(request, 'branchadd.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,'productprice':productprice,'mainmodel': mainmodel})
    elif mainmodel == 'MGHSPHEV' :
        mainacc = Accmgs.objects.filter(Q(acc_model = 'MGHS') | Q(acc_model = 'ALL')).values_list('id', 'acc_code', 'acc_name','acc_price','acc_type', named=True)
        if paytype == 'cash':
             return render(request, 'branchcash.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,})
    
        elif paytype == 'finance' :
            return render(request, 'branchadd.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,'productprice':productprice,'mainmodel': mainmodel})

    else :
        mainacc = Accmgs.objects.filter(Q(acc_model = mainmodel) | Q(acc_model = 'ALL')).values_list('id', 'acc_code', 'acc_name','acc_price','acc_type', named=True)

        if paytype == 'cash':
             return render(request, 'branchcash.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,})
    
        elif paytype == 'finance' :
            return render(request, 'branchadd.html',{'submodel': submodel,'regiscost':'{:,}'.format(regiscost),'text_productprice':'{:,}'.format(text_productprice),'mainacc':mainacc,'productprice':productprice,'mainmodel': mainmodel})

@login_required(login_url='/firstdata') 
def branceadd (request):
    
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    regiscost = int(request.session.get('regiscost'))
    productprice = int(request.session.get('productprice'))
    #productmargin  = int(request.session.get('productmargin'))
    

    #กำหนดค่าคงที่
    red_frame = int(3000) #ค่าป้ายเเดง

    #เก็บข้อมูลหน้าตัวเอง
    productmargin = int(request.POST.get('productmargin')or 0)
    gen_company = str(request.POST.get('gen_company'))
    gen_down = int(request.POST.get('gen_down') or 0)
    gen_month= int(request.POST.get('gen_month'))
    gen_inter= float(request.POST.get('gen_inter')or 0)
    gen_prepay= int(request.POST.get('gen_prepay')or 0)
    add_eq = int(request.POST.get('add_eq')or 0) 
    add_kickback = int(request.POST.get('add_kickback')or 0)
    com_fi_percent = int(request.POST.get('com_fi_percent'))
    com_fi_month = int(request.POST.get('com_fi_month'))
    #min_prosub = int(request.POST.get('min_prosub')or 0)
    min_prosub = 0
    min_reduce = int(request.POST.get('min_reduce')or 0)
    condition_finance = str(request.POST.get('condition_finance'))
    min_regis = str(request.POST.get('min_regis','N'))
    if min_regis == 'N': #ไม่เเถมค่าจดทะเบียน  minregis = 0
       min_regis = 0
    else:  # เเถมค่าจดทะเบียน minregis = regiscost
       min_regis = regiscost
    min_pdi = str(request.POST.get('min_pdi','N'))
    if min_pdi == 'N':
       min_pdi = 0
    else: 
       min_pdi = 500
    min_frame = str(request.POST.get('min_frame','N'))
    if min_frame == 'N':
       min_frame = 0
    else: 
       min_frame = 130
    min_polish = str(request.POST.get('min_polish','N'))
    if min_polish == 'N':
       min_polish = 0
    else: 
       min_polish = 500
    min_subdown = int(request.POST.get('min_subdown')or 0)
    min_subdown_vat = str(request.POST.get('min_subdown_vat','N'))
    if min_subdown_vat == 'N':
        statusvatdown = "0" #ไม่เเถม
    else:
        statusvatdown = "1" #เเถม
    
    min_inter = 0
    #min_inter = int(request.POST.get('min_inter')or 0)
    gen_remark = str(request.POST.get('gen_remark')or "-")

    # เก็บค่าอุปกรณ์ตกเเต่ง
    text_acc_card = str(request.POST.get('text_acc_card')or "-")
    min_acc_card = int(request.POST.get('min_acc_card')or 0)

    min_acc_1_code = str(request.POST.get('min_acc_1_code'))
    if min_acc_1_code == 'N':
        min_acc_1 = 0
        text_acc_1 = '-'
    else:
        find_acc_1 = Accmgs.objects.filter(Q(id = min_acc_1_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_1 :
            min_acc_1 = int(i.acc_price)
            text_acc_1 = str(i.acc_name)
    min_acc_2_code =str(request.POST.get('min_acc_2_code'))
    if min_acc_2_code == 'N':
        min_acc_2 = 0
        text_acc_2 = '-'
    else:
        find_acc_2 = Accmgs.objects.filter(Q(id = min_acc_2_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_2 :
            min_acc_2 = int(i.acc_price)
            text_acc_2 = str(i.acc_name)
    min_acc_3_code = str(request.POST.get('min_acc_3_code'))
    if min_acc_3_code == 'N':
        min_acc_3 = 0
        text_acc_3 = '-'
    else:
        find_acc_3 = Accmgs.objects.filter(Q(id = min_acc_3_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_3 :
            min_acc_3 = int(i.acc_price)
            text_acc_3 = str(i.acc_name)
    min_acc_4_code = str(request.POST.get('min_acc_4_code'))
    if min_acc_4_code == 'N':
        min_acc_4 = 0
        text_acc_4 = '-'
    else:
        find_acc_4 = Accmgs.objects.filter(Q(id = min_acc_4_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_4 :
            min_acc_4 = int(i.acc_price)
            text_acc_4 = str(i.acc_name)
    min_acc_5_code = str(request.POST.get('min_acc_5_code'))
    if min_acc_5_code == 'N':
        min_acc_5 = 0
        text_acc_5 = '-'
    else:
        find_acc_5 = Accmgs.objects.filter(Q(id = min_acc_5_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_5 :
            min_acc_5 = int(i.acc_price)
            text_acc_5 = str(i.acc_name)
    min_acc_6_code = str(request.POST.get('min_acc_6_code'))
    if min_acc_6_code == 'N':
        min_acc_6 = 0
        text_acc_6 = '-'
    else:
        find_acc_6 = Accmgs.objects.filter(Q(id = min_acc_6_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_6 :
            min_acc_6 = int(i.acc_price)
            text_acc_6 = str(i.acc_name)
    min_acc_7_code = str(request.POST.get('min_acc_7_code'))
    if min_acc_7_code == 'N':
        min_acc_7 = 0
        text_acc_7 = '-'
    else:
        find_acc_7 = Accmgs.objects.filter(Q(id = min_acc_7_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_7 :
            min_acc_7 = int(i.acc_price)
            text_acc_7 = str(i.acc_name)
    min_acc_8_code = str(request.POST.get('min_acc_8_code'))
    if min_acc_8_code == 'N':
        min_acc_8 = 0
        text_acc_8 = '-'
    else:
        find_acc_8 = Accmgs.objects.filter(Q(id = min_acc_8_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_8 :
            min_acc_8 = int(i.acc_price)
            text_acc_8 = str(i.acc_name)
    min_acc_9_code = str(request.POST.get('min_acc_9_code'))
    if min_acc_9_code == 'N':
        min_acc_9 = 0
        text_acc_9 = '-'
    else:
        find_acc_9 = Accmgs.objects.filter(Q(id = min_acc_9_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_9 :
            min_acc_9 = int(i.acc_price)
            text_acc_9 = str(i.acc_name)
    min_acc_10_code = str(request.POST.get('min_acc_10_code'))
    if min_acc_10_code == 'N':
        min_acc_10 = 0
        text_acc_10 = '-'
    else:
        find_acc_10 = Accmgs.objects.filter(Q(id = min_acc_10_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_10 :
            min_acc_10 = int(i.acc_price)
            text_acc_10 = str(i.acc_name)
    min_acc_11_code = str(request.POST.get('min_acc_11_code'))
    if min_acc_11_code == 'N':
        min_acc_11 = 0
        text_acc_11 = '-'
    else:
        find_acc_11 = Accmgs.objects.filter(Q(id = min_acc_11_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_11 :
            min_acc_11 = int(i.acc_price)
            text_acc_11 = str(i.acc_name)
    min_acc_12_code = str(request.POST.get('min_acc_12_code'))
    if min_acc_12_code == 'N':
        min_acc_12 = 0
        text_acc_12 = '-'
    else:
        find_acc_12 = Accmgs.objects.filter(Q(id = min_acc_12_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_12 :
            min_acc_12 = int(i.acc_price)
            text_acc_12 = str(i.acc_name)
    min_acc_13_code = str(request.POST.get('min_acc_13_code'))
    if min_acc_13_code == 'N':
        min_acc_13 = 0
        text_acc_13 = '-'
    else:
        find_acc_13 = Accmgs.objects.filter(Q(id = min_acc_13_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_13 :
            min_acc_13 = int(i.acc_price)
            text_acc_13 = str(i.acc_name)
    min_acc_14_code = str(request.POST.get('min_acc_14_code'))
    if min_acc_14_code == 'N':
        min_acc_14 = 0
        text_acc_14 = '-'
    else:
        find_acc_14 = Accmgs.objects.filter(Q(id = min_acc_14_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_14 :
            min_acc_14 = int(i.acc_price)
            text_acc_14 = str(i.acc_name)
    min_acc_15_code = str(request.POST.get('min_acc_15_code'))
    if min_acc_15_code == 'N':
        min_acc_15 = 0
        text_acc_15 = '-'
    else:
        find_acc_15 = Accmgs.objects.filter(Q(id = min_acc_15_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_15 :
            min_acc_15 = int(i.acc_price)
            text_acc_15 = str(i.acc_name)
    min_acc_16_code = str(request.POST.get('min_acc_16_code'))
    if min_acc_16_code == 'N':
        min_acc_16 = 0
        text_acc_16 = '-'
    else:
        find_acc_16 = Accmgs.objects.filter(Q(id = min_acc_16_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_16 :
            min_acc_16 = int(i.acc_price)
            text_acc_16 = str(i.acc_name)
    min_acc_17_code = str(request.POST.get('min_acc_17_code'))
    if min_acc_17_code == 'N':
        min_acc_17 = 0
        text_acc_17 = '-'
    else:
        find_acc_17 = Accmgs.objects.filter(Q(id = min_acc_17_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_17 :
            min_acc_17 = int(i.acc_price)
            text_acc_17 = str(i.acc_name)
    min_acc_18_code = str(request.POST.get('min_acc_18_code'))
    if min_acc_18_code == 'N':
        min_acc_18 = 0
        text_acc_18 = '-'
    else:
        find_acc_18 = Accmgs.objects.filter(Q(id = min_acc_18_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_18 :
            min_acc_18 = int(i.acc_price)
            text_acc_18 = str(i.acc_name)
    min_acc_19_code = str(request.POST.get('min_acc_19_code'))
    if min_acc_19_code == 'N':
        min_acc_19 = 0
        text_acc_19 = '-'
    else:
        find_acc_19 = Accmgs.objects.filter(Q(id = min_acc_19_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_19 :
            min_acc_19 = int(i.acc_price)
            text_acc_19 = str(i.acc_name)
    min_acc_20_code = str(request.POST.get('min_acc_20_code'))
    if min_acc_20_code == 'N':
        min_acc_20 = 0
        text_acc_20 = '-'
    else:
        find_acc_20 = Accmgs.objects.filter(Q(id = min_acc_20_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_20 :
            min_acc_20 = int(i.acc_price)
            text_acc_20 = str(i.acc_name)

    min_acc = int(min_acc_card+min_acc_1+min_acc_2+min_acc_3+min_acc_4+min_acc_5+min_acc_6+min_acc_7
    +min_acc_8+min_acc_9+min_acc_10+min_acc_11+min_acc_12+min_acc_13+min_acc_14+min_acc_15
    +min_acc_16+min_acc_17+min_acc_18+min_acc_19+min_acc_20)
     
  
    #ส่งชื่ออุปกรณ์ตกเเต่ง
    request.session['text_acc_card'] = text_acc_card
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
    request.session['text_acc_16'] = text_acc_16
    request.session['text_acc_17'] = text_acc_17
    request.session['text_acc_18'] = text_acc_18
    request.session['text_acc_19'] = text_acc_19
    request.session['text_acc_20'] = text_acc_20
    


    #ส่งข้อมูลออก
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
    request.session['min_prosub'] = min_prosub
    request.session['min_reduce'] = min_reduce
    request.session['min_regis'] = min_regis
    request.session['min_pdi'] = min_pdi
    request.session['min_frame'] = min_frame
    request.session['min_polish'] = min_polish
    request.session['min_subdown'] = min_subdown
    request.session['min_inter'] = min_inter
    request.session['min_acc'] = min_acc
    request.session['gen_remark'] = gen_remark

    #------------คำนวณค่า--------------
    
    #เงินดาวน์เริ่มต้น
    cost_down = int((productprice-min_reduce+add_eq)*(gen_down/100)) #pass
    #เงินดาวน๋วันออกรถ 
    exit_cost_down = int(cost_down-min_subdown) #pass
    # vat subdown 
    exit_cost_down_vat = int(min_subdown*0.07) #pass
    #ยอดจัด
    cost_finance = int((productprice-min_reduce+add_eq)-cost_down) #pass
    
    #ดอกเบี้ยทั้งหมด
    total_inter = int(((cost_finance*(gen_inter/100))*(gen_month/12))-min_inter) #edit
    #ค่างวดปกติ
    month_payment = int(math.ceil((((cost_finance*(gen_inter/100)*(gen_month/12))-min_inter)+cost_finance)/gen_month)) #pass
    #com-finance
    total_com_finance = float(((cost_finance)*(gen_inter/100)*(com_fi_percent/100)*(com_fi_month/12))/1.07) #pass
    #ส่วนเพิ่มส่วนลด
    total_addmargin = float(add_eq + add_kickback + total_com_finance) #edit
    #รวมรายการของเเถมอุปกรณ์ตกเเต่ง
    total_gift = int(min_regis + min_pdi + min_frame + min_polish + min_acc) #pass
    #ส่วนลดส่วนลด

    if statusvatdown == "1" : #เเถม vatsubdown
         total_minmargin = float(min_prosub + min_reduce + min_regis + min_pdi + min_frame + min_polish + min_subdown + min_inter+ min_acc + exit_cost_down_vat)
    elif statusvatdown == "0": # ไม่เเถม
         total_minmargin = float(min_prosub + min_reduce + min_regis + min_pdi + min_frame + min_polish + min_subdown + min_inter+ min_acc)
    #ส่วนลดสุทธิ
    total_margin = float(productmargin + total_addmargin - total_minmargin) #pass
    

    #ค่าใช้จ่ายวันออกรถ
    if min_regis == 0 and condition_finance == 'BEGIN' :
        if statusvatdown == "1" :
           total_exit = int(exit_cost_down + red_frame + regiscost + month_payment - gen_prepay)
        elif statusvatdown == "0" :
            total_exit = int(exit_cost_down + red_frame + regiscost + month_payment - gen_prepay+exit_cost_down_vat )
    elif min_regis == 0 and condition_finance != 'BEGIN' :
        if statusvatdown == "1" :
            total_exit = int(exit_cost_down + red_frame + regiscost - gen_prepay)
        elif  statusvatdown == "0" : 
            total_exit = int(exit_cost_down + red_frame + regiscost - gen_prepay+exit_cost_down_vat)
    elif min_regis != 0 and condition_finance == 'BEGIN' :
        if statusvatdown == "1" :
            total_exit = int(exit_cost_down + red_frame + month_payment - gen_prepay)
        elif  statusvatdown == "0" : 
            total_exit = int(exit_cost_down + red_frame + month_payment - gen_prepay+exit_cost_down_vat)
    else:
        if statusvatdown == "1" :
             total_exit = int(exit_cost_down + red_frame - gen_prepay)
        elif  statusvatdown == "0" : 
             total_exit = int(exit_cost_down + red_frame - gen_prepay+exit_cost_down_vat)
    

      #ค่าใช้จ่ายทั้งหมดที่ลูกค้าต้องจ่าย
    net_total_payment = (month_payment*gen_month)+exit_cost_down

    #ส่งข้อมูลออก

   
    request.session['cost_down'] = cost_down
    request.session['exit_cost_down'] = exit_cost_down
    request.session['exit_cost_down_vat'] = exit_cost_down_vat
    request.session['cost_finance'] = cost_finance
    request.session['month_payment'] = month_payment
    request.session['statusvatdown'] = statusvatdown
    request.session['total_com_finance'] = total_com_finance
    request.session['total_addmargin'] = total_addmargin
    request.session['total_minmargin'] = total_minmargin
    request.session['total_margin'] = total_margin
    request.session['total_exit'] = total_exit
  


    data = {'regiscost':'{:,}'.format(regiscost), #ค่าจดทะเบียน
            'add_eq':'{:,}'.format(add_eq), #+บวกหัวอุปกรณ์
            'cost_down':'{:,}'.format(cost_down), 
            'cost_finance':'{:,}'.format(cost_finance), #ยอดจัดไฟเเนนซ์
            'productprice':'{:,}'.format(productprice), #ราคาขาย
            'gen_prepay':'{:,}'.format(gen_prepay), #เงินจอง
            'add_kickback':'{:,}'.format(add_kickback), #+ ค่า kickback
            'min_prosub':'{:,}'.format(min_prosub), #-ค่า โปร subsidy
            'min_reduce':'{:,}'.format(min_reduce), #-ลดราคาขาย
            'total_gift':'{:,}'.format(total_gift), #-รวมการของบังคับ
            'min_subdown':'{:,}'.format(min_subdown), # 
            'min_inter':'{:,}'.format(min_inter),
            'productmargin':'{:,}'.format(productmargin),
            'exit_cost_down':'{:,}'.format(exit_cost_down),
            'red_frame':'{:,}'.format(red_frame),
            'total_exit':'{:,}'.format(total_exit),
            'net_total_payment':'{:,}'.format(net_total_payment),
            'min_regis':'{:,}'.format(min_regis),
            'exit_cost_down_vat':'{:,}'.format(exit_cost_down_vat),
            'gen_down':gen_down,
            'gen_month':gen_month,
            'gen_inter':gen_inter,
            'statusvatdown':statusvatdown,
            'min_acc':'{:,}'.format(min_acc),
            'condition_finance':condition_finance,
            'cost_finance':'{:,}'.format(cost_finance),
            'total_inter' :'{:,}'.format(total_inter),
            'month_payment':'{:,.0f}'.format(month_payment),
            'total_com_finance':'{:,.2f}'.format(total_com_finance),
            'total_addmargin':'{:,.0f}'.format(total_addmargin),
            'total_minmargin':'{:,.0f}'.format(total_minmargin),
            'total_margin':'{:,.0f}'.format(total_margin),
    }
  
    return render(request, 'showdatafinance.html', data)

@login_required(login_url='/firstdata') 
def branchcash (request):
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    regiscost = int(request.session.get('regiscost'))
    productprice = int(request.session.get('productprice'))
    #productmargin  = int(request.session.get('productmargin'))
    
    #กำหนดค่าคงที่
    red_frame = int(3000) #ค่าป้ายเเดง

    #เก็บข้อมูลหน้าตัวเอง
    gen_remark = str(request.POST.get('gen_remark')or "-")
    productmargin = int(request.POST.get('productmargin')or 0)
    gen_prepay= int(request.POST.get('gen_prepay')or 0)
    min_reduce = int(request.POST.get('min_reduce')or 0)

    min_regis = str(request.POST.get('min_regis','N'))
    if min_regis == 'N': #ไม่เเถมค่าจดทะเบียน  minregis = 0
       min_regis = 0
    else:  # เเถมค่าจดทะเบียน minregis = regiscost
       min_regis = regiscost
    min_pdi = str(request.POST.get('min_pdi','N'))
    if min_pdi == 'N':
       min_pdi = 0
    else: 
       min_pdi = 500
    min_frame = str(request.POST.get('min_frame','N'))
    if min_frame == 'N':
       min_frame = 0
    else: 
       min_frame = 130
    min_polish = str(request.POST.get('min_polish','N'))
    if min_polish == 'N':
       min_polish = 0
    else: 
       min_polish = 500

        # เก็บค่าอุปกรณ์ตกเเต่ง
    text_acc_card = str(request.POST.get('text_acc_card')or "-")
    min_acc_card = int(request.POST.get('min_acc_card')or 0)

    min_acc_1_code = str(request.POST.get('min_acc_1_code'))
    if min_acc_1_code == 'N':
        min_acc_1 = 0
        text_acc_1 = '-'
    else:
        find_acc_1 = Accmgs.objects.filter(Q(id = min_acc_1_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_1 :
            min_acc_1 = int(i.acc_price)
            text_acc_1 = str(i.acc_name)
    min_acc_2_code =str(request.POST.get('min_acc_2_code'))
    if min_acc_2_code == 'N':
        min_acc_2 = 0
        text_acc_2 = '-'
    else:
        find_acc_2 = Accmgs.objects.filter(Q(id = min_acc_2_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_2 :
            min_acc_2 = int(i.acc_price)
            text_acc_2 = str(i.acc_name)
    min_acc_3_code = str(request.POST.get('min_acc_3_code'))
    if min_acc_3_code == 'N':
        min_acc_3 = 0
        text_acc_3 = '-'
    else:
        find_acc_3 = Accmgs.objects.filter(Q(id = min_acc_3_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_3 :
            min_acc_3 = int(i.acc_price)
            text_acc_3 = str(i.acc_name)
    min_acc_4_code = str(request.POST.get('min_acc_4_code'))
    if min_acc_4_code == 'N':
        min_acc_4 = 0
        text_acc_4 = '-'
    else:
        find_acc_4 = Accmgs.objects.filter(Q(id = min_acc_4_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_4 :
            min_acc_4 = int(i.acc_price)
            text_acc_4 = str(i.acc_name)
    min_acc_5_code = str(request.POST.get('min_acc_5_code'))
    if min_acc_5_code == 'N':
        min_acc_5 = 0
        text_acc_5 = '-'
    else:
        find_acc_5 = Accmgs.objects.filter(Q(id = min_acc_5_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_5 :
            min_acc_5 = int(i.acc_price)
            text_acc_5 = str(i.acc_name)
    min_acc_6_code = str(request.POST.get('min_acc_6_code'))
    if min_acc_6_code == 'N':
        min_acc_6 = 0
        text_acc_6 = '-'
    else:
        find_acc_6 = Accmgs.objects.filter(Q(id = min_acc_6_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_6 :
            min_acc_6 = int(i.acc_price)
            text_acc_6 = str(i.acc_name)
    min_acc_7_code = str(request.POST.get('min_acc_7_code'))
    if min_acc_7_code == 'N':
        min_acc_7 = 0
        text_acc_7 = '-'
    else:
        find_acc_7 = Accmgs.objects.filter(Q(id = min_acc_7_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_7 :
            min_acc_7 = int(i.acc_price)
            text_acc_7 = str(i.acc_name)
    min_acc_8_code = str(request.POST.get('min_acc_8_code'))
    if min_acc_8_code == 'N':
        min_acc_8 = 0
        text_acc_8 = '-'
    else:
        find_acc_8 = Accmgs.objects.filter(Q(id = min_acc_8_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_8 :
            min_acc_8 = int(i.acc_price)
            text_acc_8 = str(i.acc_name)
    min_acc_9_code = str(request.POST.get('min_acc_9_code'))
    if min_acc_9_code == 'N':
        min_acc_9 = 0
        text_acc_9 = '-'
    else:
        find_acc_9 = Accmgs.objects.filter(Q(id = min_acc_9_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_9 :
            min_acc_9 = int(i.acc_price)
            text_acc_9 = str(i.acc_name)
    min_acc_10_code = str(request.POST.get('min_acc_10_code'))
    if min_acc_10_code == 'N':
        min_acc_10 = 0
        text_acc_10 = '-'
    else:
        find_acc_10 = Accmgs.objects.filter(Q(id = min_acc_10_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_10 :
            min_acc_10 = int(i.acc_price)
            text_acc_10 = str(i.acc_name)
    min_acc_11_code = str(request.POST.get('min_acc_11_code'))
    if min_acc_11_code == 'N':
        min_acc_11 = 0
        text_acc_11 = '-'
    else:
        find_acc_11 = Accmgs.objects.filter(Q(id = min_acc_11_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_11 :
            min_acc_11 = int(i.acc_price)
            text_acc_11 = str(i.acc_name)
    min_acc_12_code = str(request.POST.get('min_acc_12_code'))
    if min_acc_12_code == 'N':
        min_acc_12 = 0
        text_acc_12 = '-'
    else:
        find_acc_12 = Accmgs.objects.filter(Q(id = min_acc_12_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_12 :
            min_acc_12 = int(i.acc_price)
            text_acc_12 = str(i.acc_name)
    min_acc_13_code = str(request.POST.get('min_acc_13_code'))
    if min_acc_13_code == 'N':
        min_acc_13 = 0
        text_acc_13 = '-'
    else:
        find_acc_13 = Accmgs.objects.filter(Q(id = min_acc_13_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_13 :
            min_acc_13 = int(i.acc_price)
            text_acc_13 = str(i.acc_name)
    min_acc_14_code = str(request.POST.get('min_acc_14_code'))
    if min_acc_14_code == 'N':
        min_acc_14 = 0
        text_acc_14 = '-'
    else:
        find_acc_14 = Accmgs.objects.filter(Q(id = min_acc_14_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_14 :
            min_acc_14 = int(i.acc_price)
            text_acc_14 = str(i.acc_name)
    min_acc_15_code = str(request.POST.get('min_acc_15_code'))
    if min_acc_15_code == 'N':
        min_acc_15 = 0
        text_acc_15 = '-'
    else:
        find_acc_15 = Accmgs.objects.filter(Q(id = min_acc_15_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_15 :
            min_acc_15 = int(i.acc_price)
            text_acc_15 = str(i.acc_name)
    min_acc_16_code = str(request.POST.get('min_acc_16_code'))
    if min_acc_16_code == 'N':
        min_acc_16 = 0
        text_acc_16 = '-'
    else:
        find_acc_16 = Accmgs.objects.filter(Q(id = min_acc_16_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_16 :
            min_acc_16 = int(i.acc_price)
            text_acc_16 = str(i.acc_name)
    min_acc_17_code = str(request.POST.get('min_acc_17_code'))
    if min_acc_17_code == 'N':
        min_acc_17 = 0
        text_acc_17 = '-'
    else:
        find_acc_17 = Accmgs.objects.filter(Q(id = min_acc_17_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_17 :
            min_acc_17 = int(i.acc_price)
            text_acc_17 = str(i.acc_name)
    min_acc_18_code = str(request.POST.get('min_acc_18_code'))
    if min_acc_18_code == 'N':
        min_acc_18 = 0
        text_acc_18 = '-'
    else:
        find_acc_18 = Accmgs.objects.filter(Q(id = min_acc_18_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_18 :
            min_acc_18 = int(i.acc_price)
            text_acc_18 = str(i.acc_name)
    min_acc_19_code = str(request.POST.get('min_acc_19_code'))
    if min_acc_19_code == 'N':
        min_acc_19 = 0
        text_acc_19 = '-'
    else:
        find_acc_19 = Accmgs.objects.filter(Q(id = min_acc_19_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_19 :
            min_acc_19 = int(i.acc_price)
            text_acc_19 = str(i.acc_name)
    min_acc_20_code = str(request.POST.get('min_acc_20_code'))
    if min_acc_20_code == 'N':
        min_acc_20 = 0
        text_acc_20 = '-'
    else:
        find_acc_20 = Accmgs.objects.filter(Q(id = min_acc_20_code)).values_list('acc_name','acc_price', named=True)
        for i in find_acc_20 :
            min_acc_20 = int(i.acc_price)
            text_acc_20 = str(i.acc_name)

    min_acc = int(min_acc_card+min_acc_1+min_acc_2+min_acc_3+min_acc_4+min_acc_5+min_acc_6+min_acc_7
    +min_acc_8+min_acc_9+min_acc_10+min_acc_11+min_acc_12+min_acc_13+min_acc_14+min_acc_15
    +min_acc_16+min_acc_17+min_acc_18+min_acc_19+min_acc_20)
   


   #ส่งชื่ออุปกรณ์ตกเเต่ง
    request.session['text_acc_card'] = text_acc_card
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
    request.session['text_acc_16'] = text_acc_16
    request.session['text_acc_17'] = text_acc_17
    request.session['text_acc_18'] = text_acc_18
    request.session['text_acc_19'] = text_acc_19
    request.session['text_acc_20'] = text_acc_20

   #------------คำนวณค่า--------------
     #รวมรายการของเเถมอุปกรณ์ตกเเต่ง
    total_gift = int(min_regis + min_pdi + min_frame + min_polish + min_acc) #pass
    #รวมการใช้ส่วนลด
    total_minmargin = min_reduce + total_gift 

    #ส่วนลดคงเหลือ
    total_margin = float(productmargin - total_minmargin) #pass
    #ราคารถสุทธิ
    net_productprice = productprice-min_reduce
    
    #ค่าใช้จ่ายวันออกรถ
    if min_regis == 0 :
        total_exit = int((productprice-min_reduce)+red_frame- gen_prepay+regiscost)
    else : 
        total_exit = int((productprice-min_reduce)+red_frame- gen_prepay)
    
    #ค่าใช้จ่ายทั้งหมด
    net_total_payment = productprice-total_minmargin


    # set ค่าเป็น 0 เพราะซื้อเงินสด
    add_eq = '-'
    cost_down = '-'
    cost_finance = '-'
    add_kickback = '-'
    min_prosub = '-'
    min_subdown = '-'
    min_inter = '-'
    exit_cost_down = '-'
    exit_cost_down_vat = '-'
    total_addmargin = '-'
    total_com_finance = '-'
    month_payment = '-'
    gen_down = '-'
    gen_month = '-'
    gen_inter = '-'
    condition_finance   = '-'
    total_inter = '-'
    statusvatdown = "1"

    #รวบรวมข้อมูลเพื่อส่ง
    data = {'regiscost':'{:,}'.format(regiscost), #ค่าจดทะเบียน
            'add_eq':add_eq, #+บวกหัวอุปกรณ์
            'cost_down':cost_down, 
            'cost_finance':cost_finance, #ยอดจัดไฟเเนนซ์
            'productprice':'{:,}'.format(productprice), #ราคาขาย
            'gen_prepay':'{:,}'.format(gen_prepay), #เงินจอง
            'add_kickback':add_kickback, #+ ค่า kickback
            'min_prosub':min_prosub, #-ค่า โปร subsidy
            'min_reduce':'{:,}'.format(min_reduce), #-ลดราคาขาย
            'total_gift':'{:,}'.format(total_gift), #-รวมการของบังคับ
            'min_subdown':min_subdown, # 
            'min_inter':min_inter,
            'productmargin':'{:,}'.format(productmargin),
            'exit_cost_down':exit_cost_down,
            'red_frame':'{:,}'.format(red_frame),
            'total_exit':'{:,}'.format(total_exit),
            'net_total_payment':'{:,}'.format(net_total_payment),
            'min_regis':'{:,}'.format(min_regis),
            'exit_cost_down_vat':exit_cost_down_vat,
            'gen_down':gen_down,
            'gen_month':gen_month,
            'gen_inter':gen_inter,
            'statusvatdown':statusvatdown,
            'min_acc':'{:,}'.format(min_acc),
            'condition_finance':condition_finance,
            'total_inter' :total_inter,
            'month_payment':month_payment,
            'total_com_finance':total_com_finance,
            'total_addmargin':total_addmargin,
            'total_minmargin':'{:,.0f}'.format(total_minmargin),
            'total_margin':'{:,.0f}'.format(total_margin),
    }
   
    return render(request, 'showdatafinance.html', data)

@login_required(login_url='/firstdata') 
def showdata(request):
   # เก็บข้อมูลหน้าตัวเอง
   sell_name= str(request.POST.get('sell_name')or '-')
   sell_phone= str(request.POST.get('sell_phone')or '-')
   customer_name= str(request.POST.get('customer_name')or '-')
   customer_phone= str(request.POST.get('customer_phone')or '-')
   
   from datetime import datetime
   now = datetime.today() #วันที่
   
   #ข้อมูลทั่วไป
   submodel = str(request.session.get('submodel'))
   bodycolor = str(request.session.get('bodycolor'))
   mgbranch = str(request.session.get('mgbranch'))
   registype = str(request.session.get('registype'))
   paytype = str(request.session.get('paytype'))
   #รายละเอียดการซื้อรถยนต์
   productprice = int(request.session.get('productprice'))
   add_eq = int(request.session.get('add_eq'))
   min_reduce = int(request.session.get('min_reduce'))
   net_produceprice = int(productprice + add_eq - min_reduce) #ราคารถสุทธิ
   gen_down = int(request.session.get('gen_down'))
   cost_down = int(request.session.get('cost_down'))
   min_subdown = int(request.session.get('min_subdown'))
   exit_cost_down = int(request.session.get('exit_cost_down'))
   cost_finance = int(request.session.get('cost_finance'))
   gen_month = int(request.session.get('gen_month'))
   add_kickback = int(request.session.get('add_kickback'))
   gen_inter = float(request.session.get('gen_inter'))
   min_prosub = int(request.session.get('min_prosub'))
   min_inter = int(request.session.get('min_inter'))
   month_payment = int(request.session.get('month_payment'))
   condition_finance = str(request.session.get('condition_finance'))
   gen_company = str(request.session.get('gen_company'))
   #รายละเอียดวันออกรถ
   red_frame = int(request.session.get('red_frame'))
   gen_prepay = int(request.session.get('gen_prepay'))
   total_exit = int(request.session.get('total_exit'))
   min_regis = int(request.session.get('min_regis'))
   regiscost = int(request.session.get('regiscost'))
   statusvatdown = str(request.session.get('statusvatdown')) # 1 = เเถม
   exit_cost_down_vat = int(request.session.get('exit_cost_down_vat'))
   #รายการของเเถมอุปกรณ์ตกเเต่ง 
   min_acc = int(request.session.get('min_acc'))
   min_pdi = int(request.session.get('min_pdi'))
   min_frame = int(request.session.get('min_frame'))
   min_polish = int(request.session.get('min_polish'))
   if statusvatdown == '1' : #เเถมจะส่งเลข 1
       total_gift = int(min_acc+min_pdi+min_frame+min_polish+min_regis+exit_cost_down_vat)
   else :
       total_gift = int(min_acc+min_pdi+min_frame+min_polish+min_regis)
      
   #ชื่ออุปกรณ์ตกเเต่ง
   text_acc_card = str(request.session.get('text_acc_card'))
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
   text_acc_16 = str(request.session.get('text_acc_16'))
   text_acc_17 = str(request.session.get('text_acc_17'))
   text_acc_18 = str(request.session.get('text_acc_18'))
   text_acc_19 = str(request.session.get('text_acc_19'))
   text_acc_20 = str(request.session.get('text_acc_20'))
   # หมายเหตุ
   gen_remark = str(request.session.get('gen_remark'))
   

   # รวมข้อมูลเพื่อส่งไปหน้าใบเสนอราคา
   details = {
      'now':now, #ข้อมูลทั่วไป
      'submodel':submodel,
      'gen_remark':gen_remark,
      'bodycolor':bodycolor,
      'mgbranch':mgbranch,
      'registype':registype,
      'paytype':paytype, 
      'gen_month':gen_month, 
      'gen_company':gen_company, 
      'condition_finance':condition_finance, 
      'min_regis':'{:,.0f}'.format(min_regis), 
      'regiscost':'{:,.0f}'.format(regiscost), 
      'productprice':'{:,.0f}'.format(productprice), 
      'min_prosub':'{:,.0f}'.format(min_prosub), 
      'exit_cost_down':'{:,.0f}'.format(exit_cost_down), 
      'cost_down':'{:,.0f}'.format(cost_down), 
      'red_frame':'{:,.0f}'.format(red_frame), 
      'total_exit':'{:,.0f}'.format(total_exit), 
      'net_produceprice':'{:,.0f}'.format(net_produceprice), 
      'gen_down':'{:,.0f}'.format(gen_down), 
      'add_eq':'{:,.0f}'.format(add_eq), 
      'gen_prepay':'{:,.0f}'.format(gen_prepay), 
      'min_subdown':'{:,.0f}'.format(min_subdown), 
      'min_reduce':'{:,.0f}'.format(min_reduce), 
      'add_kickback':'{:,.0f}'.format(add_kickback), 
      'cost_finance':'{:,}'.format(cost_finance), 
      'month_payment':'{:,}'.format(month_payment), 
      'min_inter':'{:,.0f}'.format(min_inter), 
      'gen_inter':'{:,.2f}'.format(gen_inter), 
      'statusvatdown':statusvatdown, 
      'exit_cost_down_vat':'{:,.0f}'.format(exit_cost_down_vat), 
      'min_acc':'{:,.0f}'.format(min_acc), 
      'min_pdi':min_pdi, 
      'min_frame':min_frame, 
      'min_polish':min_polish, 
      'total_gift':'{:,.0f}'.format(total_gift),
      'text_acc_card':text_acc_card,  
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
      'text_acc_16':text_acc_16,  
      'text_acc_17':text_acc_17,  
      'text_acc_18':text_acc_18,  
      'text_acc_19':text_acc_19,  
      'text_acc_20':text_acc_20,  
      'sell_name':sell_name,  
      'sell_phone':sell_phone,  
      'customer_name':customer_name,  
      'customer_phone':customer_phone,  
      
       

   }
   return render(request, 'quotation.html', details)

##############################################################################




























