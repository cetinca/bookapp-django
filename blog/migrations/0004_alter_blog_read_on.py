# Generated by Django 4.1.3 on 2022-11-15 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_read_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='read_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
