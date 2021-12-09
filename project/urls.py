
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studinfo/<int:pk>',views.student_details),
    path('studinfo/',views.student_list),


]
