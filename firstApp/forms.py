from django import forms



class MyIntroForm(forms.Form):
<<<<<<< HEAD
    # firstName = forms.CharField(label = 'First Name', max_length = 100)    
    # lastName = forms.CharField(label= "Last Name", max_length = 100)
    firstName = forms.CharField(label = 'First Name', max_length = 100, widget = forms.TextInput(attrs={'class':"form-control"}))
    lastName = forms.CharField(label= "Last Name", max_length = 100, widget = forms.TextInput(attrs={'class':"form-control"}))
=======
    # firstName = forms.CharField(label = 'First Name', max_length = 100)
    # lastName = forms.CharField(label= "Last Name", max_length = 100)

    firstName = forms.CharField(label = 'First Name', max_length = 100, widget = forms.TextInput(attrs = {"class":"form-control"}))
    lastName = forms.CharField(label= "Last Name", max_length = 100, widget = forms.TextInput(attrs ={"class":"form-control"}))
>>>>>>> 1512b6608899141a3033e854dadf12581301d432
