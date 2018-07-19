#!/usr/bin/python3
# gets all states via python yee boi with your own state SAFE


def main(args):
    # gets all state stuff SAFELY
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (args[4],))
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
