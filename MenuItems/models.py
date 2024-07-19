from django.db import models
from django.contrib.auth.models import User
# Create your models here.



CATEGORY_CHOICES = (
    ('FastFood', 'FastFood'),
    ('PakistaniCuisine', 'PakistaniCuisine'),
    ('Continental', 'Continental'),
    ('Desserts', 'Desserts'),

)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, null=False, default='burger')
    image = models.ImageField(null=True, blank=True)
    ingredients = models.CharField(max_length=300)
    price = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default='FF')
    product_description = models.TextField(max_length=300, blank=False, null=False, default="none")
    product_quantity = models.IntegerField( default=1)

    def __str__(self):
        return self.product_name




class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity


    # @property
    # def get_cart_total(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.get_total for item in orderitems])
    #     return total

class shipping_address(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, default='nihal')
    email = models.CharField(max_length=200, null=True, default='none')
    number = models.CharField(max_length=100, null=True, default='111')
    address = models.CharField(max_length=400, default='none')
    city = models.CharField(max_length=200 , default='lahore')
    province = models.CharField(max_length=200, default='none')
    zipcode = models.CharField(max_length=100, default='none')
    instruction = models.CharField(max_length=500, default='none')



    def __str__(self):
        return self.address


class dineIn(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, default='Saad')
    email = models.CharField(max_length=200, null=True, default='none')
    number = models.CharField(max_length=100, null=True, default='111')
    table_no = models.CharField(max_length=200, default='none')
    people = models.CharField(max_length=100, default='none')
    requests = models.CharField(max_length=500, default='none')


    def __str__(self):
        return self.name


