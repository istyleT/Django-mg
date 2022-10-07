from django.shortcuts import render, redirect, reverse ;
from sellmg.models import Product ;
from sellmg.models import Regiscost ;
from sellmg.models import Accmg ;
from django.db.models import Q ;

# Create your views here.
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
                    submodel = request.GET.get('submodel') #รับข้อมูลจาก form ที่ลูกค้ากรอก
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
                    #ปัญหาการ query data หลายเงื่อนไข
                    
                    if paytype == 'cash' :              
                                        return render(request, 'managecash.html',{'submodel':submodel ,'registype':registype, 'regiscost':regiscost, 'bodycolor':bodycolor, 'mgbranch':mgbranch, 'mainacc':mainacc})
                    elif paytype == 'finance' :
                                        regiscost = Regiscost.objects.filter(regis_code = submodel)
                                        return render(request, 'managefinance.html',{'submodel':submodel, 'registype':registype, 'regiscost':regiscost, 'bodycolor':bodycolor, 'mgbranch':mgbranch, 'mainacc':mainacc})

 
#นำ css / java static มาใช้งาน
def static_css (request):
    return render(request, 'static-css.html')

def static_js (request):
    return render(request, 'static-js.html')