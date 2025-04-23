import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",  # Same as MySQL Workbench
        user="root",
        password="Rinku#281",
        database="pandeyji_eatery",
        port=3306  # Use the same port from MySQL Workbench
    )

    if conn.is_connected():
        print("✅ Connected successfully to MySQL!")
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")  # Check available tables
        for table in cursor.fetchall():
            print(table)  # Print table names

except mysql.connector.Error as e:
    print(f"❌ Error: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔌 Connection closed.")
