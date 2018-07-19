#!/usr/bin/python3
# gets all states via python yee boi with your own state


def main(args):
    # gets all state stuff by N
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
        .format(args[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == args[4]:
            print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
