from django.shortcuts import render, redirect, reverse ;
from sellmg.models import Product ;
from sellmg.models import Regiscosts ;
from sellmg.models import Accmgs ;
from sellmg.models import Colorsubmodels ;
from django.db.models import Q ;


# Create your views here.

#นำ css / java static มาใช้งาน
def static_css (request):
    return render(request, 'static-css.html')

def static_js (request):
    return render(request, 'static-js.html')


def firstpage(request):
    return render(request, 'index.html')


def collectdata(request): 

    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    username =request.POST.get('username')
    telphone = request.POST.get('telphone')
    mainmodel = request.POST.get('mainmodel')

    #ส่งข้อมูลออก
    request.session['username '] = username 
    request.session['telphone'] = telphone
    request.session['mainmodel'] = mainmodel
    
    #เงื่อนไขการ render หน้าต่อไป
    if mainmodel == "MG5" :
                        return render(request, 'Model_A.html',{'username':username})
    elif mainmodel == "MGVSHEV" :
                        return render(request, 'Model_B.html',{'username':username})
    elif mainmodel == "MGZS" :
                        return render(request, 'Model_C.html',{'username':username})
    elif mainmodel == "MGETD" :
                        return render(request, 'Model_D.html',{'username':username})
    elif mainmodel == "MGHSPHEV" :
                        return render(request, 'Model_E.html',{'username':username})
    elif mainmodel == "MGHS" :
                        return render(request, 'Model_F.html',{'username':username})
    else :
                        return redirect(firstpage) ;  

   
def showprice(request): 

    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน    
    submodel = request.POST.get('submodel') 

    #ส่งข้อมูลออก
    request.session['submodel'] = submodel
    productdata = Product.objects.filter( submodel = submodel).values_list('price','margin', named=True)
    productcolor = Colorsubmodels.objects.filter(submodel = submodel).values_list('submodel','color', named=True)
    for i in productdata :
            productprice =  int(i.price)
            productmargin = int(i.margin)               
    request.session['productprice'] = productprice     
    request.session['productmargin'] = productmargin     
    
    return render(request, 'showprice.html',{"productprice": '{:,}'.format(productprice), "productmargin": '{:,}'.format(productmargin), "submodel": submodel, "productcolor": productcolor})


#อยู่หน้า showprice Page3
def PaymentRegis(request):
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    submodel = request.session.get('submodel')
    mainmodel = request.session.get('mainmodel')

    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    paytype = request.POST.get('paytype')
    bodycolor = request.POST.get('bodycolor')
    mgbranch = request.POST.get('mgbranch')
    registype = request.POST.get('registype')

    #ส่งข้อมูลออก
    request.session['paytype'] = paytype
    request.session['bodycolor'] = bodycolor
    request.session['mgbranch'] = mgbranch
    regiscost = Regiscosts.objects.filter(regis_code = submodel).values_list('regis_personal','regis_company', named=True)
    for i in regiscost :
        if registype == 'person' :
           regiscost = int(i.regis_personal)
        elif registype == 'company' :
           regiscost = int(i.regis_company)
    request.session['regiscost'] = regiscost
    # query หา acc ตามเงื่อนไข (หาวิธีเก็บข้อมูลเป็นก้อน)
    mainacc = Accmgs.objects.filter(Q(acc_model = mainmodel) | Q(acc_model = 'ALL')).values_list('acc_code', 'acc_name','acc_price','acc_type', named=True)




    return render(request, 'branchadd.html',{'regiscost':'{:,}'.format(regiscost),'mainacc':mainacc})




