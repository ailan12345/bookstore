from django.shortcuts import render, redirect, get_object_or_404

from article.models import Book, Related
from article.forms import BookForm
from django.contrib import messages
from django.db.models.query_utils import Q
from os import name
from _csv import writer
from populate.article import publishings

def article(request):
    '''
    Render the article page
    '''
    books = Book.objects.all()
    itemList = []
    for book in books:
        items = [book]
        items.extend(list(Related.objects.filter(book=book)))
        itemList.append(items)
    context = {'itemList':itemList}
    
    return render(request, 'article/article.html', context)


def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'bookForm':BookForm()})
    # POST
    bookForm = BookForm(request.POST)
    if not bookForm.is_valid():
        return render(request, template, {'bookForm':bookForm})
    bookForm.save()
    messages.success(request,  '籍已新增')
    return redirect('article:article')
    
def articleRead(request, bookId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    book = get_object_or_404(Book, id=bookId)
    context = {
        'book': book,
        'relateds': Related.objects.filter(book=book)
    } 
    return render(request, 'article/articleRead.html', context)  


def articleUpdate(request, bookId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    book = get_object_or_404(Book, id=bookId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        bookForm = BookForm(instance=book)
        return render(request, template, {'bookForm':bookForm, 'book':book})
    # POST
    bookForm = BookForm(request.POST, instance=book)
    if not bookForm.is_valid():
        return render(request, template, {'bookForm':bookForm, 'book':book})
    bookForm.save()
    messages.success(request, '書籍已修改') 
    return redirect('article:articleRead', bookId=bookId)


def articleDelete(request, bookId):
    '''
    Delete the article instance:
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return article(request)
    # POST
    articleToDelete = get_object_or_404(Book, id=bookId)
    articleToDelete.delete()
    messages.success(request, '文章已刪除')  
    return redirect('article:article')



def articleSearch(request):
    '''
    Search for articles:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    books = Book.objects.filter(Q(name__icontains=searchTerm) |
                                Q(writer__icontains=searchTerm)|
                                Q(publishing__icontains=searchTerm)|
                                Q(date__icontains=searchTerm))
    context = {'books':books} 
    return render(request, 'article/articleSearch.html', context)