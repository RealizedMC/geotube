from system.core.model import Model

class Registration(Model):
    def __init__(self):
        super(Registration, self).__init__()

    def get_user_by_id(self, id):
        query = 'SELECT * FROM users WHERE id=:id'
        values = {
            'id': id
        }

        return self.db.get_one(query, values)

    def get_user(self, request):
        query = 'SELECT * FROM users WHERE email=:email'
        values = {
            'email': request.form['email']
        }

        user = self.db.get_one(query, values)

        # Result is empty, no user found.
        if not user:
            return False

        if 'accessToken' not in request.form:
            print "TYPE: NORMAL LOGIN"

            if not self.bcrypt.check_password_hash(user['pw_hash'], request.form['pw']):
                return False

        else:
            print "TYPE: FACEBOOK LOGIN"
            query = 'SELECT * FROM credentials WHERE user_id=:user_id'
            values = {
                'user_id': user['id']
            }

            result = self.db.get_one(query, values)

            if not result or result['fb_id'] != request.form['userID']:
                return False

        # Return id to store in session
        return user['id']

    def add_user(self, request):
        query = 'SELECT * FROM users WHERE email=:email'
        values = {
            'email': request.form['email']
        }

        result = self.db.query_db(query, values)

        if result:
            return False

        query = 'INSERT INTO users (name, email, pw_hash, created_at) VALUES (:name, :email, :pw_hash, NOW())'
        values = {
            'name': request.form['name'],
            'email': request.form['email'],
            'pw_hash': self.bcrypt.generate_password_hash(request.form['pw'])
        }

        return self.db.query_db(query, values)

    def add_facebook_user(self, request):
        query = 'SELECT * FROM users WHERE email=:email'
        values = {
            'email': request.form['email']
        }

        result = self.db.query_db(query, values)

        if result:
            return False

        query = 'INSERT INTO users (name, email, created_at) VALUES (:name, :email, NOW())'
        values = {
            'name': request.form['name'],
            'email': request.form['email']
        }

        user_id = self.db.query_db(query, values)
        query = 'INSERT INTO credentials (user_id, fb_id) VALUES (:user_id, :fb_id)'
        values = {
            'user_id': user_id,
            'fb_id': request.form['userID']
        }

        self.db.query_db(query, values)
        return user_id


