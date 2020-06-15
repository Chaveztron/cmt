from django.shortcuts import render, redirect
from .models import Post, Tipo_Model, Contacto
from django.contrib.gis.geoip2 import GeoIP2


def age(request):
    """ TUTORIAL PARA HACER ESTO https://medium.com/@arrosid/get-visitor-location-using-geoip2-in-django-32ad3d417115 """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]
    if(location_country == 'Mexico'):
        return redirect("https://www.lmgtfy.es/?q=google")
    else:
        return render(request, 'pagesAd/index.html', {"location": location_country})

def index(request):
    contactos = Contacto.objects.all()
    return render(request, 'index.html', {'contactos': contactos})

def portfolio(request):
    contactos = Contacto.objects.all()
    tipoM = Tipo_Model.objects.all()
    posts=Post.objects.all()
    return render(request, 'portfolio.html', {'posts': posts, 'models': tipoM, 'contactos': contactos })

def portfolio_single(request, id):
    contactos = Contacto.objects.all()
    post = Post.objects.get(id=id)
    context = {
        "post": post,
        'contactos': contactos
    }
    return render(request, 'portfolio-single.html', context)

def about(request):
    return render(request, 'home-2.html', {})