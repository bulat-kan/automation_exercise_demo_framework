from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("shop.db")


def main() -> None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.executescript(
        """
        DROP TABLE IF EXISTS order_items;
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS users;

        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );

        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            in_stock INTEGER NOT NULL
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            total REAL NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            item_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
        """
    )

    users = [
        ("John Smith", "john@mail.com"),
        ("Ana Johnson", "ana@mail.com"),
        ("Peter Parker", "peter@mail.com"),
    ]
    products = [
        ("Blue T-Shirt", 19.99, 1),
        ("Black Sneakers", 79.99, 1),
        ("Coffee Mug", 12.50, 0),
        ("Laptop Bag", 49.99, 1),
    ]
    orders = [
        (1, "paid", 99.98, "2026-04-20 10:00:00"),
        (1, "shipped", 12.50, "2026-04-21 09:30:00"),
        (2, "pending", 49.99, "2026-04-21 16:45:00"),
    ]
    order_items = [
        (1, 1, 1, 19.99),
        (1, 2, 1, 79.99),
        (2, 3, 1, 12.50),
        (3, 4, 1, 49.99),
    ]

    cursor.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        users,
    )
    cursor.executemany(
        "INSERT INTO products (name, price, in_stock) VALUES (?, ?, ?)",
        products,
    )
    cursor.executemany(
        "INSERT INTO orders (user_id, status, total, created_at) VALUES (?, ?, ?, ?)",
        orders,
    )
    cursor.executemany(
        """
        INSERT INTO order_items (order_id, product_id, quantity, item_price)
        VALUES (?, ?, ?, ?)
        """,
        order_items,
    )

    connection.commit()
    connection.close()

    print(f"Sample database created at: {DB_PATH}")


if __name__ == "__main__":
    main()
