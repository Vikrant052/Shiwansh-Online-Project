from django.db import models

#CATEGORY
class Category(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  

#PRODUCT
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  stock = models.PositiveIntegerField()
  
  def __str__(self):
    return self.name
  
#CART ITEM
class CartItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
#user = we complete custom user first 
  quantity = models.PositiveIntegerField()

def __str__(self):
    return f'{self.quantuty} X {self.name}'
  
#ORDER ITEM
class Order(models.Model):
  #user
  items = models.ManyToManyField(CartItem)
  total_price = models.models.DecimalField(max_digits=20, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=50,choices=[('Pending', 'Pending'),('Completed','Completed',)],default= 'Pending')
  
  # def __str__(self):
  #   return f'{self.id} by {self.user.email}'
 