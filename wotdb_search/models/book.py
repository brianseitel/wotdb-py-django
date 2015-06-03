from django.db import models

class Book(models.Model):
    title  = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    class Meta:
        app_label = "wotdb_search"
        
    def chapters(self):
        from wotdb_search.models.chapter import Chapter

        return Chapter.objects.filter(book_id=self.id).extra(order_by = ['number'])
