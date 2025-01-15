# 作成するフォームのインポート
# signUp用のフォーム：CustomUser
# logIn用のフォーム：AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# 入力フォームを変更する為の設定をするインポート
# チェックボックス：CheckboxSelectMultiple
# emailでログイン：EmailInput
from django.forms.widgets import CheckboxSelectMultiple, EmailInput
# バリデーション用のライブラリをインポート
from django.forms import ValidationError
from django.views.generic.edit import CreateView
from django import forms 
from .models import Category
from guide.models import Case
from django.utils import timezone

#########################################################
# 1/14 小山
###事例登録のフォームを定義
class CaseRegistrationForm(forms.ModelForm):

   class Meta:
        model = Case
        fields = ['case_number', 'number', 'title', 'category', 'main', 'post_date']  # モデルのフィールドを指定

    # 必要に応じてフィールドのウィジェットやラベルを設定できます
   case_number = forms.CharField(max_length=30, label='事例番号')
   number = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'type':'text'}),label="社員番号" )
   title = forms.CharField(max_length=30, label='タイトル')
   category = forms.ModelChoiceField(queryset=Category.objects.all(), label='カテゴリ', empty_label="カテゴリを選択")
   main = forms.CharField(widget=forms.Textarea, label='本文')
   post_date = forms.DateField(initial=timezone.now, widget=forms.DateInput(attrs={'type': 'date'}), label="投稿日")

   def __init__(self, *args, **kwargs):
        # 現在のログインユーザーを取得
        user = kwargs.get('user')  # ビューから渡されるユーザー情報

        super().__init__(*args, **kwargs)

        # ユーザーが存在する場合、社員番号を自動で入力
        if user:
            self.fields['number'].initial = user.profile.employee_number  # ユーザーの社員番号を設定