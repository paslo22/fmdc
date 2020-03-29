from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	mensaje = forms.CharField(
		required=True,
		widget=forms.Textarea)


class AdminSongForm(forms.ModelForm):
	canciones = forms.FileField(widget=forms.FileInput(
		attrs={'multiple': True}), 
		required=False
	)

class ImagesRevistaForm(forms.ModelForm):
	imagenes = forms.FileField(widget=forms.FileInput(
		attrs={'multiple': True}), 
		required=True
	) 