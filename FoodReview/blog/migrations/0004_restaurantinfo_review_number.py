# Generated by Django 2.1.7 on 2019-07-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_restaurantinfo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantinfo',
            name='review_number',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
