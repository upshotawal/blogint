# Generated by Django 4.0.1 on 2022-08-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('decription', models.CharField(max_length=550)),
                ('readtiem', models.CharField(max_length=50)),
                ('authname', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
