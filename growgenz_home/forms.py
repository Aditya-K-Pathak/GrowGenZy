from django import forms

class userDetails(forms.Form):
    f_name = forms.CharField(max_length=20)
    l_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    firm_name = forms.CharField(max_length=40)
    