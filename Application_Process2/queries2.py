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


if __name__ == '__main__':
    mentors_and_schools()
