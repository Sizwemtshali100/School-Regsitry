from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . models import RegisterParent, RegisterStudent
from . forms import RegisterParentForm, RegisterStudentForm

# Create your views here.
def Home(request):
    return render(request, 'RegisterTwo/Home.html')

def AllParent(request):
    ParentsAllOfEm = RegisterParent.objects.all()
    return render(request, 'RegisterTwo/AllParent.html',
    {'ParentsAllOfEm':ParentsAllOfEm})
    
def Grade8(request):
    All_Student = RegisterStudent.objects.filter(Student_Grade='Grade_8')
    return render(request, 'RegisterTwo/Grade8.html',
    {'All_Student':All_Student})

def Grade9(request):
    All_Student = RegisterStudent.objects.filter(Student_Grade='Grade_9')
    return render(request, 'RegisterTwo/Grade9.html',
    {'All_Student':All_Student})

def ParentRegister(request):
    RegisterParent = RegisterParentForm
    if request.method == 'POST':
        RegisterParent = RegisterParentForm(request.POST)
        if RegisterParent.is_valid():
            RegisterParent.save()
    return render(request, 'RegisterTwo/ParentRegister.html',
    {'RegisterParent':RegisterParent})   


#ALL CRUD

#READ
def StudentDetails(request, pk_details):
    DetailsOfLearner = RegisterStudent.objects.get(id=pk_details)
    return render(request, 'RegisterTwo/StudentDetails.html',
    {'DetailsOfLearner':DetailsOfLearner})

#CREATE
def StudentRegister(request):
    RegisterLearner = RegisterStudentForm
    if request.method == 'POST':
        RegisterLearner = RegisterStudentForm(request.POST, request.FILES)
        if RegisterLearner.is_valid():
            RegisterLearner.save()
    return render(request, 'RegisterTwo/StudentRegister.html',
    {'RegisterLearner':RegisterLearner})
#UPDATE 
def StudentEdit(request, pk_EditStudent):
    Edit = RegisterStudent.objects.get(id=pk_EditStudent)
    EdittingStudent = RegisterStudentForm(request.POST or None, instance=Edit)
    if request.method == 'POST':
        EdittingStudent = RegisterStudentForm(request.POST)
        EdittingStudent.is_valid()
        EdittingStudent.save()
    return render(request, 'RegisterTwo/StudentEdit.html',
    {'Edit':Edit,
    'EdittingStudent':EdittingStudent})  
    
#Deleting page
def StudentDelete(request, pk_DeleteStudent):
    DeletingStudent = RegisterStudent.objects.get(id=pk_DeleteStudent)
    return render(request, 'RegisterTwo/StudentDelete.html',
    {'DeletingStudent':DeletingStudent})

def DeleteConfirmed(request, pk_DeleteStudent):
    DeletingStudent = RegisterStudent.objects.get(id=pk_DeleteStudent)
    DeletingStudent.delete()

