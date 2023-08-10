from django.shortcuts import render
from .forms import VendorAploadForm
from vendor.models import Salesperson


def upload_vendor(request):
    if request.method == 'POST':
        form = VendorAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = VendorAploadForm()
    return render(request,'vendor/vendor_upload.html', {'form': form})



def vendor_list(request):
    vendors = Salesperson.objects.all()
    return render(request, "vendor/vendor_list.html", {"vendors": vendors})


def edit_vendor_view(request, id):
    vendor = Salesperson.objects.get(id=id)
    if request.method == 'POST':
        form = VendorAploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
    else:
        form = VendorAploadForm(instance=vendor)
    return render(request, "vendor/edit_vendor.html", {"form": form})



