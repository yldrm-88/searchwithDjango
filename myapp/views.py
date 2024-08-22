from django.shortcuts import render
from .models import*
from django.db.models import Q
# Create your views here.
def index(request):
    products=Products.objects.all()
    context={
        'products':products
    }
    return render(request, 'index.html',context)

def detail(request,id):
    products=Products.objects.get(id=id)
    context={
        'products':products
    }
    return render(request,'detail.html',context)

def search(request):
   if request.method == 'POST':
    searched=request.POST['searched']
    products=Products.objects.filter(
     Q(title__icontains=searched)| Q(description__icontains=searched)
    )
    context={
       'searched':searched,
       'products':products,
    }
    return render(request,'search.html',context)
   else:
    return render(request,'search.html')