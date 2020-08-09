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
    first = "SELECT cities.name FROM cities WHERE cities.state_id = "
    second = "(SELECT states.id FROM states WHERE states.name = %(name)s)"
    argument = first + second
    cursor.execute(argument, {'name': sys.argv[4]})
    result = cursor.fetchall()
    coma = ""
    for row in result:
        print(coma, end="")
        coma = ", "
        print(row[0], end="")
    print("")
    cursor.close()
    connection.close()
