from django import forms
class SigninForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(render_value=True))
    save = forms.BooleanField(required=True)   
