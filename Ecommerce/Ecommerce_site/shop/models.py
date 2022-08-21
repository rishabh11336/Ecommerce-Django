from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=10)
    description = models.CharField(max_length=200, default='', null=False, blank=False)
    fdescription = models.CharField(max_length=500, default='', null=True, blank=True)
    tag = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='static/Shop/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();

    def get_types(self):
        return self.types.all()

    class Meta:
        db_table = "Product"