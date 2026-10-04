from enum import Enum

class OrderStatus(Enum):
    PLACED = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5


order_status = OrderStatus.SHIPPED

if order_status == OrderStatus.PLACED:
    print("Your order has been placed")

elif order_status == OrderStatus.PROCESSING:
    print("Your order is being processed")

elif order_status == OrderStatus.SHIPPED:
    print("Your order has been shipped")

elif order_status == OrderStatus.DELIVERED:
    print("Your order has been delivered")

elif order_status == OrderStatus.CANCELLED:
    print("Your order has been cancelled")