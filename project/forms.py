from django import forms 
from .models import Comments
from django.contrib.auth import get_user_model
 
User = get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'address', 'gender', 'photo']

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
         min_value=1, max_value=5,
         widget=forms.NumberInput(attrs={'type':'number', 'min':'1', 'max':'5'})
    )
     
    class Meta:
         model = Comments
         fields = ['name', 'email', 'desc', 'rating']




