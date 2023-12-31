# Generated by Django 4.2.6 on 2023-11-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='note/', verbose_name='rasmlar')),
            ],
            options={
                'verbose_name': 'Rasm',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Galeriya nomi')),
                ('images', models.ManyToManyField(related_name='images', to='gallery.img', verbose_name='toplami')),
            ],
            options={
                'verbose_name': 'Galeriya',
            },
        ),
    ]
