from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    imgFile = forms.ImageField(label='Elige una imagen')
