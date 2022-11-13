from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('Grade8/', views.Grade8, name='Grade8'),
    path('Grade9/', views.Grade9, name='Grade9'),
    #path('Grade10/', views.Grade10, name='Grade10'),
    #path('Grade11/', views.Grade11, name='Grade11'),
    #path('Grade12/', views.Grade12, name='Grade12'),
    path('AllParent/', views.AllParent, name='AllParent'),
    path('StudentDetails/<int:pk_details>', views.StudentDetails, name='StudentDetails'),
    #CRUD
    path('StudentRegister/', views.StudentRegister, name='StudentRegister'),
    path('StudentEdit/<int:pk_EditStudent>', views.StudentEdit, name='StudentEdit'),   
    path('Delete/<int:pk_DeleteStudent>', views.StudentDelete, name='StudentDelete'),   
    path('ParentRegister/', views.ParentRegister, name='ParentRegister'),
    path('DeleteConfirmed/', views.DeleteConfirmed, name='DeleteConfirmed'),



]