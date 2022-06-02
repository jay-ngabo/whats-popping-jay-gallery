from email.mime import image
from django.shortcuts import render, redirect
from .models import Photo, Category

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = { 'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)



def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photos': photos})


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] == 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
            photo = Photo.objects.create(image=image, description=data['description'], category=category)
            return redirect('/gallery/')
    context = { 'categories': categories}
    return render(request, 'photos/add.html', context)

