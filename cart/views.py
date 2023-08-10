from django.shortcuts import render
from .forms import CartAploadForm
from .models import Basket

def upload_cart(request):
    if request.method == 'POST':
        form = CartAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = CartAploadForm()
    return render(request, "cart/cart_upload.html", {"form": form})

def cart_list(request):
    basket = Basket.objects.all()
    return render(request, "cart/cart_list.html", {"basket": basket})


def edit_cart_view(request,id):
    cart = Basket.objects.get(id=id)
    if request.method =='POST':
        form = CartAploadForm(request.POST,instance=cart)
        if form.is_valid():
            form.save()
            
        form = CartAploadForm(instance=cart)
    return render(request,"cart/edit_cart.html",{"form": form})


