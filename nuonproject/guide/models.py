from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.utils import timezone

# 1/8小山---------------------------
# 1/21小山--------------------------

# カスタムユーザー用
# 社員番号の採番乱数関数
def random_num():
    return str(random.randint(10000001,100000000)) # (1*10^7+1, 1*10^8)　# 10000001~99999999

# カスタムユーザーモデル
class CustomUser(AbstractUser):
    number = models.CharField(max_length=8,verbose_name="社員番号",primary_key=True,default=random_num )# 乱数関数
    username = models.CharField(verbose_name="氏名", max_length=20)
    # passwordは標準の機能を利用
    password = models.CharField(verbose_name="パスワード", max_length=256)
    email = models.EmailField(verbose_name="メールアドレス", unique=True)
    admin = models.BooleanField(verbose_name="管理者", default=False)

    # メールアドレスでログインする
    USERNAME_FIELD = 'number' # 標準のユーザー名を「number」と同じする
    REQUIRED_FIELDS = ['username', 'email']
    
    # CustomUserが参照されたときに返す値を設定
    class Meta:
        verbose_name_plural = "カスタムユーザー"
    def __str__(self):
        return f"{self.username}({self.number})"
       

# 種類モデル
class Sort(models.Model):
    sort_name = models.CharField(verbose_name="種類名", max_length=10)
   
    class Meta:
        verbose_name_plural = "種類"
    def __str__(self):
        return self.sort_name
    
# ガイドピンモデル
class GuidePin(models.Model):
    number = models.ForeignKey(CustomUser,verbose_name="社員番号", on_delete=models.CASCADE)
    sort = models.ForeignKey(Sort,verbose_name="種類", on_delete=models.CASCADE)
    longitude = models.DecimalField(verbose_name="経度", max_digits=9, decimal_places=6, default=0.00)
    latitude = models.DecimalField(verbose_name="緯度", max_digits=9, decimal_places=6, default=0.00)

    # ガイドピンモデルの参照設定
    class Meta:
        verbose_name_plural = "ガイドピン"
    def __str__(self):
        # return f"{self.name}({self.cd})"
        return f"{self.number}"
        

# ツアーモデル
class Tour(models.Model):
    tour_number = models.CharField(max_length=8, verbose_name="ツアー番号", primary_key=True, default="00000000")
    number = models.ForeignKey(CustomUser,verbose_name="社員番号",on_delete=models.CASCADE)						
    tour_name = models.CharField(verbose_name="ツアー名", max_length=50)
    location = models.CharField(verbose_name="場所", max_length=4)
    tour_date = models.DateTimeField(verbose_name="ツアー日")
    # information_pin_number = models.IntegerField(verbose_name="案内ピン番号")
    
    # ツアーモデルが呼ばれたときの設定
    class Meta:
        verbose_name_plural = "ツアー"
    def __str__(self) -> str:
        return f"{self.tour_name[:10]}({self.tour_date})"

# 案内ピンモデル
class Information_pin(models.Model):
    information_pin_id = models.IntegerField(verbose_name="案内ピン番号",default=0, primary_key=True)
    tour_number = models.ForeignKey(Tour, related_name='information_pin',verbose_name="ツアー番号", on_delete=models.CASCADE)
    tour_name = models.CharField(verbose_name="ツアー名",max_length=30)
    explanation = models.CharField(verbose_name="説明",max_length=700)
    address = models.CharField(verbose_name="住所", max_length=50)
    pref = models.CharField(verbose_name="都道府県", max_length=30, default="unknown")


    # モデルが参照されたときの設定
    class Meta:
        verbose_name_plural = "説明"
    def __str__(self) -> str:
        return f"{self.place[:10]}:{self.explanation[:10]}"
        
# カテゴリモデル
class Category(models.Model):
    category_name = models.CharField(verbose_name="カテゴリ名", max_length=20)

    class Meta:
        verbose_name_plural = 'カテゴリ名'
    def __str__(self):
        return f"{self.category_name}"

# 事例モデル
class Case(models.Model):
     case_number = models.CharField(verbose_name= "事例番号",max_length=20,primary_key=True)
     number = models.ForeignKey(CustomUser,verbose_name= "社員番号",on_delete=models.CASCADE)
     title = models.CharField(verbose_name="タイトル", max_length=30)
     category = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.CASCADE)
     main = models.CharField(verbose_name="本文",max_length=300)
     post_date = models.DateField(verbose_name="投稿日",default=timezone.now)
     authonrization = models.BooleanField(verbose_name="認可済",max_length=20,default=False)

     class Meta:
        verbose_name_plural = '事例'
     def __str__(self):
        return f"{self.case_number}({self.number}) - {self.title}"

# コメントモデル
class Comment(models.Model):
    case_number = models.ForeignKey(Case, verbose_name="事例番号", on_delete=models.CASCADE)
    number = models.ForeignKey(CustomUser, verbose_name="社員番号", on_delete=models.DO_NOTHING)
    comment = models.CharField(verbose_name="コメント", max_length=500)

    class Meta:
        verbose_name_plural="コメント"

    def __str__(self):
        return f"{self.comment[:10]}"
    