def branceadd (request):
    
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    regiscost = int(request.session.get('regiscost'))
    productprice = int(request.session.get('productprice'))
    productmargin  = int(request.session.get('productmargin'))
    
    #กำหนดค่าคงที่
    red_frame = int(3000)

    #เก็บข้อมูลหน้าตัวเอง
    gen_down = int(request.POST.get('gen_down') or 0)
    gen_month= int(request.POST.get('gen_month'))
    gen_inter= float(request.POST.get('gen_inter')or 0)
    add_eq = int(request.POST.get('add_eq')or 0) 
    add_kickback = int(request.POST.get('add_kickback')or 0)
    com_fi_percent = int(request.POST.get('com_fi_percent'))
    com_fi_month = int(request.POST.get('com_fi_month'))
    com_as_percent = int(request.POST.get('com_as_percent'))
    com_as_month = int(request.POST.get('com_as_month'))
    min_prosub = int(request.POST.get('min_prosub')or 0)
    min_reduce = int(request.POST.get('min_reduce')or 0)
    condition_finance = str(request.POST.get('condition_finance'))
    min_regis = str(request.POST.get('min_regis','N'))
    if min_regis == 'N':
       min_regis = 0
    else: 
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
    min_inter = int(request.POST.get('min_inter')or 0)
    min_acc1 = int(request.POST.get('min_acc1'))
    min_acc2 = int(request.POST.get('min_acc2'))
    min_acc3 = int(request.POST.get('min_acc3'))
    min_acc4 = int(request.POST.get('min_acc4'))
    min_acc5 = int(request.POST.get('min_acc5'))
    min_acc6 = int(request.POST.get('min_acc6'))
    min_acc7 = int(request.POST.get('min_acc7'))
    min_acc8 = int(request.POST.get('min_acc8'))
    min_acc9 = int(request.POST.get('min_acc9'))
    min_acc10 = int(request.POST.get('min_acc10'))
    min_acc = min_acc1+min_acc2+min_acc3+min_acc4+min_acc5+min_acc6+min_acc7+min_acc8+min_acc9+min_acc10 

    #ทดสอบ
  

    #ส่งข้อมูลออก
    request.session['gen_down'] = gen_down
    request.session['gen_month'] = gen_month
    request.session['gen_inter'] = gen_inter
    request.session['add_eq'] = add_eq
    request.session['add_kickback'] = add_kickback
    request.session['com_fi_percent'] = com_fi_percent
    request.session['com_fi_monthl'] = com_fi_month
    request.session['com_as_percent'] = com_as_percent
    request.session['com_as_month'] = com_as_month
    request.session['min_prosub'] = min_prosub
    request.session['min_reduce'] = min_reduce
    request.session['min_regis'] = min_regis
    request.session['min_pdi'] = min_pdi
    request.session['min_frame'] = min_frame
    request.session['min_polish'] = min_polish
    request.session['min_subdown'] = min_subdown
    request.session['min_inter'] = min_inter
    request.session['min_acc'] = min_acc

    #------------คำนวณค่า--------------
    
    #เงินดาวน์
    cost_down = int(productprice*(gen_down/100))
    #เงินดาวน๋วันออกรถ 
    exit_cost_down = int(cost_down-(0.93*min_subdown))
    #ยอดจัด
    cost_finance = int((productprice+add_eq-min_reduce)-cost_down)
    #ดอกเบี้ยทั้งหมด
    total_inter = int(((cost_finance*(gen_inter/100))*(gen_month/12))-min_inter)
    #ค่างวด
    month_payment = int((total_inter+cost_finance)/gen_month)
    #ค่าใช้จ่ายทั้งหมดที่ให้กับ finance
    total_payment = int(month_payment*gen_month)
    #ค่าใช้จ่ายทั้งหมดที่ลูกค้าต้องจ่าย
    net_total_payment = total_payment + exit_cost_down
    #com-finance
    total_com_finance = int((cost_finance*(gen_inter/100)*(com_fi_percent/100)*com_fi_month)/1.07)
    #com-ansure
    total_com_ansure = 0
    #ส่วนเพิ่มส่วนลด
    total_addmargin = int(add_eq + add_kickback + total_com_finance + total_com_ansure)
    #ส่วนลดส่วนลด
    total_minmargin = int(min_prosub + min_reduce + min_regis + min_pdi + min_frame + min_polish + min_subdown + min_inter+ min_acc)
    #ส่วนลดสุทธิ
    total_margin = int(productmargin + total_addmargin - total_minmargin)
    #รวมรายการบังคับ
    fix_cost = int(min_regis + min_pdi + min_frame + min_polish)
    #ค่าใช้จ่ายวันออกรถ
    if min_regis == 0 and condition_finance == 'BEGIN' :
        total_exit = int(exit_cost_down + red_frame + regiscost + month_payment)
    elif min_regis == 0 and condition_finance != 'BEGIN' :
        total_exit = int(exit_cost_down + red_frame + regiscost)
    elif min_regis != 0 and condition_finance == 'BEGIN' :
        total_exit = int(exit_cost_down + red_frame + month_payment)
    else:
        total_exit = int(exit_cost_down + red_frame)

    #รวบรวมข้อมูลเพื่อส่ง
    data = {'regiscost':'{:,}'.format(regiscost),
            'add_eq':'{:,}'.format(add_eq),
            'add_kickback':'{:,}'.format(add_kickback),
            'min_prosub':'{:,}'.format(min_prosub),
            'min_reduce':'{:,}'.format(min_reduce),
            'fix_cost':'{:,}'.format(fix_cost),
            'min_subdown':'{:,}'.format(min_subdown),
            'min_inter':'{:,}'.format(min_inter),
            'productmargin':'{:,}'.format(productmargin),
            'exit_cost_down':'{:,}'.format(exit_cost_down),
            'red_frame':'{:,}'.format(red_frame),
            'total_exit':'{:,}'.format(total_exit),
            'net_total_payment':'{:,}'.format(net_total_payment),
            'min_regis':'{:,}'.format(min_regis),
            'gen_down':gen_down,
            'gen_month':gen_month,
            'gen_inter':gen_inter,
            'min_acc':'{:,}'.format(min_acc),
            'condition_finance':condition_finance,
            'cost_down':'{:,}'.format(cost_down),
            'cost_finance':'{:,}'.format(cost_finance),
            'total_inter' :'{:,}'.format(total_inter),
            'month_payment':'{:,}'.format(month_payment),
            'total_payment':'{:,}'.format(total_payment),
            'total_com_finance':'{:,}'.format(total_com_finance),
            'total_com_ansure':total_com_ansure,
            'total_addmargin':'{:,}'.format(total_addmargin),
            'total_minmargin':'{:,}'.format(total_minmargin),
            'total_margin':'{:,}'.format(total_margin)
    }
  
    return render(request, 'branchmin.html', data)


    































































