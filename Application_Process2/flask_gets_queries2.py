from flask import Flask, render_template
import psycopg2
import queries2

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main_page.html')


@app.route('/mentors')
def mentors_and_schools():
    mentors_schools = queries2.mentors_and_schools()
    return render_template('mentors_and_schools.html', mentors_schools=mentors_schools)


@app.route('/all-school')
def all_school_page():
    schools = queries2.all_schools()
    return render_template('all_schools.html', schools=schools)


if __name__ == '__main__':
    app.run(debug=True)
