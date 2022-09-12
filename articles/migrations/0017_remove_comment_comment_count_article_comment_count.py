# Generated by Django 4.1 on 2022-09-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_comment_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_count',
        ),
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]