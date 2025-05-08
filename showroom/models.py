from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=10, choices=[
        ('TILE', 'Tiles'),
        ('GRANITE', 'Granite'),
        ('MARBLE', 'Marble'),
    ])
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_product_type_display()} - {self.name}"
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_messages'