# from django.db import models

# # 1/8  --------------------------------------------
# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# class CustomUser(AbstractUser):
#     number = models.CharField(verbose_name="社員番号", max_length=8, primary_key= True)
#     name = models.CharField(verbose_name="氏名", max_length=20)
#     email = models.EmailField(verbose_name="メールアドレス",)
#     password = models.CharField(verbose_name="パスワード", max_length=256)
#     admin = models.BooleanField(verbose_name="管理者",default= False)

#     class Meta:
#         verbose_name_plural = 'カスタムユーザー'
#     def __str__(self):
#         return f"{self.name}({self.number})"