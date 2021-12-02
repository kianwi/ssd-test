from flask import url_for, render_template, redirect
import re

app = Flask(__name__)

app.secret_key = "teskey"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        searchstring = request.form["search"]
        if not re.match(r'[a-z0-9_ ]{3,16}$', searchstring):
            return render_template('home.html')
        else:
            session["display"] = searchstring
            return redirect(url_for("display"))
    return render_template('home.html')


@app.route('/display', methods=['GET', 'POST'])
def display():
    return render_template('display.html', searchstring=session["display"])


if __name__ == '__main__':
    app.run()
