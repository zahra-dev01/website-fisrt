from django import forms
from .models import *


# Create Register Form ---------------------------------------------
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام کاربری خود را وارد کنید'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد کنید'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام خود را وارد کنید'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی خود را وارد کنید'}))
    password_1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'پسورد خود را وارد کنید'}))
    password_2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'پسورد خود را تکرار کنید'}))

    # Form Validation
    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری از قبل وجود دارد.')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود دارد.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 2:
            raise forms.ValidationError('تعداد حروف کمتر از حد مجاز است.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 2:
            raise forms.ValidationError('تعداد حروف کمتر از حد مجاز است.')
        return last_name

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('تکرار رمزعبور مطابقت ندارند.')
        elif len(password1) < 4:
            raise forms.ValidationError('رمز عبور شما کوتاه است.')
        # elif not any(i.issupper for i in password1):
        #     raise forms.ValidationError('رمز عبور شما حداقل باید یک حروف بزرگ داشته باشد.')
        return password1


# Create login Form --------------------------------------------------------
class UserLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Mata:
        model = Profile
        fields = ['phone', 'address']




