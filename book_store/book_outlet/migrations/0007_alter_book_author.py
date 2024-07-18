# Generated by Django 5.0.6 on 2024-07-14 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(db_column='author-id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_outlet.author'),
        ),
    ]
