# Generated by Django 5.0.6 on 2024-07-18 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0011_alter_book_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='country',
            new_name='published_countries',
        ),
    ]
