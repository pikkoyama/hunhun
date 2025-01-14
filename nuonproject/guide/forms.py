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

#########################################################
# 1/14 小山
###事例登録のフォームを定義
class CaseRegistrationForm():
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
        # email 氏名 郵便番号 住所 マイショップ パスワード パスワード（確認用）
        fields = ("email", "name", "zip_code", "address",
                   "myshops", "password1", "password2")
        
        # マイショップをチェックボックスで選択できるように設定する
        widgets = {
            "myshops":CheckboxSelectMultiple
        }
                # エラーメッセージを指定
        error_messages = {
            "email": {
                # emailが未入力の時のエラーメッセージ
                "required": "このフィールドを入力してください",
                # "unique":"入力されたemailと一致するemailが存在します" # <- 独自バリデーションの為無効化
            }
        }