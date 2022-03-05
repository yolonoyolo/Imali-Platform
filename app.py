from flask import Flask, render_template, redirect, url_for, session
#from authlib.integrations.flask_client import OAuth
from datetime import timedelta
from flask import session
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        if user:
            return f(*args, **kwargs)
        return 'You aint logged in, no page for u!'
    return decorated_function

# App config
app = Flask(__name__, template_folder='templates') 
# Session config
# app.secret_key = "abc"
# app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# oAuth Setup
# oauth = OAuth(app)
# google=oauth.register(
#     name='google',
#     client_id="1005334554128-a10got2vmu0tlo420cit9lvkk402b4ml.apps.googleusercontent.com",
#     client_secret="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",
#     access_token_url='https://accounts.google.com/o/oauth2/token',
#     access_token_params=None,
#     authorize_url='https://accounts.google.com/o/oauth2/auth',
#     authorize_params=None,
#     api_base_url='https://www.googleapis.com/oauth2/v1/',
#     userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
#     client_kwargs={'scope': 'openid email profile'},
# )


@app.route("/")
def homeroute():
    page="homepage"
    return "Works"


@app.route("/index.html")
def homeroute2():
    page="homepage"
    return render_template("index.html", page=page)

@app.route("/left-sidebar.html")
def leftbar():
    page="left-sidebar"
    return render_template("left-sidebar.html",page=page)

@app.route("/right-sidebar.html")
def rightbar():
    return render_template("right-sidebar.html")

#login config and what not
# @app.route("/login-home")
# @login_required
# def hello_world():
#     session_dict = dict(session)
#     print(session_dict)
#     return f"Hello, you are logge in as {session_dict['profile']['email']}!"


# @app.route('/login')
# def login():
#     google = oauth.create_client('google')  # create the google oauth client
#     redirect_uri = url_for('authorize', _external=True)
#     return google.authorize_redirect(redirect_uri)


# @app.route('/authorize')
# def authorize():
#     google = oauth.create_client('google')  # create the google oauth client
#     token = google.authorize_access_token()  # Access token from google (needed to get user info)
#     resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
#     user_info = resp.json()
#     user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
#     # Here you use the profile/user data that you got and query your database find/register the user
#     # and set ur own data in the session not the profile from google
#     session['profile'] = user_info
#     session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
#     return redirect('/login-home')


# @app.route('/logout')
# def logout():
#     session_dict = dict(session)
#     print(f"Logout Attempt for: {session_dict['profile']['name']}")
#     for key in list(session.keys()):
#         session.pop(key)
#     print("Logout succesful")
#     return redirect('/')