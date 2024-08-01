from django.urls import path
from .views import hello_world, name, home, submit, userdata, sample, get_data ,edit, user_delete
from . import views


urlpatterns = [
    path('', home, name = 'home'),
    path('hello/', hello_world, name = 'hello_world'),
    path('name/', name, name = 'name'),
    path('submit/', submit, name = 'submit'),
    path('user/', userdata, name = 'user'),
    path('sample/', sample, name = 'sample'),
    path('data/', get_data, name = 'data'),
    path('edit/<pk>', edit, name = 'edit'),
    path('delete/<pk>', user_delete, name = 'delete'),

]
