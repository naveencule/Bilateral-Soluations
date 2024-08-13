from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def evaluate_password_strength(password):
    length_score = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()-_+=<>?/\\' for c in password)
    
    score = 0
    if length_score:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    return score

def prime_factorization(n):
    factors = []
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factors.append((2, count))

    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))

    if n > 2:
        factors.append((n, 1))
    
    return factors

@app.route('/', methods=['GET', 'POST'])
def index():
    posts = None
    password_strength = None
    factors = None
    if request.method == 'POST':
        if 'user_id' in request.form:
            user_id = int(request.form['user_id'])
            #posts = get_friend_posts(user_id)
        elif 'password' in request.form:
            password = request.form['password']
            password_strength = evaluate_password_strength(password)
        elif 'number' in request.form:
            number = int(request.form['number'])
            factors = prime_factorization(number)
    return render_template('index.html', posts=posts, password_strength=password_strength, factors=factors)

@app.route('/password_strength')
def password_strength():
    return render_template('password.html')

@app.route('/prime_factorization')
def prime_factorization_page():
    return render_template('factorization.html')

@app.route('/friend_posts')
def friend_posts():
    return render_template('friend.html')

if __name__ == '__main__':
    app.run(debug=True)
