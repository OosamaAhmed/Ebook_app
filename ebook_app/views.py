 
from django.http import HttpResponse
from django.shortcuts import render
from .models import EBooksModel


# show all books in home page ==============================>>> 
def home (request):
    allbook = EBooksModel.objects.all()
    context={'allbooks' :allbook }
    return  render ( request ,  'home.html' ,context)


# show one books in book page ==============================>>> 
def book(request, pk):
    getbook = EBooksModel.objects.get(id=pk)
    context={'book' : getbook }
    return  render ( request ,  'book.html' ,context)