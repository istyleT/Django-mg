from django.shortcuts import render, redirect, reverse ;
from sellmg.models import Product ;
from sellmg.models import Regiscost ;
from sellmg.models import Accmg ;
from sellmg.models import Tisconormal ;
from django.db.models import Q ;


# Create your views here.

#นำ css / java static มาใช้งาน
def static_css (request):
    return render(request, 'static-css.html')

def static_js (request):
    return render(request, 'static-js.html')


def firstpage(request):
                    return render(request, 'index.html')


#อยู่หน้าเเรก Page1
def collectdata(request): #create variablr for collect data from url
                    # เเก้ปัญหาเรื่องความปลอดภัยของข้อมูล
                    if 'username' not in request.POST :
                        return render(request, 'index.html')
                    else :
                         username =request.POST.get('username')
                         telphone = request.POST.get('telphone')
                         mainmodel = request.POST.get('mainmodel')
                         #ส่งข้อมูลให้ view ในหน้าต่อไป
                         request.session['mainmodel'] = mainmodel
                         
                         if mainmodel == "MG5" :
                                             return render(request, 'Model_A.html',{'username':username,'telphone':telphone})
                         elif mainmodel == "MGVSHEV" :
                                             return render(request, 'Model_B.html',{'username':username,'telphone':telphone})
                         elif mainmodel == "MGZS" :
                                             return render(request, 'Model_C.html',{'username':username,'telphone':telphone})
                         elif mainmodel == "MGETD" :
                                             return render(request, 'Model_D.html',{'username':username,'telphone':telphone})
                         elif mainmodel == "MGHSPHEV" :
                                             return render(request, 'Model_E.html',{'username':username,'telphone':telphone})
                         elif mainmodel == "MGHS" :
                                             return render(request, 'Model_F.html',{'username':username,'telphone':telphone})
                         else :
                                             return redirect(firstpage) ;  

   
#อยู่หน้า model Page2
def showprice(request): #ลูกค้าเลือกรุ่นย่อย 
                    mainmodel = request.session.get('mainmodel')#รับข้อมูลหน้าที่เเล้ว
                    submodel = request.POST.get('submodel') #รับข้อมูลจาก form ที่ลูกค้ากรอก
                    # เอา submodel ไป filter ในตาราง product เก็บข้อมูลลงในตัวเเปร productdata
                    productdata = Product.objects.filter( submodel = submodel)
                    #ส่งข้อมูลให้ view ในหน้าต่อไป
                    request.session['mainmodel'] = mainmodel
                    request.session['submodel'] = submodel
                    for i in productdata :
                                        print (i.price)                  
                    request.session['productprice'] = i.price     
                    request.session['productmargin'] = i.margin     
                    
                    # render page ส่งข้อมูล
                    return render(request, 'showprice.html',{'pricedata':productdata})


#อยู่หน้า showprice Page3
def PaymentRegis(request):
                    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
                    productprice = request.session.get('productprice')
                    productmargin = request.session.get('productmargin')
                    mainmodel = request.session.get('mainmodel')
                    submodel = request.session.get('submodel') 
                    #ส่งข้อมูลให้ view ในหน้าต่อไป
                    request.session['productprice'] = productprice
                    request.session['productmargin'] = productmargin
                    request.session['mainmodel'] = mainmodel
                    request.session['submodel'] = submodel  
                    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
                    paytype = request.POST.get('paytype')
                    registype = request.POST.get('registype')
                    bodycolor = request.POST.get('bodycolor')
                    mgbranch = request.POST.get('mgbranch')
                    # query ข้อมูลจาก database
                    mainacc = Accmg.objects.filter(acc_model = mainmodel).values_list('acc_name','acc_price','acc_type', named=True)
                    regiscost = Regiscost.objects.filter(regis_code = submodel)
                    #สร้างตัวเเปรกำหนดค่า
                    x = 0
                    if paytype == 'cash' :              
                                        return render(request, 'managecash.html',{'submodel':submodel ,'registype':registype, 'regiscost':regiscost, 'bodycolor':bodycolor, 'mgbranch':mgbranch, 'mainacc':mainacc})
                    elif paytype == 'finance' :
                                        regiscost = Regiscost.objects.filter(regis_code = submodel)
                                        return render(request, 'managefinance.html',{'submodel':submodel, 'registype':registype, 'regiscost':regiscost, 'bodycolor':bodycolor, 'mgbranch':mgbranch, 'mainacc':mainacc})




# สร้างเงื่อนไขการคำนวน
def Normalcalculate (request):
   
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    #productprice = int(request.session.get('productprice'))
    #productmargin = int(request.session.get('productmargin'))
    mainmodel = request.session.get('mainmodel')
    #submodel = request.session.get('submodel') 


    #ส่งข้อมูลให้ view ในหน้าต่อไป
    #request.session['productprice'] = productprice
    #request.session['productmargin'] = productmargin
    #request.session['mainmodel'] = mainmodel
    #request.session['submodel'] = submodel  
    # สร้างตัวเเปรมาเก็บข้อมูลจากหน้าปัจจุบัน
    financecompany = request.POST.get('financecompany')
    request.session['financecompany'] = financecompany
    if financecompany == 'TISCO' :
        condition_inter = Tisconormal.objects.filter(Q(fi_model = mainmodel)).values_list('fi_down','fi_in_48','fi_in_60', named=True)
        return render(request, 'test.html', {'condition_inter': condition_inter, 'financecompany':financecompany})
        #condition_inter = Tisconormal.objects.filter(Q(fi_model = mainmodel) & Q(fi_down = downpay)).values_list('fi_down', 'fi_in_48','fi_in_60', 'fi_in_72', 'fi_in_84',named=True)
        #for i in condition_inter :
        #    if monthqty == 48 :
        #       rate_inter = i.fi_in_48
        #    elif monthqty == 60 :
        #        rate_inter = i.fi_in_60
        #    elif monthqty == 72 :
        #        rate_inter = i.fi_in_72
        #    elif monthqty == 84 :
        #        rate_inter = i.fi_in_84
        #    else :
        #        rate_inter = 0
        #         #ต้องฟ่อง errors
        #rate_inter = rate_inter/100
        #financecost = float(productprice-downcost)
        #car_payment = int(((((financecost)*rate_inter)*(monthqty/12))+(financecost))/monthqty)
        #return render(request,'begincarpay.html', {'downcost':downcost, 'car_payment':car_payment, 'monthqty': monthqty})
        
        
        
    else :
        pass
    #return render(request, 'Normalcalculate.html', {'condition_inter': condition_inter, 'financecompany':financecompany})

def conditionfinance (request):
    #สร้างตัวเเปรการเก็บของข้อมูลรุ่นจากข้อมูลที่ส่งมาก่อนหน้า ใช้ request.session
    productprice = int(request.session.get('productprice'))
    mainmodel = request.session.get('mainmodel')
    financecompany = request.session.get('financecompany')
    #เก็บตัวเเปรจากหน้าตัวเอง
    downpay = int(request.POST.get('downpay'))
    monthqty= int(request.POST.get('monthqty'))
    # คำนวนค่าดาว์น
    downcost = float(productprice*(downpay/100))
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
        financecost = float(productprice-downcost)
        car_payment = int(((((financecost)*rate_inter)*(monthqty/12))+(financecost))/monthqty)
        return render(request,'begincarpay.html', {'downcost':downcost, 'car_payment':car_payment, 'monthqty': monthqty})
    else:
        pass