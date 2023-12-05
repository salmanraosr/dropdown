from django.contrib import admin
from django.urls import path
import cccapp.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dependantfield, name="dependantfield"),
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('result', views.result, name='result')
]