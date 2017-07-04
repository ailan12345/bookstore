from django.contrib import admin

from article.models import Book,Related

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['book','edition', 'price']
    list_display_links = ['edition']
    list_filter = ['book','edition', 'price']
    search_fields = ['edition']
    list_editable = ['price']
 
    class Meta:
        model = Related
        
class CommentModelAdmin2(admin.ModelAdmin):
    list_display = ['name','writer','publishing','date']
    list_editable = ['writer','publishing']
    
    class Meta:
        model = Book

admin.site.register(Book, CommentModelAdmin2)
admin.site.register(Related, CommentModelAdmin)

