from pathlib import Path
import sqlite3
from sql_practice import run_query

DB_PATH = Path(__file__).with_name("shop.db")


def main() -> None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    run_query(
        cursor,
        "1. Count all users",
        """
        SELECT COUNT(*) FROM users
        """,
    )

    run_query(
        cursor,
        "2. Count out-of-stock products",
        """
        SELECT COUNT(*) FROM products WHERE products.in_stock =?
        """, (0,),
    )

    run_query(
        cursor,
        "3. Sum all order totals",
        """
        SELECT SUM(total) FROM orders
        """,
    )

    run_query(
        cursor,
        "4. Count orders per user",
        """
        SELECT user_id, COUNT(*)
        FROM orders
        GROUP BY user_id
        """,
    )

    run_query(
        cursor,
        "5. Show users with more than one order",
        """
        SELECT user_id, COUNT(*)
        FROM orders
        GROUP BY user_id
        HAVING COUNT(*) > 1
        """,
    )
    run_query(
        cursor,
        "Show each product_id together with the total quantity across all order items for that product.",
        """
        SELECT product_id, SUM(quantity)
        FROM order_items
        GROUP BY product_id
        """,
    )

    run_query(
        cursor,
        "Show each product name together with the total quantity across all order items for that product",
        """
        SELECT products.name, SUM(quantity) 
        FROM order_items 
        JOIN products ON order_items.product_id = products.id
        GROUP BY products.name
        """,
    )
    run_query(
        cursor,
        "Group orders by status and return the count of orders in each status.",
        """
        SELECT status, COUNT(*)
        FROM orders
        GROUP BY status
        """,
    )


if __name__ == "__main__":
    main()
