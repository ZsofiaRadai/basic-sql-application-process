import psycopg2


def run_query(query):
    try:
        connect_str = "dbname='zsofi' user='zsofi' host='localhost' password='pwd'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    return cursor


def mentors_and_schools():
    cursor = run_query("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country \
                        FROM mentors \
                        LEFT JOIN schools ON mentors.city=schools.city \
                        ORDER BY mentors.id;""")
    mentors_schools = cursor.fetchall()
    return mentors_schools


def all_schools():
    cursor = run_query("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country \
                        FROM mentors \
                        RIGHT JOIN schools ON mentors.city=schools.city \
                        ORDER BY mentors.id;""")
    schools = cursor.fetchall()
    return schools


def mentors_by_country():
    cursor = run_query("""SELECT schools.country, COUNT(mentors.first_name) AS count \
                        FROM mentors \
                        INNER JOIN schools ON mentors.city=schools.city \
                        GROUP BY schools.country \
                        ORDER BY schools.country ASC;""")
    count = cursor.fetchall()
    return count


def contacts():
    cursor = run_query("""SELECT schools.name, mentors.first_name, mentors.last_name \
                        FROM schools \
                        INNER JOIN mentors ON schools.contact_person=mentors.id \
                        ORDER BY schools.name ASC;""")
    contact = cursor.fetchall()
    return contact


def applicants():
    cursor = run_query("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date \
                        FROM applicants \
                        INNER JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id \
                        ORDER BY creation_date DESC;""")
    apps = cursor.fetchall()
    return apps


if __name__ == '__main__':
    mentors_and_schools()
