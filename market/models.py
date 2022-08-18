from django.db import models


class Shop(models.Model):
    class Meta:
        app_label = 'market'

    name = models.CharField(max_length=50,
                            help_text="The name of the Shop.")

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        app_label = 'market'

    category = models.CharField(max_length=50,
                                help_text="The name of the Category.")

    def __str__(self):
        return self.category


class Product(models.Model):
    class Meta:
        app_label = 'market'

    name = models.CharField(max_length=50,
                            help_text="The name of the Product.")
    description = models.TextField(help_text="The Product's description.", blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
