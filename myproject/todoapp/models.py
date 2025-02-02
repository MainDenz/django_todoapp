from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, default="To do item")
    content= models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        order_with_respect_to = 'user'