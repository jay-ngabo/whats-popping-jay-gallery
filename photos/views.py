from django.shortcuts import render
from .models import Photo, Category

# Create your views here.

def gallery(request):
    Category = Category.objects.all()
    context = { 'Category': Category }
    return render(request, 'photos/gallery.html', context)



def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')


def addPhoto(request):
    return render(request, 'photos/add.html')

