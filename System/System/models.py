from django.db import models

# Create your models here.

FACULTY = (("ENGINEERING","ENGINEERING"),("SCIENCE","SCIENCE"),
           )
GENDER = (("MALE","MALE"),("FEMALE","FEMALE"),)
LEVEL = (("100","100"),("200","200"),("300","300"),("400","400"),
         ("500","500"),("600","600"),("700","700"),)
class Info(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    faculty= models.CharField(max_length=200,blank=False,null=False,choices=FACULTY)
    department= models.CharField(max_length=200,blank=False,null=False)
    mat_no= models.CharField(max_length=200,blank=False,null=False)
    level =models.CharField(max_length=200,blank=False,null=False,choices=LEVEL,default=1)
    session = models.CharField(max_length=200,blank=False,null=False,default="2020/2023")
    date_of_birth= models.DateField(auto_now_add = False)
    gender= models.CharField(max_length=200,blank=False,null=False,choices=GENDER)
    image =   models.ImageField(upload_to="images/")
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_created",)
    def __str__(self) -> str:
        return f"user : {self.name}"