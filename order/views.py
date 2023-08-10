
from django.shortcuts import render
from .forms import OrderAploadForm
from order.models import Place_order


def upload_order(request):
    if request.method == 'POST':
        form = OrderAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderAploadForm()
    return render(request, 'order/order_upload.html', {'form': form})


def order_list(request):
    orders = Place_order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})





def edit_order_view(request, id):
    order = Place_order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderAploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
        form = OrderAploadForm(instance=order)
    return render(request, "order/edit_order.html", {"form": form})