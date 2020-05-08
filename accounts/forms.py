from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='اسم العائلة')
    email = forms.EmailField(label='البريد الاليكتروني')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الاليكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'subtitle', 'bio', 'address', 'address_detail', 'number_phone',
                   'working_hours', 'waiting_time', 'specialist_doctor', 'price',
                  'facebook', 'twitter', 'google', 'image')