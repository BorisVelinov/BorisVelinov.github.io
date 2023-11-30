from flask import Flask, jsonify, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost:3306/history_site'

def validate_registration(username, email, password, gender):
    errors = []

    # Validate username
    if not username or len(username) < 3:
        errors.append("Username must be at least 3 characters long.")

    # Validate email
    if not email or '@' not in email:
        errors.append("Invalid email address.")

    # Validate password
    if not password or len(password) < 6:
        errors.append("Password must be at least 6 characters long.")

    # Validate gender
    if not gender or gender not in ['male', 'female']:
        errors.append("Invalid gender selection.")

    return errors

def register(username, password, email, gender):
    print("REGISTER FUNC")
    print(username, password, email, gender)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="history_site"
    )

    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password, gender) VALUES (%s, %s, %s, %s)",
            (username, email, password, gender)
        )
        conn.commit()
    except Exception as e:
        print("ERROR " + e)

    cursor.close()
    conn.close()

    return True

# Регистрирайте функцията като представление с декоратора @app.route
@app.route('/register', methods=['GET','POST'])
def register_user():

    if request.method == "POST":
        email = request.form['email']
        name = request.form['username']
        password = request.form['password']
        gender = request.form.get('gender')

        status = register(name, password, email, gender)
        print(status)

    return render_template('register.html')
users = []
def login(username, password):

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Check login credentials
        if login(username, password):
            # Successful login, redirect to the index page
            return redirect(url_for('index'))
        else:
            # Failed login, render the login page with an error message
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


