from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('home/',  views.home , name= "home"),
    path('books/<int:pk> ', views.book , name= "book"),
    path('add/',  views.add , name= "add"),
    path('delete/<int:pk> ', views.delete , name= "delete"),
    path('edit/<int:pk> ', views.edit , name= "edit"),
    path('api/', views.api , name = 'api'),
    path('api/<int:pk>', views.api_one , name = 'api_one'),
    path('api/add/', views.api_add , name = 'api_add'),
    path('api/delete/<int:pk>', views.api_del , name = 'api_del'),
    path('api/edit/<int:pk>', views.api_edit , name = 'api_edit'),

]
