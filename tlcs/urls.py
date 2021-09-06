from django.urls import path
from .import views

urlpatterns = [
       path('',views.home,name='home'),
       path('services',views.services,name='services'),
       path('services_2',views.services_2,name='services_2'),
       path('team',views.team,name='team'),
       path('contact/',views.contact,name='contact'),
       path('project_one',views.project_one,name='project_one'),
       path('project_two',views.project_two,name='project_two'),
       path('web_one',views.web_one,name='web_one')
]