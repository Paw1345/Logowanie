from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a real secret key

# Dummy user data
users = {
    'admin': 'password'
}

def get_random_cat_image_url():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    response.raise_for_status()
    data = response.json()
    return data[0]['url']

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            cat_image_url = get_random_cat_image_url()
            return render_template('welcome.html', username=username, cat_image_url=cat_image_url)
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    cat_image_url = get_random_cat_image_url()
    return render_template('welcome.html', username=session['username'], cat_image_url=cat_image_url)

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/user_panel', methods=['GET', 'POST'])
def user_panel():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form['username']
        
        if action == 'add':
            users[username] = 'password'  # Add user with a default password
        elif action == 'delete' and username in users:
            del users[username]
    
    return render_template('user_panel.html', users=users)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

