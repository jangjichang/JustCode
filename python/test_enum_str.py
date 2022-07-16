if __name__ == '__main__':
    order_item = {"original_price": None, "product_price": 20000}

    result = order_item.get("original_price", [order_item["product_price"], "0.00"])
    result = order_item.get(order_item["original_price"])
    print(order_item.get("original_price") or order_item.get("product_price") or "0.00")


    print(result)