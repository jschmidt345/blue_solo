from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .models import Item, Stock
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader
import datetime
import pandas_datareader.data as web
import os


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
        new_asset.port_return=(new_asset.value_sum_sold - new_asset.value_sum_current)/(new_asset.value_sum_current)
        new_asset.save()
        
        return redirect('portfolio')
    
    

    return render(request, 'finance_app/add_asset.html')
def choose_equity(request):

    if request.method == 'POST':
        chosen_stock = Stock()
        chosen_stock.stock1=str(request.POST.get('equity_name'))
        # chosen_stock.stock2=str(request.POST.get('equity_name2'))
        chosen_stock.save()
    
        return redirect('choose')
    
    return render(request,'finance_app/choose_equity.html')

def display_data(stock1):
    start = datetime.datetime(2012, 1, 1)
    end = datetime.datetime(2019, 2, 1)
    
    equity1 = web.DataReader(stock1, 'yahoo', start, end)
    
    
    plot1 = equity1['Open'].plot(title='Open Price')
    plt.grid()
    plt.ylabel('Price')
    plt.xlabel('Years')
    plt.legend()


    my_path = "/Users/jschmidt/Desktop/pythonbootcam/workspace/blue_badge_ind/finance_project/finance_app/static/finance_app/graphs"
    plt.savefig(my_path+'/plot1.png')
    
    s_p_dat = web.DataReader('^GSPC','yahoo',start, end)
    s_p_plot = s_p_dat['Open'].plot(title='Open Price')
    plt.grid()
    plt.ylabel('Price')
    plt.xlabel('Years')
    plt.legend()
    plt.savefig(my_path+'/s_p_plot.png')
    
    plot2 = equity1['Volume'].plot(title='Trading Volume')
    plt.grid()
    plt.ylabel('Volume')
    plt.xlabel('Years')
    plt.legend()
      
    plt.savefig(my_path+'/plot2.png')   

    # plot3 = equity1['Close'].plot(title='Close Price')
    # plt.grid()
    # plt.ylabel('Price')
    # plt.xlabel('Years')
    # plt.legend()
    
    # plt.savefig(my_path+'/plot3.png')

    

def display_equity(request):
    display_data(request.POST['equity_name'])
    
     
    
    return render(request, 'finance_app/view_plot.html')


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
    
    if total > 0:
        returns = (total_sold - total)/total
    else:
        returns = 1
    
    context = {
        'current' : current_items,
        'sold' : sold_items,
        'total' : total, 
        'total_sold' : total_sold,
        'returns' : round(returns,2)
    }
    print(current_items)
   

    return render(request, 'finance_app/view_portfolio.html', context=context)


    

def sold(request):

    if request.method == 'POST':

        item = Item.objects.get(id=request.POST.get('id'))
        updated_price = ((item.price * np.random.randint(-2,2)) + item.price)
        item.price = updated_price
        
        item.sold_assets = True

        item.save()
        
        
        

        return redirect('portfolio')
    return redirect('portfolio')

def returns(request):
    if request.method == 'POST':
    

        item = Item.objects.get(id=request.POST.get('id'))
        updated_price = ((item.price * np.random.randint(-2,2)) + item.price)
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


        