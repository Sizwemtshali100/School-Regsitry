# Generated by Django 3.2.8 on 2022-11-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterLearner', '0002_auto_20221107_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_Age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Students Age'),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_Gender',
            field=models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=10, null=True, verbose_name='Students Gender'),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_Grade',
            field=models.CharField(blank=True, choices=[('Grade_10', 'Grade 10'), ('Grade_8', 'Grade 8'), ('Grade_9', 'Grade 9'), ('Grade_11', 'Grade 11'), ('Grade_12', 'Grade 12')], max_length=50, null=True, verbose_name='Registered Grade'),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Students Name'),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_subject',
            field=models.CharField(blank=True, choices=[('Commence', 'Commence'), ('Engineering', 'Engineering'), ('Sports', 'Sports')], max_length=50, null=True, verbose_name='Select main Subject'),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='Student_surname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Students Surname'),
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Profile picture'),
        ),
    ]
