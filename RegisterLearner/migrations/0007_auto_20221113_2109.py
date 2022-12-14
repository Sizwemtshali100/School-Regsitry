# Generated by Django 3.2.8 on 2022-11-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterLearner', '0006_alter_registerparent_parenting_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerparent',
            name='Parenting_type',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother'), ('FATHER', 'Father'), ('OTHER', 'OTHER')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_Grade',
            field=models.CharField(blank=True, choices=[('Grade 8', 'Grade_8'), ('Grade 9', 'Grade_9'), ('Grade 10', 'Grade_10'), ('Grade 11', 'Grade_11'), ('Grade 12', 'Grade_12')], max_length=50, null=True, verbose_name='Registered Grade'),
        ),
    ]
