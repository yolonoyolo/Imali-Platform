from app import render_template, app, session, login_required, redirect, oauth, google,url_for

@app.route("/")
def homeroute():
    page="homepage"
    return render_template("index.html",page=page)


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
@app.route("/login-home")
@login_required
def hello_world():
    session_dict = dict(session)
    print(session_dict)
    return f"Hello, you are logge in as {session_dict['profile']['email']}!"


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/login-home')


@app.route('/logout')
def logout():
    session_dict = dict(session)
    print(f"Logout Attempt for: {session_dict['profile']['name']}")
    for key in list(session.keys()):
        session.pop(key)
    print("Logout succesful")
    return redirect('/')
