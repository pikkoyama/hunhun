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
from guide.models import Case, CustomUser, Tour
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
   number = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label="社員番号", empty_label="社員番号を選択")
   title = forms.CharField(max_length=30, label='タイトル')
   category = forms.ModelChoiceField(queryset=Category.objects.all(), label='カテゴリ', empty_label="カテゴリを選択")
   main = forms.CharField(widget=forms.Textarea, label='本文')
   post_date = forms.DateField(initial=timezone.now, widget=forms.DateInput(attrs={'type': 'date'}), label="投稿日")

   def __init__(self, *args, **kwargs):
        # 'user' を kwargs から取得
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # ログインユーザーが存在する場合、そのユーザーを初期値として設定
        if user:
            self.fields['number'].initial = user  # ユーザーのインスタンスを初期値として設定
# ツアー登録用フォーム
class TourRegistrationForm(forms.ModelForm):
# koyama 
    class Meta:
        model = Tour
        fields = ['tour_number','tour_name', 'number','location','tour_date']  # モデルのフィールドを指定
        
    tour_number = forms.CharField(max_length=8, label='ツアー番号')
    tour_name = forms.CharField(max_length=30, label='ツアー名')
    number = forms.CharField(max_length=8,label="社員番号")
    location = forms.CharField(max_length=30, label='場所')
    tour_date = forms.DateTimeField(initial=timezone.now, widget=forms.DateInput(attrs={'type': 'date'}), label="ツアー日")


    def __init__(self, *args, **kwargs):
            # 'user' を kwargs から取得
            user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)
            self.fields['number'].widget.attrs['readonly'] = True  # 社員番号は読み取り専用
            # ログインユーザーが存在する場合、そのユーザーを初期値として設定
            if user:
                self.fields['number'].initial = user.number  # ユーザーのインスタンスを初期値として設定

    def clean_number(self):
        """社員番号から対応するCustomUserインスタンスを取得"""
        number = self.cleaned_data.get('number')
        print(f"{number}")
        
        try:
            return CustomUser.objects.get(number=number)  # 社員番号からインスタンスを取得
        except CustomUser.DoesNotExist:
            raise ValidationError("指定された社員番号のユーザーが存在しません。")
                
#################################
class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', max_length=100,required=True)

      