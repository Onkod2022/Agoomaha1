# Generated by Django 4.0.3 on 2022-06-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agoon', '0008_alter_order_age_alter_studentreport_arabic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='age',
            field=models.IntegerField(max_length=20, verbose_name='student age'),
        ),
    ]
