""""
By Ismailov Sarvarbek
"""
import psycopg2

# from colorama import Fore

# 1 - MASALA
db_name = 'postgres'
password = '5'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(
    database=db_name,
    user=user,
    password=password,
    host=host,
    port=port
)

cur = conn.cursor()


# class Product:
#     def __init__(self, id, product_name, price, color, image):
#         self.id = id
#         self.name = product_name
#         self.price = price
#         self.color = color
#         self.image = image
#
#
# """CREATE TABLE PRODUCTS"""
#
#
# @staticmethod
# def create_table():
#     try:
#         create_table_query = '''
#             CREATE TABLE IF NOT EXISTS products (
#             id SERIAL PRIMARY KEY,
#             product_name VARCHAR(255) NOT NULL,
#             price FLOAT NOT NULL,
#             color VARCHAR(255) NOT NULL,
#             image VARCHAR(255) NOT NULL
#             )'''
#         cur.execute(create_table_query)
#         conn.commit()
#         print(Fore.GREEN + "Table created successfully" + Fore.RESET)
#     except psycopg2.DatabaseError as error:
#         print(Fore.RED + "Error creating products table" + Fore.RESET, error)
#
#
# # create_table()
#
#
# """INSERT PRODUCT"""
#
#
# def save(self):
#     try:
#         insert_query = '''
#             INSERT INTO products (product_name, price, color, image)
#             VALUES (%s, %s, %s, %s) RETURNING id'''
#         cur.execute(insert_query, (self.name, self.price, self.color, self.image))
#         self.id = cur.fetchone()[0]  # generated id
#         conn.commit()
#         print(Fore.GREEN + "Products saved successfully" + Fore.RESET)
#     except psycopg2.DatabaseError as error:
#         print(Fore.RED + "Error saving products table" + Fore.RESET, error)
#         conn.rollback()
#
#
# """UPDATE PRODUCT"""
#
#
# def update_product(self):
#     try:
#         update_query = '''
#             UPDATE products SET product_name = %s, price = %s, color = %s, image = %s WHERE id = %s
#             '''
#         cur.execute(update_query, (self.name, self.price, self.color, self.image, self.id))
#         conn.commit()
#         print(Fore.GREEN + "Product updated successfully" + Fore.RESET)
#     except psycopg2.DatabaseError as error:
#         print(Fore.RED + "Error updating products" + Fore.RESET, error)
#         conn.rollback()
#
#
# """DELETE PRODUCT"""
#
#
# @staticmethod
# def delete_product(product_id):
#     try:
#         delete_query = '''
#             DELETE FROM products WHERE id = %s
#             '''
#         cur.execute(delete_query, (product_id,))
#         conn.commit()
#         print(Fore.GREEN + f"Product with id {product_id} deleted successfully" + Fore.RESET)
#     except psycopg2.DatabaseError as error:
#         print(Fore.GREEN + f"Error deleting product with id {product_id}" + Fore.RESET)
#         conn.rollback()
#
#
# """SELECT ALL PRODUCTS"""
#
#
# @staticmethod
# def get_all():
#     try:
#         select = '''SELECT * FROM products'''
#         cur.execute(select)
#         rows = cur.fetchall()
#         product_list = [Product(*row) for row in rows]
#         return product_list
#     except psycopg2.DatabaseError as error:
#         print(Fore.RED + "Error products" + Fore.RESET, error)
#         return []
#
#
# """INPUT PRODUCT"""
#
# product1 = Product(None, 'Samsung 24 Ultra', 1600.0, 'White', 'image_1')
# product2 = Product(None, 'Samsung A34', 300.0, 'Black', 'image_2')
# product3 = Product(None, 'Iphone 15 Pro', 1250.0, 'Titan', 'image_3')
# # product1.save()
# # product2.save()
# # product3.save()
#
# """UPDATE"""
# product1.name = 'Samsung A54'
# product1.price = 500
# product1.color = 'Black'
# product1.image = 'image_update'
# # update_product()
#
# """DELETE"""
# # delete_product(3)
#
# all_products = Product.get_all()
# for Product in all_products:
#     print(
#         f"{Fore.MAGENTA}Product name:{Fore.RESET} {Product.name}, "
#         f"{Fore.CYAN}Price:{Fore.RESET} {Product.price}, "
#         f"{Fore.BLUE}Color:{Fore.RESET} {Product.color}, "
#         f"{Fore.LIGHTMAGENTA_EX}image:{Fore.RESET} {Product.image}")
# cur.close()
# conn.close()

# 6 - MASALA

class ConnectDB:
    def __init__(self):
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = conn = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()


# class CAR:
#     def __init__(self, id, car_name, price):
#         self.id = id
#         self.car_name = car_name
#         self.price = price
#
#     @staticmethod
#     def create_table():
#         with ConnectDB() as db:
#             db.cur.execute("""
#                 CREATE TABLE IF NOT EXISTS cars (
#                     id INT PRIMARY KEY,
#                     car_name VARCHAR (255) NOT NULL,
#                     price FLOAT NOT NULL
#                 )
#             """)
#
#     def save(self):
#         with ConnectDB() as db:
#             insert_into_cars = """
#                 INSERT INTO cars (id, car_name, price)
#                 VALUES (%s,%s,%s);
#             """
#             db.cur.execute(insert_into_cars, (self.id, self.car_name, self.price))
#             print(Fore.GREEN + 'Successfully saved' + Fore.RESET)
#
#     @classmethod
#     def fetch_all(cls):
#         with ConnectDB() as db:
#             db.cur.execute("""SELECT * FROM cars;""")
#             return db.cur.fetchall()
#
#
# # Create table car
# CAR.create_table()
#
# # Insert cars
# car1 = CAR(1, 'BMW', 300000)
# car2 = CAR(2, 'Nexia 3', 9000)
# # car1.save()
# car2.save()
#
# # Get all CARS
# cars = CAR.fetch_all()
# print(cars)


# 3 MASALA
# class EnglishAlphabet:
#     def __init__(self):
#         self.letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
#         self.index = 0
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
#
# alphabet = EnglishAlphabet()
#
# for letter in alphabet:
#     print(letter)

# 4 MASALA
# import threading
# import time
#
#
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
#
#
# def print_letters():
#     for letter in "ABCDE":
#         print(letter)
#         time.sleep(1)
#
#
# # Creating threads
# number_thread = threading.Thread(target=print_numbers)
# letters_thread = threading.Thread(target=print_letters)
#
# # Starting threads
# number_thread.start()
# letters_thread.start()
#
# number_thread.join()
# letters_thread.join()
#
# print("FINISHED")
