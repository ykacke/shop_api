from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.category.name}"

STARS = (
        ('🌟', '🌟'),
        ('🌟🌟', '🌟🌟'),
        ('🌟🌟🌟', '🌟🌟🌟'),
        ('🌟🌟🌟🌟', '🌟🌟🌟🌟'),
        ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟'),

    )

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5, choices=STARS)
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.text