from django import forms

class BookingForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    num_people = forms.IntegerField(label='Number of Guests', required=True)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'], required=True)
    time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'type': 'time'}), input_formats=['%H:%M'], required=True)
