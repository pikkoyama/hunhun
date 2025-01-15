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

#########################################################
# 1/14 小山
###事例登録のフォームを定義
class CaseRegistrationForm(forms.form):
    '''CaseRegistrationForm のサブクラス
    '''
    class Meta:
        '''CaseRegistrationForm のインナークラス
        Attributes:
            model:連携するUserモデル
            fileds:フォームで使用するフィールド
        '''
        # 連携するモデルを設定
        model = Case
        # フォームで使用するフィールドを設定（画面設計を参照）
        # 社員番号 タイトル カテゴリー 本文 
        fields = ("number", "title", "category", "main")
        
                # エラーメッセージを指定
        error_messages = {
            "title": {
                # emailが未入力の時のエラーメッセージ
                "required": "このフィールドを入力してください",
                
            }
        }