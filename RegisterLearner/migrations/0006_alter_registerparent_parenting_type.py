# Generated by Django 3.2.8 on 2022-11-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterLearner', '0005_auto_20221113_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerparent',
            name='Parenting_type',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother'), ('OTHER', 'OTHER'), ('FATHER', 'Father')], max_length=50, null=True),
        ),
    ]
