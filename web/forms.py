from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	mensaje = forms.CharField(
		required=True,
		widget=forms.Textarea)