 
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from  .serializers import EbookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .forms import EbooksForms
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

# add new book 

def add(request):

    if request.method== 'POST':
        print(request.POST) 

        book_form=  EbooksForms(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('home')
       
    else: 
        book_form= EbooksForms()

    context = {'form' : book_form}
    return render(request , 'add.html',context)


# delete book 

    
def delete (request,pk ):
    d_book= EBooksModel.objects.get(id=pk)
    d_book.delete()
    return redirect('home')

# edit book details
def edit (request, pk ):
    e_book= EBooksModel.objects.get(id=pk)
    if request.method == 'POST':
        e_book_form= EbooksForms(request.POST, request.FILES, instance=e_book)
        if e_book_form.is_valid():
            e_book_form.save()
            return redirect('home')
        
    else:
        e_book_form= EbooksForms(instance=e_book)
 
    context = {'form' : e_book_form}
    return render(request , 'add.html',context)


# api rest frame work ===============>>>

@api_view ( ['GET'] )
def api (request):
    all_book = EBooksModel.objects.all()
    serializer = EbookSerializer (all_book, many=True)
    return Response(serializer.data)  

@api_view ( ['GET'] )
def api_one (request,pk):
    all_book = EBooksModel.objects.get(id=pk)
    sr = EbookSerializer (all_book, many=False)
    return Response(sr.data)

@api_view(['POST'])
def api_add(request):
    title = request.data.get('title')
    summary = request.data.get('summary')
    pages = request.data.get('pages')
    category = request.data.get('category')
    author = request.data.get('author_id')
    pdf = request.FILES.get('pdf')

    if not all([title, summary, pages, category, author, pdf]):
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ebook = EBooksModel(
            title=title,
            summary=summary,
            pages=int(pages),  
            category=category,
            author_id=author,
            pdf=pdf  
        )
        
        ebook.save()

        return Response({"detail": "Book added successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_del (request , pk):
    d_book = EBooksModel.objects.get(id=pk)
    d_book.delete()
    return Response({"message": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def api_edit (request , pk):
    api_b = EBooksModel.objects.get(id = pk)
    book_sr=  EbookSerializer(data=request.data ,instance=api_b , partial=True)
    if book_sr.is_valid():
        book_sr.save()
        return Response({"detail": "Book Edited successfully."}, status=status.HTTP_201_CREATED)
     