# Generated by Django 5.0 on 2023-12-27 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_reservationmodel_reservation_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationmodel',
            old_name='reservation_date',
            new_name='datepicker',
        ),
        migrations.RenameField(
            model_name='reservationmodel',
            old_name='guest_number',
            new_name='guest',
        ),
        migrations.RenameField(
            model_name='reservationmodel',
            old_name='phone_number',
            new_name='phone',
        ),
    ]