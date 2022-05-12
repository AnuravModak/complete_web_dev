from mysql.connector import Error
import time
import mysql.connector

# connection = mysql.connector.connect(host='localhost',
#                                          database='internship',
#                                          user='root',
#                                          password='')

# cursor = connection.cursor()
# cursor.execute("DROP TABLE sample")


def connector_register(email,password,fname,lname,login="True"):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  # this will fetch gitam database name

            # print("You're connected to database: ", record)

            # Upto this part code will always be same....


            query = "INSERT INTO user_details VALUES('{}','{}','{}','{}','{}')".format(email,password,fname,lname,login)
            # print("query executed",query)
            cursor.execute(query)
            connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")
            cursor.close()

    except Error as e:
        return [e,-1]
    finally:
        if connection.is_connected():
            connection.close()
            # print("Database is Closed")
def login_user(email):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  #
            query = "UPDATE user_details SET status='True' WHERE user_details.email='{}'".format(email)

            print(cursor.execute(query))
            connection.commit()

            myresult = cursor.fetchall()
            print(myresult)
            if len(myresult) > 0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()
def check_login(email):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT status from user_details where email='{}'".format(email)

            cursor.execute(query)

            myresult = cursor.fetchall()
            # print(myresult)
            if len(myresult)>0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return -1

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()

def find_user(email):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT password from user_details where email='{}'".format(email)

            cursor.execute(query)

            myresult = cursor.fetchall()
            # print(myresult)
            if len(myresult)>0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()

def logout_user(email):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  #
            query = "UPDATE user_details SET status='False' WHERE user_details.email='{}'".format(email)


            print(cursor.execute(query))
            connection.commit()

            myresult = cursor.fetchall()
            print(myresult)
            if len(myresult)>0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()


def edit_details(email,fname,lname,password):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  #
            if fname:
                query = "UPDATE user_details SET firstname='{}' WHERE user_details.email='{}'".format(fname,email)

                cursor.execute(query)
                print("fname")

            if lname:
                query = "UPDATE user_details SET lastname='{}' WHERE user_details.email='{}'".format(lname,email)
                cursor.execute(query)
                print("lname")


            if password:
                query = "UPDATE user_details SET password='{}' WHERE user_details.email='{}'".format(password,email)
                cursor.execute(query)
                print(password)

            connection.commit()


            myresult = cursor.fetchall()
            # print(myresult)
            if len(myresult)>0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()

def delete_account(email):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  #
            query="DELETE FROM user_details WHERE email = '{}'".format(email)
            cursor.execute(query)

            connection.commit()


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()


def add_todo_list(email,name,status,notes):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  # this will fetch gitam database name

            # print("You're connected to database: ", record)

            # Upto this part code will always be same....

            if not status:
                status="None"
            if not status:
                status="None"
            query = "INSERT INTO activities VALUES('{}','{}','{}','{}')".format(email,name,status,notes)

            connection.commit()

            # print("query executed",query)
            cursor.execute(query)
            connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")
            cursor.close()

    except Error as e:
        return [e,-1]
    finally:
        if connection.is_connected():
            connection.close()
            # print("Database is Closed")


def delete_activity(email,name):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  #
            query="DELETE FROM activities WHERE PID = '{}' and act_name='{}'".format(email,name)
            cursor.execute(query)

            connection.commit()


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()

def find_activity(email,name):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT act_name from activities where PID='{}' and act_name='{}'".format(email,name)

            cursor.execute(query)

            myresult = cursor.fetchall()
            # print(myresult)
            if len(myresult) > 0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()

def edit_activity(email,name,nname,status,notes):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            db_Info = connection.get_server_info()

            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("DROP TABLE sample")
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  #
            if nname:
                query = "UPDATE activities SET name='{}' WHERE activities.PID='{}' and activities.act_name".format(name, email,name)

                cursor.execute(query)

            if status:
                query = "UPDATE activities SET name='{}' WHERE activities.PID='{}' and activities.act_name".format(name, email,status)
                cursor.execute(query)


            if notes:
                query = "UPDATE activities SET name='{}' WHERE activities.PID='{}' and activities.act_name".format(name, email,name)
                cursor.execute(query)


            connection.commit()

            myresult = cursor.fetchall()
            # print(myresult)
            if len(myresult) > 0:
                cursor.close()
                return myresult[0][0]
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()
def get_activity(email):
    connection = mysql.connector.connect(host='localhost',
                                         database='internship',
                                         user='root',
                                         password='')
    # print(connection)
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query="SELECT act_name FROM activities WHERE PID ='{}'".format(email)
            cursor.execute(query)
            # print(cursor.execute(query))

            myresult = cursor.fetchall()
            # connection.commit()
            lis=[]
            for i in myresult:
                lis.append(i[0])

            if len(myresult) > 0:
                cursor.close()
                return lis
            else:
                cursor.close()
                return None

            # connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into user_details table")


    except Error as e:
        return [e, -1]
    finally:
        if connection.is_connected():
            connection.close()
if __name__ == '__main__':
    print(get_activity("anvmodak@gmail.com"))
    # print(delete_account("anv1@gmail.com"))
#     print(edit_details("anv@gmail.com","ddddddd","Awdawd","ddd"))
    # para=anv@gmail.com
    # print(logout_user("anv@gmail.com"))
    # print(find_user("anv@gmail.com"))
    # print(check_login("anuravmoawdddak1@gmail.com"))

    # print(connector_register("an]ak1@gmail.com","adadwad"))
# INSERT INTO user_details VALUES("avmodak1@gmail.com","password","dad","waddwdaw","True")
# UPDATE user_details SET status="True" WHERE email='anurav@gmail.com'