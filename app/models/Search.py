from system.core.model import Model

class Search(Model):
    def __init__(self):
        super(Search, self).__init__()

    def get_favourites_by_user_id(self, session):
        if 'id' not in session:
            return False
        
        print 'Session is - ', session,'\n'
        data = {
            'id': session['id']
        }

        query = 'SELECT * FROM favorites WHERE user_id = :id'

        return self.db.query_db(query, data)

    def add_favourite(self, user_id, form):
        print "Search_add_favourite",'\n'
        query = 'INSERT INTO favorites (name, description, url, created_at, user_id) VALUES (:name, :description, :url, NOW(), :id)'
        print "Form data is ", form, '\n'

        data = {
            'name': form['name'],
            'description': form['description'],
            'url': form['current_url_search'],
            'id': user_id
        }

        return self.db.query_db(query, data)

    # def get_fav_by_user(self, user_id, fav_id):
    #     print 'Search_get_fav_by_user'
    #     data = {
    #         'user_id': user_id,
    #         'fav_id': fav_id
    #     }
    #     query = 'SELECT url FROM favorites WHERE user_id=:user_id AND id=:fav_id'
    #     favorites = self.db.query_db(query, data)
    #     print 'Search URL is ', search_url,'\n'
    #     return favorites