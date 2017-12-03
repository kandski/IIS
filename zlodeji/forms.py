from .models import Zlodej as User
from .models import *
from django import forms
from django.contrib.admin import widgets


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(help_text="Prezívka a Použivateľské meno musia byť rovnaké!")
    prezivka = forms.CharField(help_text="Prezívka a Použivateľské meno musia byť rovnaké!")

    class Meta:
        model = User
        fields = ['username', 'email', 'prezivka', 'meno', 'password', 'odmena',
                  'rc', 'fotka', 'zivy']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-lg'

    def clean(self):
        username = self.cleaned_data.get('username')
        prezivka = self.cleaned_data.get('prezivka')

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            pass

        if prezivka != username:
            self.add_error('username', u"Prezívka a Použivateľské meno musia byť rovnaké!")
            self.add_error('prezivka', u"Prezívka a Použivateľské meno musia byť rovnaké!")

            if username == User.objects.get(username=username).username:
                self.add_error('username', u"Uživateľ " + username + " už existuje!")


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


class EvidujeForm(forms.ModelForm):
    class Meta:
        model = Eviduje
        fields = '__all__'
        widgets = {
        }
