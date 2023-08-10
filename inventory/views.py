from django.shortcuts import render, redirect
from .forms import ProductAploadForm
from .models import Product

def upload_product(request):
    if request.method == 'POST':
        form = ProductAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products_list_view")
    else:
        form = ProductAploadForm()
    return render(request, "inventory/product_upload.html", {"form": form})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_detail.html", {"product": product})

def edit_product_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=product.id)
    else:
        form = ProductAploadForm(instance=product)
    return render(request, "inventory/edit_product.html", {"form": form})