from django.db import models


class Category(models.Model):

    title = models.CharField(
        max_length=250,
        unique=True
    )

    snippet = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    modified = models.DateTimeField(
        auto_now=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )


class Product(models.Model):

    alias = models.CharField(
        max_length=250,
        unique=True
    )

    title = models.CharField(
        max_length=250,
        unique=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        blank=True,
        null=True,
    )

    snippet = models.TextField(
        blank=True,
        null=True
    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.alias