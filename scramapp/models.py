from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class scram(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    private = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
