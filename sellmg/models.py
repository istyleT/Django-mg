from django.db import models
from django import forms

class Product(models.Model) :
      mainmodel = models.CharField(max_length=25)
      submodel = models.CharField(max_length=50)
      price = models.IntegerField()
      margin = models.IntegerField() 
                    
      def __str__(self) : #เเสดงข้อมูลที่ query มาได้
          return f'{self.mainmodel} | {self.submodel} | {self.price} |{self.margi}'    

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
            
#เก็บข้อมูลลูกค้าทั้งหมด
class MSAcustomer(models.Model):
      msabranch = models.CharField(max_length=20, default='-')
      teamsell = models.CharField(max_length=10, default='-')
      date = models.DateField(auto_now_add=True)
      firstname = models.CharField(max_length=30)
      mainmodel = models.CharField(max_length=25)
      customername = models.CharField(max_length=50) #เเก้ได้
      contactcustomer = models.CharField(max_length=50) #เเก้ได้
      chanelcustomer = models.CharField(max_length=30)  
      statuscustomer = models.CharField(max_length=30) #เเก้ได้
      remark = models.CharField(max_length=100, default='-') #เเก้ได้
      quotation = models.CharField(max_length=20, default='-')
      def __str__(self):
         return f'{self.msabranch} |{self.teamsell} |{self.date} | {self.firstname} | {self.mainmodel} | {self.customername} | {self.contactcustomer} | {self.chanelcustomer} | {self.statuscustomer}| {self.quotation}'
#ประวัติลูกค้าทั้งหมด
class Pathstatusmsa(models.Model):
      msabranch = models.CharField(max_length=20, default='-')
      id_msacustomer = models.CharField(max_length=4)
      date = models.DateField(auto_now_add=True)    
      statuscustomer = models.CharField(max_length=30)
      remark = models.CharField(max_length=100, default='-')
      def __str__(self):
         return f'{self.msabranch} |{self.id_msacustomer} | {self.date} | {self.statuscustomer} | {self.remark}'
