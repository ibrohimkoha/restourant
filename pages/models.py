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
        verbose_name = 'message'
        verbose_name_plural = 'messages'


class ReservationModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    datepicker = models.CharField(max_length=15)
    phone = models.CharField(max_length=13)
    guest = models.PositiveSmallIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
