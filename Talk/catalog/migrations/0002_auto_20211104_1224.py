# Generated by Django 3.2.8 on 2021-11-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='city',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='rating',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
