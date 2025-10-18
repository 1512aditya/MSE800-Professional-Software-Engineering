# # import sqlite3


# # class UserService:
# #     def get_user(self, user_id):
# #         conn = sqlite3.connect('app.db')  # New connection
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
# #         result = cursor.fetchone()
# #         conn.close()
# #         return result
 
# # class OrderService:
# #     def get_orders(self, user_id):
# #         conn = sqlite3.connect('app.db')  # Another new connection
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
# #         result = cursor.fetchall()
# #         conn.close()
# #         return result



# from msilib.schema import Class
# from re import X
# import sqlite3
# import threading

# class Database:
#     _instance = None
#     _lock = threading.Lock()
#     def __new__(cls):
#         if  cls._instance is None:
#             with cls._lock:
#                 if  cls._instance is None:
#                     cls._instance = super().__new__(cls)
#                     cls._instance.conn = None
#         return cls._instance      
        
#     def get_conn(self):
#         if self._conn  




# Class UserService:
#     def get_user(self, uid): return Database().fetch_one("SELECT * FROM users WHERE id=?", (uid,))

# class OrderService:
#     def get_orders(self, uid): return Database().fetch_all("SELECT * FROM orders WHERE user_id=?", (uid,))




import sqlite3, timeit

#Setup: create an in-memory database for testing
def setup_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INT, item TEXT)')
    c.executemany('INSERT INTO users(name) VALUES(?)', [('Adi',), ('Aditya',)])
    c.executemany('INSERT INTO orders(user_id, item) VALUES(?, ?)',
                  [(1, 'Book'), (1, 'Pen'), (2, 'Notebook')])
    conn.commit()
    return conn

# Create the in-memory DB once and keep it around for both tests
DB_CONN = setup_db()


#  Original style: open & close connection every call

def get_user_original(user_id):
    conn = sqlite3.connect(':memory:')
    # To reuse our prepared data, attach the existing in-memory DB
    conn.executescript("ATTACH DATABASE ':memory:' AS mem;")  # no-op for demonstration
    # (In real file-based DB, you'd just connect to 'app.db')
    c = DB_CONN.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return c.fetchone()

def get_orders_original(user_id):
    c = DB_CONN.cursor()
    c.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
    return c.fetchall()


#Singleton style: one shared connection
class Database:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.conn = DB_CONN      # reuse same in-memory DB
        return cls._instance
    def fetch_one(self,q,p=()): return self.conn.execute(q,p).fetchone()
    def fetch_all(self,q,p=()): return self.conn.execute(q,p).fetchall()

def get_user_singleton(user_id):
    return Database().fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))

def get_orders_singleton(user_id):
    return Database().fetch_all("SELECT * FROM orders WHERE user_id = ?", (user_id,))


# Timing comparison
#Each function runs 1,000 database queries so the performance difference is measurable
def run_original():
    for _ in range(1000):
        get_user_original(1)
        get_orders_original(1)

def run_singleton():
    for _ in range(1000):
        get_user_singleton(1)
        get_orders_singleton(1)

print("Original (new connection each time):",
      timeit.timeit(run_original, number=1), "seconds")
print("Singleton (shared connection):",
      timeit.timeit(run_singleton, number=1), "seconds")
