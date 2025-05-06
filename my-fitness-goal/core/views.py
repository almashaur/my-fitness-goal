from .models import Goal
from .forms import GoalForm
from .models import Workout
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#  Goal views
@login_required
def goals_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/list.html', {'goals': goals})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals')
    else:
        form = GoalForm()
    return render(request, 'goals/form.html', {'form': form, 'title': 'Add Goal'})

@login_required
def edit_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goals/form.html', {'form': form, 'title': 'Edit Goal'})

@login_required
def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals')
    return render(request, 'goals/list.html', {'goals': Goal.objects.filter(user=request.user)})


# Workout views
@login_required
def workouts_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/list.html', {'workouts': workouts})

@login_required
def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    return render(request, 'workouts/detail.html', {'workout': workout})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST, user=request.user)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workouts')
    else:
        form = WorkoutForm(user=request.user)
    return render(request, 'workouts/form.html', {'form': form, 'title': 'Add Workout'})


@login_required
def edit_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('workouts')
    else:
        form = WorkoutForm(instance=workout, user=request.user) 
        
    return render(request, 'workouts/form.html', {'form': form, 'title': 'Edit Workout'})


@login_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts')
    return render(request, 'workouts/detail.html', {'workout': workout, 'confirm_delete': True})

# Dashboard view
@login_required
def dashboard(request):
    goals = Goal.objects.filter(user=request.user)
    workouts = Workout.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'dashboard.html', {'goals': goals, 'workouts': workouts})


# User registration view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')  # or dashboard
    return render(request, 'registration/register.html', {'form': form})