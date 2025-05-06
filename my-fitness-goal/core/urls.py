from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='register'),
    path('goals/', views.goals_list, name='goals'),
    path('goals/add/', views.add_goal, name='add_goal'),
    path('goals/edit/<int:pk>/', views.edit_goal, name='edit_goal'),
    path('goals/delete/<int:pk>/', views.delete_goal, name='delete_goal'),
    path('workouts/', views.workouts_list, name='workouts'),
    path('workouts/add/', views.add_workout, name='add_workout'),
    path('workouts/edit/<int:pk>/', views.edit_workout, name='edit_workout'),
    path('workouts/delete/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('workouts/<int:pk>/', views.workout_detail, name='workout_detail'),
]
