# Generated by Django 4.1 on 2022-09-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment_article_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='익명', max_length=50),
        ),
    ]
