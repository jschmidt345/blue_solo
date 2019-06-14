from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    return render(request, 'finance_app/home.html')

def view_portfolio(request):

    port_items = Item.objects.filter(sold_assets=False)

    sold_items = Item.objects.filter(sold_assets=True)

    context = {
        'current' : port_items,
        'sold' : sold_items
    }

    print(port_items)

    return render(request, 'finance_app/view_portfolio.html', context=context)

def buy_asset(request):
    
    if request.method == 'POST':

        new_asset = Item(asset_name=request.POST['asset name'],
                        asset_class=request.POST['asset class'],
                        asset_price=request.POST['asset price'],
                        asset_quantity=request.POST['asset quantity'])
        new_asset.save()

        return redirect('portfolio')
    
    return render(request, 'finance_app/add_asset.html')

def sold(request):

    if request.method == 'POST':

        to_sell = Item.object.get(id=request.POST['sold'])

        to_sell.sold = request.POST['sold']

        to_sell.save()

        return redirect('portfolio')
    return redirect('portfolio')

def delete(request):

    if request.method == 'POST':

        to_delete = Item.objects.get(id=request.POST['id'])

        to_delete.delete()

        return redirect('portfolio')
    
    return redirect('portfolio')
    