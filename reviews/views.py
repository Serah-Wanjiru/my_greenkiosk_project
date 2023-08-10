from django.shortcuts import render
from .forms import ReviewAploadForm
from reviews.models import Rating


def upload_reviews(request):
    if request.method =='POST':
        form = ReviewAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ReviewAploadForm()
    return render(request,'reviews/reviews_upload.html',{'form': form})
