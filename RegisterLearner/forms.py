from . models import RegisterParent, RegisterStudent
from django import forms
from django.forms import ModelForm

class RegisterStudentForm(ModelForm):
    class Meta:
        model = RegisterStudent
        fields = ['Student_name','Student_surname','Student_Gender',
        'Student_Age','Student_Grade','Student_subject','image']

        #widgets = {
       #     'Student_name': forms.TextInput(attrs={'class':'form-control'}),
      #      'Student_surname': forms.TextInput(attrs={'class':'form-control'}),
     #       'Student_Gender': forms.TextInput(attrs={'class':'form-control'}),
    #        'Student_Age': forms.TextInput(attrs={'class':'form-control'}),
   #         'Student_Grade': forms.TextInput(attrs={'class':'form-control'}),
  #          'Student_subject': forms.TextInput(attrs={'class':'form-control'}),
 #           'image': forms.TextInput(attrs={'class':'form-control'}),

#        }


##
class RegisterParentForm(ModelForm):
    class Meta:
        model = RegisterParent
        fields = "__all__"