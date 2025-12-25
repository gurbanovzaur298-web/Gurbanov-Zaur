class DatabaseConfig:
    _instance = None   
    def __new__(cls, db_name=None, user=None, password=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_name = db_name
            cls._instance.user = user
            cls._instance.password = password
        return cls._instance
    def __init__(self, db_name=None, user=None, password=None):
        pass
conf1 = DatabaseConfig("shop_db", "admin", "123")
print(f"conf1: имя БД={conf1.db_name}, пользователь={conf1.user}")
conf2 = DatabaseConfig("users_db", "root", "000")
print(f"conf2: имя БД={conf2.db_name}, пользователь={conf2.user}")
print(f"\nconf1 is conf2: {conf1 is conf2}")
print(f"id(conf1): {id(conf1)}")
print(f"id(conf2): {id(conf2)}")
