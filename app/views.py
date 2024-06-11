from django.shortcuts import render,redirect
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from shoppinghyx import settings
from django.contrib import messages
import random

# Create your views here.
def product_list(request):
    products = ProductMst.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(ProductMst, pk=pk)
    sub_cats = ProductSubCat.objects.filter(product=product)
    return render(request, 'products/product_detail.html', {'product': product, 'sub_cats': sub_cats})

def product_create(request):
    if request.method == 'POST':
        form = ProductMstForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductMstForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_sub_create(request):
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductSubCatForm()
    return render(request, 'products/product_sub_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(ProductMst, pk=pk)
    if request.method == 'POST':
        form = ProductMstForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductMstForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(ProductMst, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})