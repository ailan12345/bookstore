from django import forms
from article.models import Book


class BookForm(forms.ModelForm):
    name = forms.CharField(label='書名',  max_length=128)
    writer = forms.CharField(label='作者', max_length=128)
    publishing = forms.CharField(label='出版商', max_length=128)
    date = forms.DateTimeField(label='日期', widget=forms.TextInput(attrs={'type':'date'}))
    
    class Meta:
        model = Book
        fields = ['name', 'writer', 'publishing', 'date']