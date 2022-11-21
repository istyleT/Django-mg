from django.db import models
from django import forms
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=12)

# ตารางเพื่อตั้งค่า รุ่นหลัก รุ่นย่อย ราคา ส่วนลด ค่าจดทะเทียน
class Product(models.Model) :
                    mainmodel = models.CharField(max_length=25)
                    submodel = models.CharField(max_length=50)
                    price = models.IntegerField()
                    margin = models.IntegerField() 
 
                    def __str__(self) : #เเสดงข้อมูลที่ query มาได้
                          return f'{self.mainmodel} | {self.submodel} | {self.price} |{self.margin}'



class Regiscosts(models.Model):
      regis_code = models.CharField(max_length=30)
      regis_personal = models.IntegerField()
      regis_company = models.IntegerField()

      def __str__(self) : 
                          return f'{self.regis_code} | {self.regis_personal} | {self.regis_company} '
      


class Accmgs(models.Model) :
      acc_code = models.CharField(max_length=20)
      acc_name = models.CharField(max_length=100)
      acc_price = models.IntegerField()
      acc_type = models.CharField(max_length=10)
      acc_model = models.CharField(max_length=10)



class Colorsubmodels(models.Model):
      submodel = models.CharField(max_length=50)
      color = models.CharField(max_length=50)
      
      def __str__(self):
             return f'{self.submodel} | {self.color}'

#เก็บข้อมูลหน้า filepdf ที่ upload เข้ามา
class Quotations(models.Model):
      date = models.DateField(auto_now_add=True)
      username = models.CharField(max_length=20)
      mainmodel = models.CharField(
            max_length=15,
            choices=[('MG5','MG 5'),('MGVSHEV','MG VS HEV'),('MGZS','MG ZS'),('MGEDT','MG EXTENDER'),
            ('MGHSPHEV','MG HS PHEV'),('MGHS','MG HS')],
            default='MG5'
            )
      filepdf = models.FileField(upload_to='upload/')
      def __str__(self):
             return f'{self.date} | {self.username} | {self.mainmodel} | {self.filepdf}'

#form ที่เอาไว้เก็บข้อมูลจาก class quotation
class QuotationsForm (forms.ModelForm):
      class Meta :
            model = Quotations
            fields = '__all__'
            labels = {
                  'mainmodel': 'รุ่นรถ MG' ,
                  'filepdf': 'ไฟล์ PDF',
                  'username': 'ผู้เสนอราคา'}
            widgets = {'filepdf': forms.FileInput(attrs={'type':'file'}),
            'Model': forms.Select()}
            exclude = []
            