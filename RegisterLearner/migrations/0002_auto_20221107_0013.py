# Generated by Django 3.2.8 on 2022-11-06 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterLearner', '0001_initial'),
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
            field=models.CharField(blank=True, choices=[('Grade_10', 'Grade 10'), ('Grade_8', 'Grade 8'), ('Grade_9', 'Grade 9'), ('Grade_11', 'Grade 11'), ('Grade_12', 'Grade 12')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_subject',
            field=models.CharField(blank=True, choices=[('Commence', 'Commence'), ('Sports', 'Sports'), ('Engineering', 'Engineering')], max_length=50, null=True),
        ),
    ]
