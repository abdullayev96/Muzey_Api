# Generated by Django 4.2.6 on 2023-11-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='updated_at',
            field=models.DateField(),
        ),
    ]
