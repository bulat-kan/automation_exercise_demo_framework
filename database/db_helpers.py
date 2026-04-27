from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("shop.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_user_by_email(email: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM users WHERE email = ?
        """,
        (email,),
    )
    user = cursor.fetchone()
    connection.close()
    return user


def count_orders_for_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) FROM orders WHERE user_id = ?
        """, (user_id,),

    )
    count = cursor.fetchone()[0]
    connection.close()
    return count


def sum_orders_for_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT SUM(total) FROM orders WHERE user_id = ?
        """, (user_id,),
    )

    total = cursor.fetchone()[0]
    connection.close()

    return total if total is not None else 0


def get_out_of_stock_product_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) FROM products WHERE in_stock = 0
        """
    )
    count = cursor.fetchone()[0]
    connection.close()
    return count


if __name__ == "__main__":
    print("User by email:", get_user_by_email("john@mail.com"))
    print("Orders for user 2:", count_orders_for_user(2))
    print("Order sum for user 1:", sum_orders_for_user(1))
    print("Out of stock product count:", get_out_of_stock_product_count())
