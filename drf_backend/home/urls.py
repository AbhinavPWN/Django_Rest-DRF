from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/<int:pk>', views.student_info),
    path('info/', views.student_list),

]
