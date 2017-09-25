# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from crud.models import Item

def index(request):
    item = Item.objects.all()
    context = {
        'item' : item
    }
    return render(request, 'crud/home.html', context)
def create_post(request):
    return render(request, 'crud/create.html')
def create(request):
    item = Item(
        title = request.POST['title'],
        post = request.POST['post']
    )
    item.save()
    return redirect('/crud')
def show(request, id):
    item = Item.objects.get(id = id)
    return render(request, 'crud/show.html', {
        'item' : item
    })
def edit(request, id):
    item = Item.objects.get(id = id)
    return render(request, 'crud/edit.html', {
        'item' : item
})
def update(request, id):
    item = Item.objects.get(id = id)
    item.title = request.POST['title']
    item.post = request.POST['post']
    item.save()
    return redirect('/crud')
def destroy(request, id):
    item = Item.objects.get(id = id)
    item.delete()
    return redirect('/crud')
