import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def add_movies(connection):
    with connection.cursor() as cursor:
        insert_query = """
        INSERT INTO movies (title, release_year, duration) 
        VALUES (%s, %s, %s), (%s, %s, %s)
        """
        movies_data = ('Godfather', 1972, 175, 'The Green Mile', 1999, 189)
        
        cursor.execute(insert_query, movies_data)
        connection.commit()


def get_all_movies(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM movies ORDER BY id")
        rows = cursor.fetchall()
        return rows
# END
