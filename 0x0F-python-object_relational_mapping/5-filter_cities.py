#!/usr/bin/python3
# gets all CITIES


def main(args):
    # gets all CITY stuff
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities\
            c JOIN states s ON s.id=c.state_id\
            WHERE s.name=%s ORDER BY c.id", (args[4],))
    states = cur.fetchall()
    print(", ".join(map(lambda x: "%s" % x, states)))

if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
