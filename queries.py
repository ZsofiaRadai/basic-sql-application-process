import psycopg2
import os


def run_query(query):
    try:
        # setup connection string
        connect_str = "dbname='your_database_name' user='your_username' host='localhost' password='yourpwd'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute(query)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    return cursor


def print_menu():
    os.system('clear')
    print('MENU: ')
    print('1. Mentor names')
    print('2. Nicknames at Miskolc')
    print('3. Carol\'s full name')
    print('4. Possible owner of hat')
    print('5. New applicant: Markus')
    print('6. Jemima Foreman\'s number')
    print('7. Deleting applications')
    print('8. Exit')
    print('')


def user_input():
    choice = input("Enter your choice (1-8): ")
    print('')
    return choice


def display_results():
    print_menu()
    display_again = True
    while display_again:
        choice = user_input()
        if choice == '1':
            mentor_names()
            print('')
        if choice == '2':
            nicknames_at_miskolc()
            print('')
        if choice == '3':
            applicant_carol()
            print('')
        if choice == '4':
            owner_of_the_hat()
            print('')
        if choice == '5':
            new_applicant_markus()
            print('')
        if choice == '6':
            update_jemima()
            print('')
        if choice == '7':
            delete_applicants()
            print('')
        if choice == '8':
            quit()


def mentor_names():
    cursor = run_query("""SELECT first_name, last_name FROM mentors;""")
    mentor_names = cursor.fetchall()
    print_menu()
    print('Mentor names: \n')
    for name in mentor_names:
        name = ', '.join(name)
        print(name)
    return mentor_names


def nicknames_at_miskolc():
    cursor = run_query("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    nicknames = cursor.fetchall()
    print_menu()
    print('Nicknames at Miskolc: \n')
    for name in nicknames:
        name = ', '.join(name)
        print(name)


def applicant_carol():
    cursor = run_query("""SELECT first_name, last_name, phone_number FROM applicants WHERE first_name='Carol';""")
    carol_data = cursor.fetchall()
    print_menu()
    print("Carol's full name, and her phone number: \n")
    for full_name in carol_data:
        full_name = ', '.join(full_name)
        print(full_name)


def owner_of_the_hat():
    cursor = run_query(
        """SELECT first_name, last_name, phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""")
    unknown_girl_data = cursor.fetchall()
    print_menu()
    print("The possible owners of the hat: \n")
    for full_name in unknown_girl_data:
        full_name = ', '.join(full_name)
        print(full_name)


def new_applicant_markus():
    cursor = run_query("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                            VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
    print("New applicant added. \n")
    print_menu()

    cursor = run_query("""SELECT * FROM applicants WHERE application_code=54823;""")
    new_applicant_markus_data = cursor.fetchall()
    print("New applicant's data: \n")

    new_applicant_markus_data = str(new_applicant_markus_data)
    get_the_code = new_applicant_markus_data.split(',')
    app_code = (get_the_code[5][1:-2])

    data_list = []
    data = ''
    for char in new_applicant_markus_data:
        if char in [",", "(", ")", "[", "]", "'"]:
            continue
        elif char != ' ' or type(char) == int:
            data += char
        elif char == ' ':
            if len(data) > 0:
                data_list.append(data)
                data = ''

    app_id = data_list[0]
    first_name = data_list[1]
    last_name = data_list[2]
    phone = data_list[3]
    email = data_list[4]

    print("ID: {0} \nFirst name: {1}\nLast name: {2}\nPhone number: {3}\nE-mail: {4}\nApplication code: {5}"
          .format(app_id, first_name, last_name, phone, email, app_code))


def update_jemima():
    cursor = run_query("""UPDATE applicants SET phone_number='003670/223-7459'\
                        WHERE first_name='Jemima' AND last_name='Foreman';""")
    print("Data updated. \n")
    cursor = run_query("""SELECT first_name, last_name, phone_number FROM applicants\
                        WHERE first_name='Jemima' AND last_name='Foreman';""")
    jemima_number = cursor.fetchall()
    print_menu()
    print("Jemima's number: \n")
    for number in jemima_number:
        number = ', '.join(number)
        print(number)


def delete_applicants():
    cursor = run_query("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
    print('Applicant(s) removed from database.')


if __name__ == '__main__':
    display_results()
