# Generated by Django 3.1.7 on 2021-02-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polo',
            name='unidade',
            field=models.CharField(default='Bom Jesus', max_length=60, verbose_name='Unidade'),
            preserve_default=False,
        ),
    ]
