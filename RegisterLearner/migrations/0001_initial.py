# Generated by Django 3.2.8 on 2022-11-06 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Student_surname', models.CharField(blank=True, max_length=50, null=True)),
                ('Student_Gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10, null=True)),
                ('Student_Age', models.IntegerField(blank=True, null=True)),
                ('Student_Grade', models.CharField(blank=True, choices=[('Grade_9', 'Grade 9'), ('Grade_11', 'Grade 11'), ('Grade_12', 'Grade 12'), ('Grade_10', 'Grade 10'), ('Grade_8', 'Grade 8')], max_length=50, null=True)),
                ('Student_subject', models.CharField(blank=True, choices=[('Commence', 'Commence'), ('Engineering', 'Engineering'), ('Sports', 'Sports')], max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parent_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Parent_Surname', models.CharField(blank=True, max_length=50, null=True)),
                ('Parenting_type', models.CharField(blank=True, choices=[('FATHER', 'Father'), ('MOTHER', 'Mother'), ('OTHER', 'OTHER')], max_length=50, null=True)),
                ('Parent_student', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='RegisterLearner.registerstudent')),
            ],
        ),
    ]
