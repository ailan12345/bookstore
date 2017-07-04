from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=128, unique=True)
    writer = models.CharField(max_length=128)
    publishing = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=False)
    

    def __str__(self):
        return self.name + ' / ' + self.writer +' / ' + self.publishing
    
    class Meta:
        ordering = ['-date']


class Related(models.Model):
    book = models.ForeignKey(Book)
    edition = models.CharField(max_length=128)
    price = models.IntegerField() 

    def __str__(self):
        return self.book.name + '-' + self.edition + '-' + str(self.price)
# Create your models here.
