from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Link
from .forms import AddLinkForm
from django.views import generic

def home(request):
    no_discounted = 0
    error = None

    form_add = AddLinkForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form_add.is_valid():
                form_add.save()
        except AttributeError:
            error = "'Ups.. couldn't get the name of the price"
        except:
            error = "Ups.. something went wrong"
    form_add = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()
    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form_add': form_add,
        'error': error,
    }
    return render(request, 'links/main.html', context=context)

def delete(request, pk):
    data = get_object_or_404(Link, id=pk)
    data.delete()
    return redirect('home')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')