# Generated by Django 4.0.1 on 2022-08-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]