from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Form Class For User Registration
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(  # Adds Email Field With Widgets
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'}))  # CSS Class To Style
    first_name = forms.CharField(  # Adds First Name Field With Max Length
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))  # CSS Class To Style
    last_name = forms.CharField(  # Adds Last Name Field With Max Length
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))  # CSS Class To Style

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # CSS Classes For Styling
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
