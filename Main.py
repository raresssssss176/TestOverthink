from flask import Flask, render_template, redirect


LINK_FORMS_CLUB = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
LINK_FORMS_FESTIVAL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recrutari-club')
def recrutari_club():
    return redirect(LINK_FORMS_CLUB)

@app.route('/recrutari-festival')
def recrutari_festival():
    return redirect(LINK_FORMS_FESTIVAL)

if __name__ == '__main__':
    app.run(debug=True, port=5000)