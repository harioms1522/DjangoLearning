# Generated by Django 5.0.6 on 2024-07-18 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0010_country_book_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='country',
            field=models.ManyToManyField(related_name='books', to='book_outlet.country'),
        ),
    ]