# Generated by Django 4.2.6 on 2023-11-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, verbose_name='Rahbar ismi')),
                ('about', models.CharField(max_length=100, verbose_name='Lavozimi')),
                ('number', models.CharField(max_length=20, verbose_name='Tel nomeri:')),
                ('image', models.ImageField(upload_to='note/', verbose_name='Rasm joyi')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Rahbar',
            },
        ),
    ]
