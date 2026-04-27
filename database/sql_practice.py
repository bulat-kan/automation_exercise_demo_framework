from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("shop.db")


def run_query(cursor: sqlite3.Cursor, label: str, query: str, params: tuple = ()) -> None:
    print(f"\n--- {label} ---")
    print(query.strip())
    cursor.execute(query, params)
    print(cursor.fetchall())


def main() -> None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    print("\n ======== BASIC SELECT:========")
    run_query(
        cursor,
        "Show all users",
        """
        SELECT * FROM users
        """,
    )

    run_query(
        cursor,
        "Show only user names",
        """
        SELECT name FROM users
        """,
    )

    run_query(
        cursor,
        "Show all products",
        """
        SELECT * FROM products
        """,
    )

    run_query(
        cursor,
        "Show only product names and prices",
        """
        SELECT name, price FROM products
        """,
    )

    print("\n========= WHERE Filtering ===========\n")

    run_query(
        cursor,
        "Show the user whose email is `john@mail.com`",
        """
        SELECT * FROM users WHERE email = ?
        """, ("john@mail.com",),

    )

    run_query(
        cursor,
        "Show all products where `price > 20`.",
        """
        SELECT * FROM products WHERE price > ?
        """, (20,),

    )
    run_query(
        cursor,
        "7. Show all products where `in_stock = 0`.",
        """
        SELECT * FROM products WHERE in_stock = ?
        """, (0,),
    )

    run_query(
        cursor,
        "8. Show all orders where `user_id = 1`.",
        """
        SELECT * FROM orders WHERE user_id = ?
        """, (1,),
    )

    run_query(
        cursor,
        "9. Show all orders where `status = 'pending'`.",
        """
        SELECT * FROM orders WHERE status = ?
        """, ('pending',),
    )

    print("\n========== ORDER BY and LIMIT ============\n")
    run_query(
        cursor,
        "10. Show all users ordered by name ascending.",
        """
        SELECT * FROM users ORDER BY name ASC
        """,
    )
    run_query(
        cursor,
        "11. Show all orders ordered by `created_at` descending.",
        """
        SELECT * FROM orders ORDER BY created_at DESC
        """,
    )
    run_query(
        cursor,
        "12. Show the first 2 products.",
        """
        SELECT * FROM products LIMIT 2
        """,

    )

    run_query(
        cursor,
        "13. Show the most recent order only.",
        """
        SELECT * FROM orders ORDER BY created_at DESC LIMIT 1
        """,

    )

    print("\n=========== AND / OR / IN ===========\n")

    run_query(
        cursor,
        "14. Show all orders for `user_id = 1` where `status = 'shipped'`.",
        """
        SELECT * FROM orders WHERE user_id = ? AND status = ?
        """, (1, 'shipped',),

    )

    run_query(
        cursor,
        "15. Show all products where `price > 20` and `in_stock = 1`.",
        """
        SELECT * FROM products WHERE price > ? and in_stock = ?
        """, (20, 1,),

    )

    run_query(
        cursor,
        "16. Show all orders where `status = 'paid'` or `status = 'pending'`.",
        """
        SELECT * FROM orders WHERE status = ? OR status = ?
        """, ('paid', 'pending',),

    )

    run_query(
        cursor,
        "17. Rewrite question 16 using `IN`.",
        """
        SELECT * FROM orders WHERE status IN (?,?)
        """, ("paid", "pending",),
    )

    run_query(
        cursor,
        "18. Show all users whose id is either `1` or `3`",
        """
        SELECT * FROM users WHERE id IN (?,?)
        """, (1, 3,),
    )

    print("\n======== LIKE ==========\n")

    run_query(
        cursor,
        "19. Show all users whose name starts with `J`.",
        """
        SELECT * FROM users WHERE name LIKE 'J%'
        """,
    )

    run_query(
        cursor,
        "20. Show all users whose email ends with `mail.com`.",
        """
        SELECT * FROM users WHERE email LIKE '%mail.com'
        """,
    )

    run_query(
        cursor,
        "21. Show all products whose name contains `Bag`.",
        """
        SELECT * FROM products WHERE name LIKE '%Bag%'
        """,
    )

    print("\n =========== Basic JOINs =========")

    run_query(
        cursor,
        "22. Show each user name together with their order id and order status.",
        """
        SELECT users.name, orders.id, orders.status FROM users JOIN orders ON  users.id = orders.user_id
        """,

    )

    run_query(
        cursor,
        "23. Show each user name together with their order id and total.",
        """
        SELECT users.name, orders.id, orders.total FROM users JOIN orders ON users.id = orders.user_id
        """,
    )

    run_query(
        cursor,
        "24. Show order id together with product id and quantity.",
        """
        SELECT orders.id, order_items.product_id, order_items.quantity FROM orders JOIN order_items ON
        orders.id = order_items.order_id
        """,
    )
    run_query(
        cursor,
        "25. Show product name together with quantity from `order_items`.",
        """
        SELECT products.name, order_items.quantity FROM products JOIN order_items ON 
        products.id = order_items.product_id
        """,
    )

    run_query(
        cursor,
        "26. Show order id together with product name and quantity.",
        """
        SELECT order_items.order_id, products.name, order_items.quantity FROM order_items JOIN products
        ON order_items.product_id = products.id
        """,
    )
    run_query(
        cursor,
        "27. Show user name together with order id, product name, and quantity.",
        """
        SELECT users.name, orders.id, products.name, order_items.quantity
        FROM users
        JOIN orders ON users.id = orders.user_id 
        JOIN order_items ON orders.id = order_items.order_id 
        JOIN products ON products.id = order_items.product_id
        """,
    )
    print("\n============Testing-Oriented Questions===========\n")
    run_query(
        cursor,
        "28. Write a query to confirm whether a user with email `ana@mail.com` exists.",
        """
        SELECT * FROM users
        WHERE email = ?
        """, ('ana@mail.com',),
    )

    run_query(
        cursor,
        "29. Write a query to confirm whether there are any out-of-stock products.",
        """
        SELECT * FROM products
        WHERE in_stock =?
        """, (0,),
    )
    run_query(
        cursor,
        "30. Write a query to find all orders that belong to `john@mail.com`.",
        """
        SELECT orders.* FROM users
        JOIN orders ON users.id = orders.user_id
        WHERE users.email = ?
        """, ('john@mail.com',),
    )
    run_query(
        cursor,
        "31. Write a query to find all product names included in order `id = 1`.",
        """
        SELECT products.name FROM order_items 
        JOIN products ON order_items.product_id = products.id
        JOIN orders ON orders.id = order_items.order_id
        WHERE orders.id = ?
        """, (1,),
    )
    run_query(
        cursor,
        "32. Write a query to find all orders where total is greater than `50`.",
        """
        SELECT * FROM orders WHERE total > 50
        """,
    )

    run_query(
        cursor,
        "33. Write a query to find all shipped orders for `user_id = 1`.",
        """
        SELECT orders.* FROM users JOIN orders ON users.id = orders.user_id 
        WHERE orders.user_id = ? AND orders.status = ?
        """, (1, 'shipped',),
    )

    run_query(
        cursor,
        "34. Write a query to find the newest order in the database.",
        """
        SELECT * FROM orders ORDER BY created_at DESC LIMIT 1
        """,
    )

    run_query(
        cursor,
        "35. Write a query to find all users who have at least one order.",
        """
        SELECT DISTINCT users.* FROM orders JOIN users ON orders.user_id = users.id
        """,

    )
    print("\n=======Stretch Questions======\n")

    run_query(
        cursor,
        "36. Show each order with the user name and total, ordered by newest first.",
        """
        SELECT orders.id, users.name, orders.total FROM users 
        JOIN orders ON users.id = orders.user_id
        ORDER BY created_at DESC
        """,
    )

    run_query(
        cursor,
        " 37. Show each product with its quantity from `order_items`, ordered by product name.",
        """
        SELECT products.name, order_items.quantity FROM products
        JOIN order_items ON products.id =order_items.product_id
        ORDER BY products.name
        """,
    )

    run_query(
        cursor,
        "38. Show all orders for users whose name starts with `J`.",
        """
        SELECT orders.* FROM users
        JOIN orders ON users.id = orders.user_id
        WHERE users.name LIKE 'J%'
        """,
    )
    run_query(
        cursor,
        "39. Show all order items where quantity is greater than or equal to `1`.",
        """
        SELECT * FROM order_items
        WHERE quantity >=1
        """,
    )
    run_query(
        cursor,
        "40. Show all paid or shipped orders for users whose email ends with `mail.com`.",
        """
        SELECT orders.* FROM orders JOIN users ON users.id = orders.user_id
        WHERE users.email LIKE '%mail.com' 
        AND orders.status in ('paid', 'shipped')
        """,

    )

    connection.close()


if __name__ == "__main__":
    main()
