from flask import Flask, render_template, request

app = Flask(__name__)

# Seat map for the train coach
seats = [
    [0, 0, 0, 0, 0, 0, 0],  # Row 1
    [0, 0, 0, 0, 0, 0, 0],  # Row 2
    # ... (add remaining rows here)
    [0, 0, 0]               # Last row with 3 seats
]

@app.route('/')
def home():
    return render_template('index.html', seats=seats)

@app.route('/book', methods=['POST'])
def book():
    num_seats = int(request.form['num_seats'])
    booked_seats = book_seats(num_seats)
    return render_template('index.html', seats=seats, booked_seats=booked_seats)

def book_seats(num_seats):
    # Booking logic here
    pass

if __name__ == '__main__':
    app.run(debug=True)
