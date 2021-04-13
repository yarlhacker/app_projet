from django.shortcuts import render
from .models import Categories,ViewPhoto

def index(resquest):
    cotegory = resquest.GET.get('cotegory')
    if cotegory == None:
        photos = ViewPhoto.objects.all()
    else:
        photos = ViewPhoto.objects.filter(categories__nom = cotegory)

    categories = Categories.objects.all()
    connecte = {'categoris':categories,'photo':photos}
    return render(resquest ,'store/index.html',connecte)

def views(resquest,pk):
    photo = ViewPhoto.objects.get(id=pk)
    return render(resquest, 'store/viewsphoto.html',{'photo':photo})

# Create your views here.
