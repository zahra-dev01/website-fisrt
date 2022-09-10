from django import forms
from django.contrib.auth.models import User


# Create Register Form ---------------------------------------------
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password_1 = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50) #password again

    # Form Validation
    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری از قبل وجود دارد.')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email= email).exists():
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
            raise forms.ValidationError('پسوردها مطابقت ندارند.')
        elif len(password1) < 8:
            raise forms.ValidationError('پسورد شما کوتاه است.')
        elif not any(i.issupper for i in password1):
            raise forms.ValidationError('پسورد شما حداقل باید یک حروف بزرگ داشته باشد.')
        return password1