from django import forms
from .models import ImageModel  # Załóżmy, że masz model dla obrazków


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel  # Podmień na właściwy model
        fields = ['image']  # Lista pól, które chcesz w formularzu
