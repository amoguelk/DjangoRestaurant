# Generated by Django 4.2.5 on 2023-09-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('IN PROCESS', 'In process'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='IN PROCESS', max_length=50),
        ),
    ]
