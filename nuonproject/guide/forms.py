# 作成するフォームのインポート
# signUp用のフォーム：CustomUser
# logIn用のフォーム：AuthenticationForm
import re
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
from guide.models import Case, CustomUser, Tour,Comment
from django.utils import timezone

#########################################################
# 1/14 小山
###事例登録のフォームを定義
import string
import random
from django import forms
from django.core.exceptions import ValidationError
from .models import Case, CustomUser, Category
from django.utils import timezone

class CaseRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Case
        fields = ['case_number', 'number', 'title', 'category', 'main', 'post_date']  # モデルのフィールドを指定
    
    # 必要に応じてフィールドのウィジェットやラベルを設定
    case_number = forms.CharField(max_length=8, label='事例番号')  # 8桁に制限
    number = forms.CharField(max_length=8, label="社員番号")
    title = forms.CharField(max_length=30, label='タイトル')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='カテゴリ', empty_label="カテゴリを選択")
    main = forms.CharField(widget=forms.Textarea, label='本文')
    post_date = forms.DateField(initial=timezone.now, widget=forms.DateInput(attrs={'type': 'date'}), label="投稿日")

    def __init__(self, *args, **kwargs):
        # 'user' を kwargs から取得
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # ランダムな8桁の数字を生成して事例番号として設定
        case_number = ''.join(random.choices('0123456789', k=8))  # 数字のみで8桁
        self.fields['case_number'].initial = case_number  # 事例番号の初期値として設定
        self.fields['case_number'].widget.attrs['readonly'] = True  # 事例番号をreadonlyに設定

        # 社員番号の初期値をユーザーの番号に設定
        self.fields['number'].widget.attrs['readonly'] = True  # 社員番号をreadonlyに設定
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
        
    def clean_tour_number(self):
        data = self.cleaned_data['tour_number']
        # 正規表現で8桁の数字のみ許可
        if not re.fullmatch(r'\d{8}', data):
            raise ValidationError('ツアー番号は8桁の数字で入力してください。')
        return data
# ツアー登録用フォーム
class TourRegistrationForm(forms.ModelForm):
# koyama 
    class Meta:
        model = Tour
        fields = ['tour_number','tour_name', 'number','location','tour_date']  # モデルのフィールドを指定
        
    tour_number = forms.CharField(max_length=8, label='ツアー番号')
    tour_name = forms.CharField(max_length=30, label='ツアー名')
    number = forms.CharField(max_length=8,label="社員番号")
    location = forms.CharField(max_length=4, label='場所')
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
        
    def clean_tour_number(self):
        data = self.cleaned_data['tour_number']
        # 正規表現で8桁の数字のみ許可
        if not re.fullmatch(r'\d{8}', data):
            raise ValidationError('ツアー番号は8桁の数字で入力してください。')
        return data
#################################
class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', max_length=100,required=True)

class CommentForm(forms.ModelForm):
    # フィールド定義
    case_number = forms.ModelChoiceField(
        queryset=Case.objects.all(),
        widget=forms.HiddenInput,  # 非表示フィールド
        required=True  # 必須に変更
    )
    number = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="社員番号",
        empty_label="社員番号を選択",
        widget=forms.HiddenInput  # 非表示にして変更不可にする
    )
    comment = forms.CharField(
        widget=forms.Textarea,
        label='コメント'
    )

    class Meta:
        model = Comment
        fields = ['case_number', 'number', 'comment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # ビューから渡されるユーザー情報
        super().__init__(*args, **kwargs)
        if user:
            self.fields['number'].initial = user  # 初期値にログインユーザーを設定
        self.fields['number'].widget.attrs['readonly'] = True  # 社員番号は読み取り専用にする

    def clean_number(self):
        """numberフィールドのバリデーションを修正"""
        number = self.cleaned_data.get('number')

        # デバッグログ
        print(f"Raw number input: {number}")

        # `iwawa(53167804)` のような場合に `53167804` だけ取得
        match = re.search(r'\d+', str(number))  # 数字部分のみ抽出
        if match:
            number = match.group()

        print(f"Extracted number: {number}")

        if not number:
            raise ValidationError("社員番号が空です。")

        try:
            return CustomUser.objects.get(number=number)  # 数値のみで検索
        except CustomUser.DoesNotExist:
            raise ValidationError(f"指定された社員番号のユーザーが存在しません。（入力: {number}）")
    def clean_number(self):
        """numberフィールドのバリデーションを修正"""
        # ユーザーが何か入力した場合でも、ログインユーザーの社員番号を使用する
        return self.fields['number'].initial  # 自動的にログインユーザーの社員番号を使う
    
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'category', 'main']  # 編集できるフィールドを指定

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['tour_number', 'tour_name','tour_date',"location"]  # 編集できるフィールドを指定


from django import forms
from .models import Information_pin

class InformationPinForm(forms.ModelForm):
    class Meta:
        model = Information_pin
        fields = ['place', 'explanation', 'image']
