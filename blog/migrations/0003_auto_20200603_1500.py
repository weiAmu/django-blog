# Generated by Django 2.0 on 2020-06-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200603_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='bigcategory',
        ),
        migrations.DeleteModel(
            name='BigCategory',
        ),
    ]
