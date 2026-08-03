from django.db import models

class Caption(models.Model):
    product= models.CharField(max_length=200)
    platform= models.CharField(max_length=50)
    tone= models.CharField(max_length=200)
    feature= models.CharField(max_length=200,blank=True)
    cta= models.CharField(max_length=100)
    generated_caption= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    

    
