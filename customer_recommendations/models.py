from django.db import models

# Create your models here.

class Customer(models.Models):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    
    
    #more fields to add
    
class Recommendations(models.Models):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    

    
    
    