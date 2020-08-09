#!/usr/bin/python3
'''
lists all states from the database hbtn_0e_0_usa
'''
import sys
import MySQLdb


if __name__ == '__main__':
    connection = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    cursor = connection.cursor()
    qu = "SELECT cities.id, cities.name, states.name FROM states,"
    e = " cities WHERE cities.state_id = states.id ORDER BY cities.id"
    que = qu + e
    cursor.execute(que)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()
