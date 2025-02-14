# 1/15 --------------------------------------
from django import forms
from django.core.exceptions import ValidationError
import re
from guide.admin import CustomUser

class AccountCreationForm(forms.ModelForm):
    # number = forms.CharField(
    #     label='社員番号',
    #     max_length=50,
    #     widget=forms.TextInput(attrs={'placeholder': '社員番号を入力してください'}),
    #     required=True
    # )
    # username = forms.CharField(
    #     label='氏名',
    #     max_length=100,
    #     widget=forms.TextInput(attrs={'placeholder': '氏名を入力してください'}),
    #     required=True
    # )
    # email = forms.EmailField(
    #     label='メールアドレス',
    #     widget=forms.EmailInput(attrs={'placeholder': 'メールアドレスを入力してください'}),
    #     required=True
    # )
    # password = forms.CharField(
    #     label='パスワード',
    #     widget=forms.PasswordInput(attrs={'placeholder': 'パスワードを入力してください'}),
    #     required=True
    # )
    
    
    class Meta:
        model = CustomUser
        fields = ('number', 'username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['number'].widget.attrs['readonly'] = True  # 社員番号は読み取り専用

    # パスワードバリデーション
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
        
        if not re.match(password_regex, password):
            raise ValidationError('パスワードは8文字以上で、英大文字、英小文字、数字を含む必要があります。')
        
        return password