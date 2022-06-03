# Generated by Django 3.2.9 on 2022-03-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agoon', '0006_auto_20220318_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreport',
            name='Refrence',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='reference letter number'),
        ),
        migrations.AddField(
            model_name='studentreport',
            name='Total',
            field=models.IntegerField(blank=True, null=True, verbose_name='Final Business Marks'),
        ),
        migrations.AddField(
            model_name='studentreport',
            name='Total_Mid',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mid Term Business Marks'),
        ),
        migrations.AlterField(
            model_name='studentreport',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
