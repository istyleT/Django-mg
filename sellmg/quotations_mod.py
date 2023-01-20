import math
from sellmg.models import Accmgs
from django.db.models import Q ;
#กำหนดตัวเเปรค่าคงที่
min_pdi = int(500)
min_polish = int(500)
min_frame = int(130)
red_frame = int(3000)
#ราคารถสุทธิ
netproductprice_m = lambda productprice,min_reduce,add_eq : int((productprice-min_reduce+add_eq))
#คำนวนยอดจัดไฟเเนนซ์
costfinance_m = lambda netproductprice,cost_down_fi : int(netproductprice-cost_down_fi)
#ส่วนเพิ่มส่วนลด 
totaladdmargin_m = lambda com_fi,add_eq,add_kickback : int(com_fi+add_eq+add_kickback)
#รวมค่ารายการอุปกรณ์ตกเเต่งกรอกเอง
minacc_typing_m = lambda min_acc_typing : sum(min_acc_typing)
#รวมค่าอุปกรณ์ตกเเต่งทั้งหมด
minacc_m = lambda min_acc_typing,minacc_code_price : int(min_acc_typing+minacc_code_price)
#ดอกเบี้ยต่อปี
interyear_m = lambda costfinance,min_inter : int(costfinance*(min_inter/100))
#ดอกเบี้ยทั้งหมด
totalinter_m = lambda interyear,gen_month: int((interyear*(gen_month/12)))
#ค่า com finance
total_com_finance_m = lambda interyear,com_fi_percent,com_fi_month : math.ceil((interyear*(com_fi_percent/100)*(com_fi_month/12))/1.07)
#เงินที่ต้องผ่อนไฟเเนนซ์ทั้งหมด
debt_fi_m = lambda costfinance,totalinter : int(costfinance + totalinter)
#ซับดอกเบี้ย
subsidy_inter_m = lambda cost_finance,gen_month,gen_inter,min_inter : float(((cost_finance * (gen_month/12) * ((gen_inter/100)-(min_inter/100)))/1.07)*1.03)
#การ subsidy ทั้งหมด
sumsubsidy_m = lambda subsidy_inter,min_prosub : int(subsidy_inter + min_prosub)
#ค่างวด
monthpayment_m  = lambda debt_fi,gen_month : math.ceil(debt_fi/gen_month)
#ค่าใช้จ่ายทั้งหมด
net_total_payment_m = lambda debt_fi_m,exit_cost_down : int(debt_fi_m+exit_cost_down)
#ส่วนลดสุทธิ
total_margin_m = lambda productmargin,total_addmargin,total_minmargin : int(productmargin+total_addmargin- total_minmargin)
#ส่วนลดส่วนลด
total_minmargin_m = lambda min_reduce,min_subdown,sumsubsidy,total_gift : int(min_reduce+min_subdown+sumsubsidy+total_gift)
#รายได้ที่ปรึกษาการขาย
income_sell_m = lambda total_margin,release_fee : int(total_margin+release_fee)
#เงินดาวน์ return 3 ค่า ค่าไฟเเนนซ์ /ลูกค้าจ่าย /ค่าvatsubdown
def costdown_m(netproductprice,gen_down,min_subdown):
   cost_down_fi = int(netproductprice*(gen_down/100)) #ดาวน์ที่ไฟเเนซ์เข้าใจ
   # กรณ์ีไม่มี subdown => ไม่มี vat ซับดาวน์
   if  min_subdown == 0:
       exit_cost_down = cost_down_fi
       exit_cost_down_vat =  0
   elif min_subdown != 0:
       exit_cost_down = int(cost_down_fi-min_subdown)
       exit_cost_down_vat =  int(min_subdown*0.07)
   down_data = [cost_down_fi,exit_cost_down,exit_cost_down_vat]
   return down_data
#ของเเถม
def msa_gift_m(min_acc,min_subdown_vat,exit_cost_down_vat,min_regis,regiscost):
    #บังคับเเถม
    force_gift = min_pdi + min_frame + min_polish 
    #เลือกได้
    choose_gift = 0
    if min_subdown_vat == 'Y' :
       choose_gift += exit_cost_down_vat
    if min_regis == 'Y' :
       choose_gift += regiscost
    #รวมการการเเถม
    total_gift = min_acc + force_gift + choose_gift
    gift_data = [force_gift,choose_gift,total_gift]
    return gift_data
#ค่าใช้จ่ายวันออกรถ
def total_exit_m(exit_cost_down,condition_finance,month_payment,min_regis,regiscost,min_subdown_vat,exit_cost_down_vat,gen_prepay):
    total_exit = red_frame + exit_cost_down - gen_prepay
    if condition_finance == 'BEGIN' :
       total_exit += month_payment
    if min_regis == 'N' :
       total_exit += regiscost
    if min_subdown_vat == 'N':
       total_exit += exit_cost_down_vat
    return total_exit
#รายการอุปกรณ์ตกเเต่ง
def listacc_m(listacccode):
   acccodeprice = 0
   acccodename = []
   for n in listacccode :
      if n != 'N' :
         find_acc = Accmgs.objects.filter(Q(id = n)).values_list('acc_name','acc_price', named=True)
         for x in find_acc :
            acccodeprice += x.acc_price
            acccodename.append(x.acc_name)
      else :
         acccodename.append('-')
   dataacc = [acccodename, acccodeprice]
   return dataacc

