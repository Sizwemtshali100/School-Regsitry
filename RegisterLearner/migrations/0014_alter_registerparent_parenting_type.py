# Generated by Django 3.2.8 on 2022-11-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterLearner', '0013_alter_registerparent_parenting_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerparent',
            name='Parenting_type',
            field=models.CharField(blank=True, choices=[('FATHER', 'Father'), ('OTHER', 'OTHER'), ('MOTHER', 'Mother')], max_length=50, null=True),
        ),
    ]
