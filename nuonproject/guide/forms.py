# 作成するフォームのインポート
# signUp用のフォーム：CustomUser
# logIn用のフォーム：AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# main/models.py のCustomUserモデルをインポート
from guide.models import Case
# 入力フォームを変更する為の設定をするインポート
# チェックボックス：CheckboxSelectMultiple
# emailでログイン：EmailInput
from django.forms.widgets import CheckboxSelectMultiple, EmailInput
# バリデーション用のライブラリをインポート
from django.forms import ValidationError
from django.views.generic.edit import CreateView
from django import forms 
from .models import Category

#########################################################
# 1/14 小山
###事例登録のフォームを定義
class CaseRegistrationForm(forms.Form):
   category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # Categoryモデルから全てのカテゴリを取得
        empty_label="カテゴリを選択",      # 最初に空の選択肢を表示（オプション）
        required=True                    # 必須項目にする（オプション）
    )