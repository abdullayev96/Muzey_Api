# Generated by Django 4.2.6 on 2023-11-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_alter_contact_language_excursion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateField(),
        ),
    ]
