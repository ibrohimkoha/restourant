from django.contrib import admin
from .models import MessageModel, ReservationModel


# Register your models here.
@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number',)
    order_display = ('-created_at')
    search_fields = ('name', 'email', 'number',)


@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone', 'datepicker',)
    order_display = ('-created_at')
    search_fields = ('name', 'email', 'phone',)
