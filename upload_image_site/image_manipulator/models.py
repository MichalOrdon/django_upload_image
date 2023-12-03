from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='assets/images/')  # Przykładowa ścieżka dla obrazków
    # Dodaj inne pola, jeśli są potrzebne
