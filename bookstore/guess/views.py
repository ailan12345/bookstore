from django.shortcuts import render, redirect
from django.contrib import messages
from cgitb import text

a=4

def guess(request):
  
    '''
    Render the article page
    '''
    return render(request, 'guess/guess.html')


def game(request):
#     b=searchTerm
#     if a>=b
#         
#     
    messages.success(request, '猜測')
    return redirect ('guess:guess')