from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.shortcuts import redirect, get_object_or_404

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
