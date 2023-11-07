from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='books_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_created")
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)