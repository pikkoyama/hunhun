from django.contrib import admin
# import * とすることでmodels.pyで定義した全てのモデルをインポートする
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # 管理画面でのフィールドのセクション設定
    fieldsets = (
        (None, {'fields': ('number', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # 新規ユーザー追加時のフィールド設定
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('number', 'username', 'email', 'password1', 'password2'),
        }),
    )

    # 管理画面で表示するリスト
    list_display = ('number', 'username', 'email', 'is_staff')
    search_fields = ('number', 'username', 'email')
    ordering = ('number',)
    
# 作成したモデルを管理者画面で確認できるように登録する
admin.site.register(CustomUser,CustomUserAdmin)
# admin.site.register(CustomUser)
admin.site.register(GuidePin)
admin.site.register(Sort)
admin.site.register(Tour)
admin.site.register(Information_pin)
admin.site.register(Case)
admin.site.register(Category)
admin.site.register(Comment)
