# Generated by Django 4.1 on 2022-09-11 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='up_count',
            field=models.IntegerField(default=0),
        ),
    ]
