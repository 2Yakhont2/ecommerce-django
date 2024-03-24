# Generated by Django 5.0.2 on 2024-03-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='uploads/product/default.png', upload_to='uploads/product/'),
        ),
    ]