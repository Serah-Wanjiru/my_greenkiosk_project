from django.shortcuts import render
from.forms import ProductAploadForm

def upload_product(request):
    form=ProductAploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})


