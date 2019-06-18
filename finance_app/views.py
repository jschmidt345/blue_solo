from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .models import Item
import numpy as np
import matplotlib.pyplot as plt


def index(request):
    return render(request, 'finance_app/home.html')

def buy_asset(request):
    
    if request.method == 'POST':

        new_asset = Item()
        new_asset.asset_name=request.POST.get('asset_name')
        new_asset.asset_class=request.POST.get('asset_class')
        new_asset.price=int(request.POST.get('price'))
        new_asset.quantity=int(request.POST.get('quantity'))
        new_asset.value_sum_current=new_asset.price * new_asset.quantity
        new_asset.value_sum_sold=new_asset.price * new_asset.quantity
        #new.asset.port_return=(new_asset.value_sum_sold - new_asset.value_sum_current)/new_asset.value_sum_current
        new_asset.save()
        
        return redirect('portfolio')
    
    

    return render(request, 'finance_app/add_asset.html')

def view_portfolio(request):
    
    current_items = Item.objects.filter(sold_assets=False)
    total = 0
    for i in current_items:
        total += i.value_sum_current
    
    print(total)
        
    
    sold_items = Item.objects.filter(sold_assets=True)
    total_sold = 0
    for i in sold_items:
        total_sold += i.value_sum_sold

    returns = (total_sold - total)/total

    context = {
        'current' : current_items,
        'sold' : sold_items,
        'total' : total, 
        'total_sold' : total_sold,
        'returns' : returns
    }
    print(current_items)
   

    return render(request, 'finance_app/view_portfolio.html', context=context)


    

def sold(request):

    if request.method == 'POST':

        item = Item.objects.get(id=request.POST.get('id'))
        updated_price = ((item.price * np.random.randint(-5,5)) + item.price)
        item.price = updated_price
        
        item.sold_assets = True

        item.save()
        
        
        

        return redirect('portfolio')
    return redirect('portfolio')

def returns(request):
    if request.method == 'POST':
    

        item = Item.objects.get(id=request.POST.get('id'))
        updated_price = ((item.price * np.random.randint(-5,5)) + item.price)
        item.returns = ((updated_price - item.price)/item.price)
        print(item.returns)
        item.save()

    return redirect('portfolio')
    
    


def delete(request):

    if request.method == 'POST':

        to_delete = Item.objects.get(id=request.POST['id'])

        to_delete.delete()

        return redirect('portfolio')
    
    return redirect('portfolio')


        