from django import forms


class ArticleForm(forms.Form):
    math = forms.IntegerField(label='數字', max_length=128)