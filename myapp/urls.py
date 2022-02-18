from django.urls import path
from .views import my_func,my_func_1


urlpatterns = [
    path('',my_func, name='my-func-view'),
    path('my/',my_func_1, name='my_func_1_view'),
]