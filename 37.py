# Write a program having classes as Product, Order, Customer
# Do appropriate inheritance of the above classes
# Write appropriate methods / constructors in each classes
# Following output is expected
# Order No : SO001
# Customer : Sanjay Patel
# Customer Email : sanjay@dummy.com
# Name of the product is 'Pencil'
# Product Qty is : 15
# Unit Price is 20
# Order total is : 300

# class Product:
#     def __init__(self,name,quantity,price):
#         self.name=name
#         self.quantity=quantity
#         self.price=price
#
#
# class Order(Product):
#     def __init__(self,name,quantity,price,order_no,order_total):
#         super().__init__(name,quantity,price)
#         self.order_no=order_no
#         self.order_total=order_total
#
# class Customer():
#     def __init__(self,name,quantity,price,order_no,order_total,customer_name,customer_email):
#         super().__init__(name, quantity, price,order_no,order_total)
#         self.customer_name=customer_name
#         self.customer_email=customer_email
#
#     def order_details(self):
#         return f"order_no:{self.order_no}\n" \
#                f"customer:{self.customer_name}\n" \
#                f"customer_email:{self.customer_email}\n" \
#                f"product_name:{self.name}\n" \
#                f"product_quantity:{self.quantity}\n" \
#                f"price:{self.price}\n" \
#                f"total:{self.order_total}"
#
# # p=Product('Pencil',20,'5 rs')
# # o=Order('Pencil',20,'5 rs','S0001',100)
# c=Customer('Pencil',20,'5 rs','S0001',100,'Meet','meet@gmail.com')
#
# print(c.order_details())



# =============================================================
class Customer():
    def __init__(self,customer_name,customeremail):
        self.customer_name=input("enter customer name:")
        self.customer_email=input("enter customer_email:")

class Product:
    def __init__(self,name,quantity,price):
        self.name=input("enter product  name:")
        self.quantity=int(input("enter product_quantity:"))
        self.price=int(input("enter price:"))
    def total(self):
        x=self.price * self.quantity
        return x


class Order(Product,Customer):
    def __init__(self,customer_name,customeremail,name,quantity,price,order_no,order_total):
        # super().__init__(customer_name,customer_emailname,name,quantity,price)
        Product.__init__(self,name,quantity,price)
        Customer.__init__(self,customer_name,customeremail)
        self.order_no=input("enter order_no:")
        self.order_total=Product.total(self)

    def order_details(self):
        return f"order_no:{self.order_no}\n" \
                   f"customer:{self.customer_name}\n" \
                   f"customer_email:{self.customer_email}\n" \
                   f"product_name:{self.name}\n" \
                   f"product_quantity:{self.quantity}\n" \
                   f"price:{self.price}\n" \
                   f"total:{self.order_total}"

c=Order('','','','','','','')

print(c.order_details())


