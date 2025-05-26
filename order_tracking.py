import mysql.connector

def get_order_status(order_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="order_tracking"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT status, delivery_date FROM orders WHERE order_id = %s", (order_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        status, date = result
        return f"Order #{order_id} is {status} and expected on {date}."
    else:
        return f"Order #{order_id} not found."
