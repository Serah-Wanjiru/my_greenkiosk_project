from django.shortcuts import render
from .forms import ShipAploadForm
from shipments.models import Shipping

def upload_shipment(request):
    if request.method == 'POST':
        form = ShipAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ShipAploadForm()
    return render(request,'shipments/shipments_upload.html',{'form': form})



def shipments_list(request):
    shipping = Shipping.objects.all()
    return render(request, "shipments/shipments_list.html", {"shipping": shipping})


def edit_shipments_view(request, id):
    shipping = Shipping.objects.get(id=id)
    if request.method == 'POST':
        form = ShipAploadForm(request.POST, instance=shipping)
        if form.is_valid():
            form.save()
            
        form = ShipAploadForm(instance=shipping)
    return render(request, "shipments/edit_shipments.html", {"form": form})


