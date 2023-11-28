from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
cursor = conn.cursor()

# List of tuples containing title, URL, and image for each page
pages = [
    ("Men's Clothing", '/mens-clothing.html', 'path_to_image/men_clothing.jpg'),
    ('Activewear', '/activewear.html', 'path_to_image/activewear.jpg'),
    ('Festive Wear', '/festive.html', 'path_to_image/festive_wear.jpg'),
    # Add more tuples for other pages...
]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        # You can use session['user_id'] to fetch user-specific data from the database
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("SELECT * FROM `user` WHERE `email` = %s AND `password` = %s", (email, password))
    users = cursor.fetchall()

    if len(users) > 0:
        session['user_id'] = users[0][0]  # Assuming 'user_id' is the first column in the result
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    try:
        cursor.execute("""INSERT INTO `user` (`user_id`, `username`, `email`, `password`) VALUES
            (NULL, '{}', '{}', '{}')""".format(username, email, password))
        conn.commit()

        cursor.execute("""SELECT * FROM users WHERE email LIKE '{}'""".format(email))
        myuser = cursor.fetchall()

        if myuser:
            session['user_id'] = myuser[0][0]
            return redirect('/home')
        else:
            return redirect('/')
    except Exception as e:
        print(f"Error during user registration: {e}")
        return redirect('/register')  # Redirect to the registration page with an error message

@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/')

# Define a route for the men's clothing page
@app.route('/mens-clothing.html')
def mens_clothing():
    return render_template('mens.html')

# Define routes for the linked files in mens.html
@app.route('/activewear.html')
def activewear():
    return render_template('mens/activewear.html')

@app.route('/festive.html')
def festive():
    return render_template('mens/festive.html')

@app.route('/mjeans.html')
def jeans():
    return render_template('mens/mjeans.html')

@app.route('/m_w_n.html')
def m_w_n():
    return render_template('mens/m_w_n.html')

@app.route('/shirts.html')
def shirts():
    return render_template('mens/shirts.html')

@app.route('/suits.html')
def suits():
    return render_template('mens/suits.html')

@app.route('/tshirts.html')
def tshirts():
    return render_template('mens/tshirts.html')

@app.route('/hoodies.html')
def hoodies():
    return render_template('mens/hoodies.html')

# Define a route for the women's clothing page
@app.route('/womens-clothing.html')
def womens_clothing():
    return render_template('womens.html')

# Define routes for the linked files in womens.html
@app.route('/coord.html')
def coord():
    return render_template('womens/coord.html')

@app.route('/dresses.html')
def dresses():
    return render_template('womens/dresses.html')

@app.route('/wjeans.html')
def wjeans():
    return render_template('womens/wjeans.html')

@app.route('/sarees.html')
def sarees():
    return render_template('womens/sarees.html')

@app.route('/kurta.html')
def kurta():
    return render_template('womens/kurta.html')

@app.route('/sports.html')
def sports():
    return render_template('womens/sports.html')

@app.route('/tops.html')
def tops():
    return render_template('womens/tops.html')

@app.route('/w_w_n.html')
def w_w_n():
    return render_template('womens/w_w_n.html')

# Define a route for the accessories page
@app.route('/accessories.html')
def accessories():
    return render_template('accessories.html')

# Define routes for the linked files in accessories.html
@app.route('/belts.html')
def belts():
    return render_template('accessories/belts.html')

@app.route('/bracelets.html')
def bracelets():
    return render_template('accessories/bracelets.html')

@app.route('/chains.html')
def chains():
    return render_template('accessories/chains.html')

@app.route('/footwear.html')
def footwear():
    return render_template('accessories/footwear.html')

@app.route('/glasses.html')
def glasses():
    return render_template('accessories/glasses.html')

@app.route('/hats.html')
def hats():
    return render_template('accessories/hats.html')

@app.route('/makeup.html')
def makeup():
    return render_template('accessories/makeup.html')

@app.route('/watches.html')
def watches():
    return render_template('accessories/watches.html')

@app.route('/handbags.html')
def handbags():
    return render_template('accessories/handbags.html')

# Define a route for the kids' clothing page
@app.route('/kids-clothing.html')
def kids_clothing():
    return render_template('kids.html')

# Define routes for the linked files in kids.html
@app.route('/kids.html')  # Updated route path
def kids_accessories():
    return render_template('kids.html')

@app.route('/frocks.html')
def frocks():
    return render_template('kids/frocks.html')

@app.route('/jump.html')
def jump():
    return render_template('kids/jump.html')

@app.route('/kjeans.html')
def kjeans():
    return render_template('kids/kjeans.html')

@app.route('/ktshirts.html')
def ktshirts():
    return render_template('kids/ktshirts.html')

@app.route('/newborn.html')
def newborn():
    return render_template('kids/newborn.html')

@app.route('/night.html')
def night():
    return render_template('kids/night.html')

@app.route('/summer.html')
def summer():
    return render_template('kids/summer.html')

@app.route('/ksports.html')
def kids_sports():
    return render_template('kids/ksports.html')

@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')

# Define a route for the thank you page
@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html')

# Define a route for handling form submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    return redirect('/thankyou.html')

@app.route('/home.html')
def go_home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
