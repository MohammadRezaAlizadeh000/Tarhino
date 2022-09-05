from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms
                                .TextInput(attrs={'placeholder': 'نام کاربری', 'class': 'form-group mt-5'}),
                                error_messages={'invalid': '', })

    email = forms.EmailField(required=True, label="", widget=forms
                             .TextInput(attrs={'placeholder': 'ایمیل', 'class': 'form-group mt-5'}),
                             error_messages={'invalid': 'لطفا ایمیل را به درستی وارد کنید', })
    error_messages = {
        'password_mismatch': "پسوردهای وارد شده مطابقت ندارند",
    }

    # password = forms.CharField(widget=forms
    # .PasswordInput(attrs={'placeholder': 'رمز عبور', 'class': 'form-group mt-5'}), label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['password1'].widget.attrs.update({'placeholder': 'رمز عبور', 'class': 'form-group mt-5'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'تکرار رمز عبور', 'class': 'form-group mt-5'})

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password1'].error_list = None
        self.fields['password2'].error_list = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class LoginForm(forms.Form):
    user_name = forms.EmailField(label="", widget=forms
                                 .TextInput(attrs={'placeholder': 'ایمیل', 'class': 'form-group mt-5'}))
    password = forms.CharField(widget=forms
                               .PasswordInput(attrs={'placeholder': 'رمز عبور', 'class': 'form-group mt-5'}), label="")
