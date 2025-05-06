from django import forms
from .models import Workout, Goal


#  goals form
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target', 'is_completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'target': forms.TextInput(attrs={'placeholder': 'e.g. Run 5k in 30 minutes'}),
        }


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['goal', 'date', 'activity_type', 'duration', 'sets', 'reps', 'weight', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  
        super().__init__(*args, **kwargs)
        self.fields['goal'].queryset = Goal.objects.filter(user=user)

