# app.py

import os
from flask import Flask, render_template,request,flash,redirect,url_for
from forms import BookingForm
from db import check_booking,insert_new_booking,get_all_bookings,get_booking,delete_booking,update_booking

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route("/")
def index():
    bookings = get_all_bookings()
    print(bookings)
    return render_template("index.html",bookings=bookings)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/book_table")
def create():
    form = BookingForm()  
    return render_template("book_table.html", form=form)

@app.route('/add_table', methods=['POST'])
def add_table():
    if request.method == 'POST':
        form = BookingForm()
        new_first_name = form.first_name.data.lower()
        new_last_name = form.last_name.data.lower()
        new_num_people = form.num_people.data
        new_date = form.date.data
        new_time = form.time.data

        # Check for existing booking with the same date and time
        existing_booking = check_booking(new_first_name, new_last_name, new_num_people, new_date, new_time)
        
        if existing_booking:
            flash("Booking of the same person at the same time exists.")
            return redirect(url_for('create'))
        
        # If no existing booking, proceed to insert into the database
        result = insert_new_booking(new_first_name, new_last_name, new_num_people, new_date, new_time)

        if result == "Booking successfully inserted.":
            flash("Booking successful!")
            return redirect(url_for('create'))
        else:
            flash(f"Booking failed. {result}")
            return redirect(url_for('create'))

    return render_template("book_table.html", form=form)

@app.route('/delete_booking/<int:id>', methods=['GET', 'POST'])
def delete(id):
    booking = get_booking(id)
    if booking:
        result = delete_booking(id)
        flash(result)
        return redirect(url_for('index'))
    else:
        flash('The booking you are trying to cancel does not exist.')
        return redirect(url_for('index'))

@app.route('/update_booking/<int:id>', methods=['GET', 'POST'])
def update(id):
    booking = get_booking(id)

    if not booking:
        flash('Booking not found')
        return redirect(url_for('index'))

    # Create a form with the existing booking data
    form = BookingForm(request.form, obj=booking)

    if request.method == 'POST':
        new_first_name = form.first_name.data
        new_last_name = form.last_name.data
        new_num_people = form.num_people.data
        new_date = form.date.data
        new_time = form.time.data
        if new_time is None:
            new_time = booking[0][5]
        print(new_first_name,new_last_name,new_num_people,new_date,new_time)

        # Check if any data is changed
        if (
            new_first_name != booking[0][1] or
            new_last_name != booking[0][2] or
            new_num_people != booking[0][3] or
            new_date != booking[0][4] or
            new_time != booking[0][5]
        ):
            # Check if the new booking already exists
            if not check_booking(new_first_name, new_last_name, new_num_people, new_date, new_time):
                # Update the booking
                update_result = update_booking(id, new_first_name, new_last_name, new_num_people, new_date, new_time)

                if update_result == "Booking successfully updated.":
                    flash('Booking updated successfully')
                    return redirect(url_for('index'))
                else:
                    flash(f'Failed to update booking. {update_result}')
            else:
                flash('Booking with the new details already exists')
        else:
            flash('No changes made to the booking')
    return render_template('/update_booking.html', form=form, booking=booking)

if __name__ == "__main__":
    app.run(debug=True)
