import bcrypt
from flask import redirect, session
from functools import wraps

# Hashing Password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_password_complex(password):
    has_uppercase = any(char.isupper() for char in password)
    has_symbol = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?`~" for char in password)
    has_number = any(char.isdigit() for char in password)

    return has_uppercase and has_symbol and has_number

def check_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode(), hashed_password)

# Decorator
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
