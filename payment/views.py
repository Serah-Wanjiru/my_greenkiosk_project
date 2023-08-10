from django.shortcuts import render
from .forms import PaymentAploadForm
from .models import Payment_management

def upload_pay(request):
    if request.method == 'POST':
        form = PaymentAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PaymentAploadForm()
    return render(request, "payment/payment_upload.html", {"form": form})


