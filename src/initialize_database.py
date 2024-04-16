from database_connection import get_database_connection, get_test_connection



def drop_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE users (
                        user_id TEXT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                   );
                   """)


    connection.commit()


def initialize_database():

    connection = get_database_connection()

    create_tables(connection)
    drop_tables(connection)




if __name__ == "__main__":
    initialize_database()