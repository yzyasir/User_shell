from django.db import models  

# Create your models here.
class User(models.Model):
    # User inherits from users.User, gets an implicit id whenever you create a new 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
