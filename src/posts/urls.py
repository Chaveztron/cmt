
from django.urls import path
from .views import age, index, portfolio, portfolio_single, about

urlpatterns = [
    path('', age),
    path('crystal', index, name='crystal'),
    path('all', portfolio),
    path('woman/<id>/', portfolio_single, name='woman'),
    path('about', about),
]
