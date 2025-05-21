import mysql.connector



def connect_db():
    connection = mysql.connector.connect(user='devonb58',
                                   password='233481209',
                                   host='10.8.37.226',
                                   database='db_name')
    return connection


def execute(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = []
    for row in cursor:
        results.append(row)
    cursor.close()
    connection.close()
    return results

def get_student_sched(id):
    query = "CALL Student_Info('" + id + "');"
    return execute(connect_db(), query)

id_num = input("Enter your student id number:")
results = get_student_sched(id_num)

for period, course, room, teacher in results:
  print("Period: " + period)
  print("Course: " + course)
  print("Room: " + room)
  print("Teacher: " + teacher
