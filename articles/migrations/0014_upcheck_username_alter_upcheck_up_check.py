# Generated by Django 4.1 on 2022-09-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_upcheck_article_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcheck',
            name='username',
            field=models.CharField(default='익명', max_length=50),
        ),
        migrations.AlterField(
            model_name='upcheck',
            name='up_check',
            field=models.IntegerField(default=0),
        ),
    ]
