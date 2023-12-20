# yourapp/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from .db import db_check_booking, db_insert_new_booking, db_get_all_bookings, db_get_booking, db_delete_booking, db_update_booking

def index(request):
    username = request.user.username.lower()
    bookings = db_get_all_bookings(username)
    #print(bookings)
    return render(request, "index.html", {'bookings': bookings})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def create(request):
    form = BookingForm()
    return render(request, "book_table.html", {'form': form})

def add_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name'].lower()
            new_last_name = form.cleaned_data['last_name'].lower()
            new_num_people = form.cleaned_data['num_people']
            new_date = form.cleaned_data['date']
            new_time = form.cleaned_data['time']
            username = request.user.username.lower()
            if new_num_people<0 or new_num_people > 20:
                messages.error(request, "The of guests should be between 0 and 20")
            else:
                # Check for an existing booking with the same date and time
                existing_booking = db_check_booking(new_first_name, new_last_name, new_num_people, new_date, new_time,username)

                if existing_booking:
                    messages.error(request, "Booking of the same person at the same time exists.")
                    return redirect('create')

                # If no existing booking, proceed to insert into the database
                result = db_insert_new_booking(new_first_name, new_last_name, new_num_people, new_date, new_time,username)

                if result == "Booking successfully inserted.":
                    messages.success(request, "Booking successful!")
                    return redirect('create')
                else:
                    messages.error(request, f"Booking failed. {result}")
                    return redirect('create')
        else:
            messages.error(request, "Form is not valid.")
    
    form = BookingForm()
    return render(request, "book_table.html", {'form': form})

def delete_booking(request, id):
    booking = db_get_booking(id)
    print(id)
    if booking:
        result = db_delete_booking(id=id)
        messages.success(request, result)
        return redirect('index')
    else:
        messages.error(request, 'The booking you are trying to cancel does not exist.')
        return redirect('index')

def update_booking(request, id):
    booking = db_get_booking(id)
    username = request.user.username.lower()

    if not booking:
        messages.error(request, 'Booking not found')
        return redirect('index')

    # Create a form with the existing booking data
    form = BookingForm(request.POST or None, initial={
        'first_name': booking[0][1],
        'last_name': booking[0][2],
        'num_people': booking[0][3],
        'date': booking[0][4],
        'time': booking[0][5],
    })

    if request.method == 'POST':
        print(form.is_valid())
        new_first_name = form.cleaned_data['first_name']
        new_last_name = form.cleaned_data['last_name']
        new_num_people = form.cleaned_data['num_people']
        new_date = form.cleaned_data['date']
        if form.cleaned_data.get('time') is None:
            new_time = booking[0][5]
        else:
            new_time = form.cleaned_data['time']
        if new_num_people<0 or new_num_people > 20:
                messages.error(request, "The of guests should be between 0 and 20")

        else:
            # Check if any data is changed
            if (
            new_first_name != booking[0][1] or
            new_last_name != booking[0][2] or
            new_num_people != booking[0][3] or
            new_date != booking[0][4] or
            new_time != booking[0][5]
            ):
                # Check if the new booking already exists
                if not db_check_booking(new_first_name, new_last_name, new_num_people, new_date, new_time,username):
                    # Update the booking
                    update_result = db_update_booking(id, new_first_name, new_last_name, new_num_people, new_date, new_time)

                    if update_result == "Booking successfully updated.":
                        messages.success(request, 'Booking updated successfully')
                        return redirect('index')
                    else:
                        messages.error(request, f'Failed to update booking. {update_result}')
                else:
                    messages.error(request, 'Booking with the new details already exists')
            else:
                messages.info(request, 'No changes made to the booking')

    return render(request, 'update_booking.html', {'form': form, 'booking': booking})