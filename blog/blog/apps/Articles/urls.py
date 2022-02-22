from django.urls import path
from . import views

app_name = 'Articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.deteil, name = 'deteil'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
               ]