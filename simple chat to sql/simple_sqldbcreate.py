import sqlite3

# creating a basic sqlite database

connect = sqlite3.connect("studentdatabase.db")  # sql lite connection

cursor = connect.cursor()

cursor.execute("CREATE TABLE STUDENT(NAME VARCHAR(255), ROLLNO INT, SECTION VARCHAR(255), MARKS INT)")

cursor.execute("INSERT INTO STUDENT VALUES('John', 1, 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('vijay', 2, 'b', 80)")
cursor.execute("INSERT INTO STUDENT VALUES('manoj', 3, 'c', 70)")
cursor.execute("INSERT INTO STUDENT VALUES('praka', 4, 'd', 75)")
cursor.execute("INSERT INTO STUDENT VALUES('rummy', 5, 'e', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('prasanth', 6, 'd', 75)")
cursor.execute("INSERT INTO STUDENT VALUES('divya', 7, 'e', 85)")


print("the data has been inserted successfully")

for each in cursor.execute("SELECT * FROM STUDENT"):
    print(each)

connect.commit()
connect.close()