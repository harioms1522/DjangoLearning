# Generated by Django 5.0.6 on 2024-07-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_address_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
