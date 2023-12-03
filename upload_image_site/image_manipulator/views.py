from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ImageUploadForm
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


def add_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Przekierowanie gdzieś po dodaniu obrazka
    else:
        form = ImageUploadForm()

    return render(request, 'image_manipulator/add_image.html', {'form': form})
