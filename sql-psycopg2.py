import psycopg2

# connect to database

connection = psycopg2.connect(database="chinook")

# build cursor object
cursor = connection.cursor()

# select all records from artist 1
# cursor.execute('SELECT * FROM "Artist"')

# select name column from the aritst table 2
# cursor.execute('SELECT "Name" FROM "Artist"')

# select queen from the artist table 3

#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])


# select only by "ArtistId" #51 from the "Artist" table 4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# select only the albums with "ArtistId" #51 on the "Album" table 5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])


# select all tracks where the composer is "Queen" from the "Track" table 6
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the result(mutiple)

# results = cursor.fetchall()

# fetch the result(msingle)
results = cursor.fetchone()

# close connection
connection.close()

for result in results:
    print(result)