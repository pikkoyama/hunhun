from django.contrib import admin
# import * とすることでmodels.pyで定義した全てのモデルをインポートする
from .models import *
from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
# 作成したモデルを管理者画面で確認できるように登録する
# admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(CustomUser)
admin.site.register(GuidePin)
admin.site.register(Sort)
admin.site.register(Tour)
admin.site.register(Information_pin)
admin.site.register(Case)
admin.site.register(Category)
admin.site.register(Comment)
