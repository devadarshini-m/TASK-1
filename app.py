from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

light_status = {"state": "off"}

@app.route('/')
def index():
    return render_template('index.html', status=light_status["state"])

@app.route('/toggle', methods=['POST'])
def toggle_light():
    if light_status["state"] == "off":
        light_status["state"] = "on"
    else:
        light_status["state"] = "off"
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
