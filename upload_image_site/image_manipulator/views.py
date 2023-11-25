from django.shortcuts import render
from django.conf import settings
import os


def home(request):
    folder = 'assets/images/'
    folder_path = os.path.join(settings.BASE_DIR, folder)

    if os.path.exists(folder_path):
        list_of_files = os.listdir(folder_path)
        images = [file for file in list_of_files if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    else:
        images = []

    return render(request, 'image_manipulator/home.html', {'images': images})
