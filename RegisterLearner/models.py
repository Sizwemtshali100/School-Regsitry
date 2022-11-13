from django.db import models

# Create your models here.

class RegisterStudent(models.Model):
    gender = [
        ('FEMALE','Female'),
        ('MALE','Male'),
    ]
    grade = [
        ('Grade_8','Grade 8'),
        ('Grade_9','Grade 9'),
        ('Grade_10','Grade 10'),
        ('Grade_11','Grade 11'),
        ('Grade_12','Grade 12'),
    ]
    Main_subject = [
        ('Engineering','Engineering'),
        ('Commence','Commence'),
        ('Sports','Sports'),
    ]
    Student_name = models.CharField('Students Name',max_length=50, null=True, blank=True)
    Student_surname = models.CharField('Students Surname',max_length=50, null=True, blank=True)
    Student_Gender = models.CharField('Students Gender',max_length=10, choices=gender ,null=True, blank=True)
    Student_Age = models.IntegerField('Students Age',null=True, blank=True)
    Student_Grade = models.CharField('Registered Grade',max_length=50, choices=grade, null=True, blank=True)
    Student_subject = models.CharField('Select main Subject',choices=Main_subject, max_length=50, null=True, blank=True)
    image = models.ImageField('Profile picture',null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.Student_name

class RegisterParent(models.Model):
    Parent_type = {
        ('MOTHER','Mother'),
        ('FATHER','Father'),
        ('OTHER','OTHER'),

    }
    Parent_student = models.ForeignKey(RegisterStudent, max_length=50, null=True, blank=True, on_delete=models.CASCADE)
    Parent_name = models.CharField(max_length=50, null=True, blank=True)
    Parent_Surname = models.CharField(max_length=50, null=True, blank=True)
    Parenting_type = models.CharField(choices=Parent_type, max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.Parent_name)