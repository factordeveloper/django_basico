from django.urls import path
from myapp.views import hello  #asi estaba antes
from myapp import views   #asi estaba antes
from . import views   #asi es ahora

urlpatterns = [
    path('', hello),  
    path('about/', views.about), 
    path('hello/<str:username>', views.hello), 
    path('projects/', views.projects), 
    path('tasks/<int:id>', views.tasks), 
]

