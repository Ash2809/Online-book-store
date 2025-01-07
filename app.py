from flask import Flask, render_template, request, redirect, session, url_for
import secrets
app = Flask(__name__, static_folder='asset')
app.secret_key = secrets.token_hex(16)  # Generates a 32-character hex key

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

# Add to Cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    book = request.form.get('book')
    price = request.form.get('price')

    # Retrieve cart from session or create a new one
    cart = session.get('cart', [])
    cart.append({'book': book, 'price': price})

    # Save updated cart back to session
    session['cart'] = cart
    return redirect(url_for('catalogue'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
