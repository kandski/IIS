from .models import Zlodej as User
from .models import *
from django import forms
from django.contrib.admin import widgets

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email', 'prezivka','meno', 'password', 'odmena',
                  'rc', 'fotka', 'zivy']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-lg'

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class VlastnilForm(forms.ModelForm):
    od = forms.DateField(widget=widgets.AdminDateWidget)
    do = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = Vlastnil
        fields = ['prezivka', 'id_vybavenia', 'od', 'do']
