from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) # blanck nao obrigatorio
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')


    # definindo o q aparece no admin contact atraves do models
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'