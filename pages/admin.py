from django.contrib import admin
from .models import MessageModel
# Register your models here.
@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number',)
    order_display = ('-create_at')
    search_fields = ('name', 'email', 'number',)