from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulacja bazy danych
users = {'user@example.com': 'password123'}

# Strona logowania
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

# Strona dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    # Pobieranie losowego obrazka kota
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_image_url = response.json()[0]['url']

    return render_template('dashboard.html', cat_image_url=cat_image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
