from flask import Flask, render_template
import psycopg2
import queries2

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main_page.html')


@app.route('/mentors')
def mentors_and_schools_page():
    mentors_schools = queries2.mentors_and_schools()
    return render_template('mentors_and_schools.html', mentors_schools=mentors_schools)


@app.route('/all-school')
def all_school_page():
    schools = queries2.all_schools()
    return render_template('all_schools.html', schools=schools)


@app.route('/mentors-by-country')
def mentors_by_country_page():
    count = queries2.mentors_by_country()
    return render_template('mentors_by_country.html', count=count)


@app.route('/contacts')
def contacts_page():
    contact = queries2.contacts()
    return render_template('contacts.html', contact=contact)


@app.route('/applicants')
def applicants_page():
    apps = queries2.applicants()
    return render_template('applicants.html', apps=apps)


@app.route('/applicants-and-mentors')
def applicants_and_mentors_page():
    apps_ments = queries2.applicants_and_mentors()
    return render_template('applicants_and_mentors.html', apps_ments=apps_ments)


if __name__ == '__main__':
    app.run(debug=True)
