def process_order(order: dict) -> dict:

    # Validaciones
    if order.get("order_id") is None or order["order_id"] <= 0:
        raise Exception("Invalid order id")
    if "@" not in order.get("customer_email", ""):
        raise Exception("Invalid email")
    if not order.get("items"):
        raise Exception("Order must have at least one item")

    # calculando subtotal
    total = 0
    for item in order["items"]:
        if item.get("quantity", 0) <= 0:
            raise Exception("Item quantity must be greater than zero")
        
        if item.get("price", 0) < 0:
            raise Exception("Item price cannot be negative")
        
        total += item["quantity"] * item["price"]
    
    # aplicando descuento
    if order.get("discount_code"):
        if order["discount_code"] == "DISCOUNT10":
            total *= 0.9
        elif order["discount_code"] == "DISCOUNT20":
            total *= 0.8
        else:
            raise Exception("Invalid discount code")
    
    # aplicando impuesto (19%)
    tax = total * 0.19
    total_with_tax = total + tax

    # simular procesamiento del pedido
    if total_with_tax > 10000:
        raise Exception("Payment rejected")
    
    # generar resumen del pedido
    summary = f"""
    order_id: {order['order_id']}
    customer_email: {order['customer_email']}
    items: {len(order['items'])}
    total before tax: {total}
    tax: {tax}
    final total: {total_with_tax}
    """
    print(summary)

    # retornar respuesta
    return {
        "order_id": order["order_id"],
        "final_total": total_with_tax
    }


if __name__ == "__main__":
    process_order(
        {
            "order_id": 123,
            "customer_email": "customer@example.com",
            "items": [
                {"name": "item1", "quantity": 2, "price": 50},
                {"name": "item2", "quantity": 1, "price": 100}
            ],
            "discount_code": "DISCOUNT10"
        }
    )
