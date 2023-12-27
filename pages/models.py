from django.db import models

# Create your models here.
class MessageModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.TextField()

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='message'
        verbose_name_plural = 'messages'