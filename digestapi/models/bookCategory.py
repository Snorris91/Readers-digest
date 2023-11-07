from django.db import models
from django.contrib.auth.models import User

class BookCategory(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='books_category')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='category')
    date = models.DateField(auto_now=True)