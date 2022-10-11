from django.db import models
from django import forms
# ตารางเพื่อตั้งค่า รุ่นหลัก รุ่นย่อย ราคา ส่วนลด ค่าจดทะเทียน
class Product(models.Model) :
                    mainmodel = models.CharField(max_length=25)
                    submodel = models.CharField(max_length=50)
                    price = models.IntegerField()
                    margin = models.IntegerField() 
 
                    def __str__(self) : #เเสดงข้อมูลที่ query มาได้
                          return f'{self.mainmodel} | {self.submodel} | {self.price} |{self.margin}'



class Regiscost(models.Model):
      regis_code = models.CharField(max_length=30)
      regis_personal = models.IntegerField()
      regis_company = models.IntegerField()

      def __str__(self) : 
                          return f'{self.regis_code} | {self.regis_personal} | {self.regis_company} '
      


class Accmg(models.Model) :
      acc_code = models.CharField(max_length=20)
      acc_name = models.CharField(max_length=100)
      acc_price = models.IntegerField()
      acc_type = models.CharField(max_length=10)
      acc_model = models.CharField(max_length=10)


# ตารางดอกเบีย
class Tisconormal(models.Model) :        
      fi_model = models.CharField(max_length=30)
      fi_down = models.FloatField()
      fi_in_48 = models.FloatField()
      fi_in_60 = models.FloatField()
      fi_in_72 = models.FloatField()
      fi_in_84 = models.FloatField()
      fi_monthqty = models.IntegerField()
      def __str__(self) :
              return f'{self.fi_model} | {self.fi_down} | {self.fi_in_48} | {self.fi_in_60} | {self.fi_in_72} | {self.fi_in_84} | {self.fi_monthqty}'        

