from populate import base
from article.models import Book,Related


books = ['如何像電腦科學家一樣思考', '10分鐘內學好Python', '簡單學習Django']
writers =['甲','乙','丙']
publishings =['AA','BB','CC']
editions = ['a', 'b', 'c', 'd']
for i in range(8):
    books.append(i)
    writers.append('w'+str(i))
    publishings.append('天使')
    
def populate():
    print('Populating Article and Comment ... ',end='')
    Book.objects.all().delete()
    Related.objects.all().delete()
    for x in range(len(books)):
        book = Book()
        book.name = books[x]
        book.writer= writers[x]
        book.publishing= publishings[x]
        book.date='2016-05-17'
        book.save()
        for edition in editions:
            Related.objects.create(book=book, price=int(100) , edition=edition)
    print('done')


if __name__ == '__main__':
    populate()
    