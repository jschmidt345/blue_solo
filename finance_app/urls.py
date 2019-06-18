from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_portfolio', views.view_portfolio, name='portfolio'),
    path('add_asset', views.buy_asset, name='add'),
    path('sell', views.sold, name='sold'),
    path('delete', views.delete, name='delete'),
    path('returns', views.returns, name='returns')
    
]
