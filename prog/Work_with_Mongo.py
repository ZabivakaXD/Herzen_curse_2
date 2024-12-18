from pymongo import MongoClient

class MongoDBConnectionContextManager(object):
    """MongoDB Connection Context Manager"""
    def __init__(self, host='localhost', port=27017, username='admin', password='admin'):
        self.host = host; self.port = port
        self.username = username; self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            self.host, self.port,
            username=self.username, password=self.password,
            authMechanism='SCRAM-SHA-1'
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

# Использование контекстного менеджера
mongo = MongoDBConnectionContextManager(host='localhost', port=27017, username='myUserAdmin', password='abc123')
with mongo as mongo_connection_context:
    collection = mongo_connection_context.connection['myshinynewdb']['user']
    user = collection.find({'age': 205})
    print(next(user))

# Вывод результата
# {'_id': ObjectId('6385ef3006529f7b69971ef4'), 'name': 'Ada Lovelace', 'age': 205}
