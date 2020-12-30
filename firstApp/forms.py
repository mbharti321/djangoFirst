from django import forms



class MyIntroForm(forms.Form):
    firstName = forms.CharField(label = 'First Name', max_length = 100)
    lastName = forms.CharField(label= "Last Name", max_length = 100)