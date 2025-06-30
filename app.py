from flask import request, render_template, redirect, url_for, session
from models import User  # assuming User model is defined
# from werkzeug.security import check_password_hash (recommended for real use)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error_message = "Please provide both username and password."
        else:
            # Find user by username
            user = User.query.filter_by(username=username).first()

            # Validate password (plaintext check for now; not recommended)
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('dashboard'))
            else:
                error_message = "Invalid username or password."

    return render_template('login.html', error_message=error_message)
