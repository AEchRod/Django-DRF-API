from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    #As client app will search against this field, it must be indexed.
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True, default=0)
    #A menu item will always belong to a category.
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} - {self.price}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    #this price multiplies the unit and quantity.
    price = models.DecimalField(max_digits=6, decimal_places=2)

    #this means there can only be one menu item for a specific user.
    class Meta:
        unique_together = ('menu_item', 'user')

    def __str__(self):
        return f"{self.user.username}'s Cart Item: {self.menu_item.title}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #We need related_name as two foreign keys referring to the same field in foreign table, as both user and delivery crew refer to user id in user table.
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    #status to mark if order is delivered or not.
    status = models.BooleanField(db_index=True, default=0)
    #total price for all menu items in order.
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(db_index=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

#All items from cart will be moved here with order ID, so cart will be empty after order.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')

    def __str__(self):
        return f"Order #{self.order.id} - {self.menu_item.title} x{self.quantity}"