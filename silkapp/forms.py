from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=150)
    desc = forms.TextInput()
    price = forms.DecimalField()
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    ptype = forms.CharField(max_length=300)