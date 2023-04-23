from mysqlconnection import connectToMySQL


DATABASE = "first_flask"

class User:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def show_first_name(self):
        return self.first_name
    
    #! Create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)



    #! READ ALL
    @classmethod
    def get_all(cls):
        query = "Select * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        users = []
        for user in results:
            users.append(User(user))
        return users
    
    #!READ ONE
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result[0])
        user = User(result[0])
        return user
    
    #! UPDATE
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    #! Delete
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
        