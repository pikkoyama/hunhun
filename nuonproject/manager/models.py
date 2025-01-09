# from django.db import models

# # 1/8 岩本 --------------------------------------------
# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# class CustomUser(AbstractUser):
#      number = models.CharField(verbose_name="社員番号", max_length=8, primary_key= True)
#      name = models.CharField(verbose_name="氏名", max_length=20)
#      email = models.EmailField(verbose_name="メールアドレス",)
#      password = models.CharField(verbose_name="パスワード", max_length=256)
#      admin = models.BooleanField(verbose_name="管理者",default= False)

# USERNAME_FIELD = 'number' #標準のユーザー名を「number」にする
# REQUIRED_FIELDS = ['email','name']

# class Sort(models.Model):
#      sort_name = models.CharField(max_length=20)

# class Case(models.Model):
#      case_number = models.CharField(verbose_name= "事例番号",max_length=20,primary_key=True)
#      number = models.ForeignKey(CustomUser,verbose_name= "社員番号",on_delete=models.CASCADE)
#      title = models.CharField(verbose_name="タイトル", max_length=30)
#      category = models.IntegerField(verbose_name="カテゴリ",max_length=1)
#      main = models.CharField(verbose_name="本文",max_length=300)
#      post_date = models.DateTimeField(verbose_name="投稿日",max_length=20)
#      authonrization = models.BooleanField(verbose_name="認可済",max_length=20,default=False)

# class Category(models.Model):
#      category_name = models.CharField(verbose_name="カテゴリ名",max_length=50)