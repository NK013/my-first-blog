from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Item(models.Model):
    itemname = models.CharField(
        validators=[
            MinLengthValidator(4, 'Der Name kann nur 4 - 24 Zeichen enthalten!')
            ], max_length=24
        )
    number = models.CharField(
        validators=[
            MinLengthValidator(1, 'Die Anzahl kann nur nur ein- bis dreistellig sein!!')
            ], max_length=3
        )