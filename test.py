# # while True:
# #     data = input("Please enter a loud message (must be all caps): ")
# #     if not data.isupper():
# #         print("Sorry, your response was not loud enough.")
# #         continue
# #     else:
# #         #we're happy with the value given.
# #         #we're ready to exit the loop.
# #         break
# # ===================================================================
#
# class Product:
#     def __init__(self, list_of_products):
#         self.products = list_of_products
#
#     def displayAvailableproducts(self):
#         print("products present are: ")
#         for product in self.products:
#             print(" *" + product)
#
#     def purchaseproduct(self, product_name):
#         if product_name in self.products:
#             print(f"You have purchased {product_name}")
#             self.products.remove(product_name)
#             return True
#         else:
#             print(
#                 "Sorry, This product is either not available or has already purchased by someone else. Please wait until the product is available")
#             return False
#
#     def saleproduct(self, product_name):
#         self.products.append(product_name)
#         print("Thanks for selling this product!")
#
#
# class Customer:
#     def purchaseproduct(self):
#         self.products = input("Enter the name of the product you want to purchase: ")
#         return self.products
#
#     def saleproduct(self):
#         self.products = input("Enter the name of the product you want to sell: ")
#         return self.products
#
#
# if __name__ == "__main__":
#     p = Product(["Pencil", "Pen", "Cycle", "Cover"])
#     customer = Customer()
#     # centraLibrary.displayAvailableBooks()
#     while (True):
#         welcomeMsg = '''\n =========   Welcome   ===========
#         Please choose an option:
#         1. List all the products
#         2. purchase a product
#         3. Sale a product
#         4. Exit
#         '''
#         print(welcomeMsg)
#         a = int(input("Enter a choice: "))
#         if a == 1:
#             p.displayAvailableproducts()
#         elif a == 2:
#             p.purchaseproduct(customer.purchaseproduct())
#         elif a == 3:
#             p.saleproduct(customer.saleproduct())
#         elif a == 4:
#             print("Thanks You!")
#             exit()
#         else:
#             print("Invalid Choice!")
# # ===========================================================
#  class Product():
# #     def __init__(self,product_name):
# #         self.product_name=product_name
# #         # self.product_quantity=product_quantity
# #         # self.product_total=product_total
# #
# #     def display_product(self):
# #         for products in Product:
# #             print('*'+products)
# #
# #     def display_details(self):
# #         return f'{self.product_name}\n'
# #                # f'{self.product_quantity}\n' \
# #                # f'{self.product_total}'
# # class Customer():
# #     def sale(self):
# #         pass
# #
# # if __name__ == "__main__":
# #     product = Product(["Pencil", "Pen", "Scale", "Books"])
# #     customer = Customer()
# #     while (True):
# #         print('please choose product:')
# #         print('1.Product')
# #         print('2.Sale')
# #         print('3.Purchase')
# #         print('4.Exit')
# #         a = int(input("Enter a choice: "))
# #         if a==1:
# #             product.display_product()
# #
# # p=Product('pencil')
# # print(p.display_details())
# name = input('Enter name of prduct:')
# email = input("Enter the email:")
# phn = int(input('Enter the phn:'))
# tmp_dict = {'name': name, 'email': email, 'phn': phn}
# fname = input('Enter name of fprduct:')
# fphn = int(input('Enter the fphn:'))
# tmp_dict1 = {'fname': fname, 'fphn': fphn}
# print(tmp_dict)
# print(tmp_dict1)
# x=tmp_dict1.update(tmp_dict)
# print(x)
