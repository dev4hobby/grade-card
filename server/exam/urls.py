from django.urls import path

from .views import exam_list

urlpatterns = [
    path('', exam_list),
]
