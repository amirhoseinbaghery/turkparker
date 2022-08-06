# Generated by Django 4.0.4 on 2022-07-01 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productcategory_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-publish'], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AddField(
            model_name='product',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
    ]
