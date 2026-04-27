from database.db_helpers import (
    count_orders_for_user,
    get_out_of_stock_product_count,
    get_user_by_email,
    sum_orders_for_user,
)


def main() -> None:
    user = get_user_by_email("john@mail.com")
    print("john@mail.com ->", user)

    user_order_count = count_orders_for_user(1)
    print("user_id=1 order count ->", user_order_count)

    user_order_total = sum_orders_for_user(1)
    print("user_id=1 total order value ->", user_order_total)

    out_of_stock_count = get_out_of_stock_product_count()
    print("out of stock products ->", out_of_stock_count)

    assert user is not None
    assert user_order_count == 2
    assert user_order_total == 112.48
    assert out_of_stock_count == 1

    print("Database validation demo passed")


if __name__ == "__main__":
    main()
