# Generated by Django 3.2.8 on 2022-11-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterLearner', '0011_alter_registerparent_parenting_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerparent',
            name='Parenting_type',
            field=models.CharField(blank=True, choices=[('OTHER', 'OTHER'), ('MOTHER', 'Mother'), ('FATHER', 'Father')], max_length=50, null=True),
        ),
    ]
