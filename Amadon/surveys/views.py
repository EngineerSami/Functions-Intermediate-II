# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def buy(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))


        product = get_object_or_404(Product, id=product_id)


        total = product.price * quantity


        request.session['recent_order_total'] = float(total)
        request.session['recent_order_quantity'] = quantity
        request.session['total_items'] = request.session.get('total_items', 0) + quantity
        request.session['total_spent'] = request.session.get('total_spent', 0.0) + float(total)


        return redirect('checkout')
    return redirect('index')

def checkout(request):
    recent_order_total = request.session.get('recent_order_total', 0)
    recent_order_quantity = request.session.get('recent_order_quantity', 0)
    total_items = request.session.get('total_items', 0)
    total_spent = request.session.get('total_spent', 0.0)

    context = {
        'recent_order_total': recent_order_total,
        'recent_order_quantity': recent_order_quantity,
        'total_items': total_items,
        'total_spent': total_spent,
    }
    return render(request, 'checkout.html', context)


# migrations/XXXX_add_initial_products.py
from django.db import migrations

def create_initial_products(apps, schema_editor):
    Product = apps.get_model('yourapp', 'Product')
    Product.objects.bulk_create([
        Product(name="Dojo T-shirt", price=19.99),
        Product(name="Dojo Sweater", price=29.99),
        Product(name="Dojo Cup", price=4.99),
        Product(name="Algorithm Book", price=49.99),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('yourapp', 'previous_migration_name'),  # Replace with the name of the latest migration
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]

