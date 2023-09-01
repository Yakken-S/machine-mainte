from django.urls import path
from . import views

urlpatterns = [
    path('', views.l1_list, name='l1_list'),
    path('<int:pk>/', views.issue_list, name='issue_list'),
    path('issue/post/', views.post_issue, name='post_issue'),
    path('issue/update/<int:pk>/', views.update_issue, name='update_issue'),
]