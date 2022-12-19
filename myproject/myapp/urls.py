from django.urls import path
from . import views

urlpatterns = [

    path('',views.home.as_view(),name='home'),
    path('all_data',views.all_data.as_view(),name='all_data'),
    path('stu_data/<int:pk>',views.stu_data.as_view(),name='stu_data'),
    path('create_data/<str:pk>',views.create_data,name='crcreate_dataate'),


]