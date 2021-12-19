# Import the LaunchDarkly SDK
import ldclient
from ldclient.config import Config
import os
from flask import Flask, render_template, session, request


# Load the LaunchDarkly SDK Key
# ldclient.set_sdk_key('sdk-381ef9b4-0a3d-456c-9fca-786f789c04a4')
ldclient.set_config(Config("<SDK_KEY>"))

# Intialise a LaunchDarkly client
ld_client = ldclient.get()


app = Flask(__name__, static_folder='public', template_folder='views')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
  if 'username' in session:
    user = {
      "key": session['username']
    }
    selling_enabled = ld_client.variation('selling_enabled', user, False)
    return render_template('home.html', selling_enabled=selling_enabled)
  return render_template('login.html')

  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        user = {
          "key": session['username']
        }
        selling_enabled = ld_client.variation('selling_enabled', user, False)
        return render_template('home.html', selling_enabled=selling_enabled)
    return render_template('login.html')

  
@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')
  
  

if __name__ == '__main__':
    app.run()
