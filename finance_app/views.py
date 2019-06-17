from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, PlotItem


def index(request):
    return render(request, 'finance_app/home.html')

def view_portfolio(request):

    current_items = Item.objects.filter(sold_assets=False)
  
       
        
    
    sold_items = Item.objects.filter(sold_assets=True)

    context = {
        'current' : current_items,
        'sold' : sold_items
    }
    print(current_items)

    return render(request, 'finance_app/view_portfolio.html', context=context)

def buy_asset(request):
    
    if request.method == 'POST':

        new_asset = Item()
        new_asset.asset_name=request.POST.get('asset_name')
        new_asset.asset_class=request.POST.get('asset_class')
        new_asset.price=int(request.POST.get('price'))
        new_asset.quantity=int(request.POST.get('quantity'))
        new_asset.save()

        return redirect('portfolio')
    
    return render(request, 'finance_app/add_asset.html')

def sold(request):

    if request.method == 'POST':

        #to_sell = Item.object.get(id=request.POST['sold_assets'])
        item = Item.objects.get(id=request.POST.get('id'))

        item.sold_assets = True

        item.save()

        return redirect('portfolio')
    return redirect('portfolio')

def delete(request):

    if request.method == 'POST':

        to_delete = Item.objects.get(id=request.POST['id'])

        to_delete.delete()

        return redirect('portfolio')
    
    return redirect('portfolio')

# make another page for inputing data, this then is plugged into a function that generates and prints a graph
# make a login page that uses boolean to bring up database

def create_plot(request):
    
    if request.method == 'POST':
        
        plot_items = PlotItem()
        plot_item.x_value = request.POST.get('x_value')
        plot_item.y_value = request.POST.get('y_value')
        plot_items.save()
        
        