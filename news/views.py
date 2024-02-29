from django.shortcuts import render


from .models import News, AboutUs, Reviews

def homepage (request):
    news = News.objects.all()
    context = {'news':news}
    return render(request, 'index.html', context)

from django.shortcuts import render
from .models import News, AboutUs


def homepage(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'index.html', context)

def about(request):
    abouts = AboutUs.objects.latest("id")
    context = {'abouts': abouts}
    return render(request, 'about.html', context)

def reviews(request):
    reviews = Reviews.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews.html', context)

