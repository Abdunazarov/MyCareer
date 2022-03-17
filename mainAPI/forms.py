from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email_address = forms.EmailField(max_length=150)
	phone = forms.CharField(max_length=50)
	message = forms.CharField(max_length=2000, widget=forms.Textarea)