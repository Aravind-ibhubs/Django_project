# Generated by Django 4.2.6 on 2023-10-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syallabus', '0002_books_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]
