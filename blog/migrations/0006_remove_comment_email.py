# Generated by Django 4.1 on 2022-08-20 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
