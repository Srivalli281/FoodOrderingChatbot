import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rinku#281",
    database="pandeyji_eatery"
)

def get_order_status(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    #query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    query=("SELECT status from order_tracking WHERE order_id=%s")
    cursor.execute(query,(order_id,))
    

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None
