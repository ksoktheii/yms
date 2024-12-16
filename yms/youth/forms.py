from django import forms
from .models import Profile  # Assuming Profile is a model related to the User model

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'education_background', 'grade_attained', 'university_attended', 'course_pursued']