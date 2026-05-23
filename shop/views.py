from django.shortcuts import render
from .models import Product, Order, Stock

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def orders_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'shop/orders.html', {'orders': orders})

def products_list(request):
    products = Product.objects.all()
    stock_data = {}
    for product in products:
        try:
            stock = Stock.objects.get(product=product)
            stock_data[product.id] = stock.quantity
        except Stock.DoesNotExist:
            stock_data[product.id] = 0
    return render(request, 'shop/products.html', {
        'products': products,
        'stock_data': stock_data
    })