#-----------------------------------------ส่วนเเยกโปรเเกรม---------------------------------------------------

# เลือกบริษัทไฟเเนนซ์
def Normalcalculate (request):
   
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    mainmodel = request.session.get('mainmodel')
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    financecompany = request.POST.get('financecompany')
    request.session['financecompany'] = financecompany #ส่งข้อมูลออก

    if financecompany == 'TISCO' :
        #ส่งข้อมูลเงินดาวน์
        condition_inter = Tisconormal.objects.filter(Q(fi_model = mainmodel)).values_list('fi_down', named=True)
        #ส่งข้อมูลจำนวนงวด
        fi_monthqty = Tisconormal.objects.exclude(fi_monthqty = None).values_list('fi_monthqty', named=True)
        return render(request, 'test.html', {'condition_inter': condition_inter, 'financecompany':financecompany, 'fi_monthqty':fi_monthqty})
    #elif financecompany == 'CITY' :
    #    condition_inter = Tisconormal.objects.filter(Q(fi_model = mainmodel)).values_list('fi_down', named=True)

    else :
        pass


def conditionfinance (request):
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    productprice = int(request.session.get('productprice'))
    mainmodel = request.session.get('mainmodel')
    financecompany = request.session.get('financecompany')
    #เก็บตัวเเปรจากหน้าตัวเอง
    downpay = int(request.POST.get('downpay'))
    monthqty= int(request.POST.get('monthqty'))
    # คำนวนค่าดาว์น
    downcost = int(productprice*(downpay/100))
    if financecompany == 'TISCO' :
        inter = Tisconormal.objects.filter(Q(fi_model = mainmodel) & Q(fi_down = downpay)).values_list('fi_down', 'fi_in_48','fi_in_60', 'fi_in_72', 'fi_in_84',named=True)
        for i in inter :
           if monthqty == 48 :
              rate_inter = i.fi_in_48
           elif monthqty == 60 :
               rate_inter = i.fi_in_60
           elif monthqty == 72 :
               rate_inter = i.fi_in_72
           elif monthqty == 84 :
               rate_inter = i.fi_in_84
        rate_inter = rate_inter/100
        financecost = int(productprice-downcost)
        car_payment = int(((((financecost)*rate_inter)*(monthqty/12))+(financecost))/monthqty)
        return render(request,'begincarpay.html', {'downcost':'{:,}'.format(downcost), 'car_payment':'{:,}'.format(car_payment), 'monthqty': monthqty})
    else:
        pass


def cashusemargin (request):
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    productmargin = int(request.session.get('productmargin'))
   
    #เก็บตัวเเปรจากหน้าตัวเอง (รายการอุปกรณ์ตกเเต่งยังไม่เก็บ)
    reduceproductprice = int(request.POST.get('reduceproductprice'))
    regiscost = int(request.POST.get('regiscost'))
    pdicost = int(request.POST.get('pdicost'))
    frame = int(request.POST.get('frame'))
    polishing = int(request.POST.get('polishing'))
    
    #รวมการใช้ส่วนลด
    total_reduce = reduceproductprice+regiscost+pdicost+frame+polishing
   
    #ส่วนลดคงเหลือ 
    final_margin = productmargin-total_reduce 

    
    return render(request,'showcashfinalmargin.html', {'productmargin':'{:,}'.format(productmargin), 'total_reduce':'{:,}'.format(total_reduce), 'final_margin':'{:,}'.format(final_margin), 'final_margin':final_margin})
     
    