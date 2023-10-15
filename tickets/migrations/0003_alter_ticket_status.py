# Generated by Django 4.2.5 on 2023-10-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Approved', 'Approved'), ('Declined', 'Declined'), ('InProcess', 'InProcess')], max_length=20),
        ),
    ]