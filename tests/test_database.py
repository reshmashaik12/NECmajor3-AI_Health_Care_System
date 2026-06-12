from database.db import get_connection

def test_db_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()
    print("DB Connection Test Passed")

if __name__ == "__main__":
    test_db_connection()