from django.shortcuts import render
from .forms import CustomerAploadForm
from .models import Buyer

def upload_customer(request):
    if request.method == 'POST':
        form = CustomerAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = CustomerAploadForm()
    return render(request, "customer/customer_upload.html", {"form": form})



def customer_list(request):
    buyer = Buyer.objects.all()
    return render(request,"customer/customer_list.html", {"buyer":buyer})
