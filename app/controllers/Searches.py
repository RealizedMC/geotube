from system.core.controller import *

class Searches(Controller):
    def __init__(self, action):
        super(Searches, self).__init__(action)
        self.load_model('Search')

    def add_favourite(self):
        if 'id' not in session:
            return redirect('/search/get_favs_table_partial')

        print 'Searches_add_favourite'
        print 'data received - ', request.form, '\n'
        new_fav_id = self.models['Search'].add_favourite(session['id'], request.form)
        print 'New fav ID - ', new_fav_id
        # newfile = jsonify({'new_fav_id': new_fav_id})
        # return newfile
        return redirect('/search/get_favs_table_partial')

    def favs_partial_html(self):
        user_favs = self.models['Search'].get_favourites_by_user_id(session)
        print 'Searches_favs_partial_html - ', user_favs, '\n'
        return self.load_view('partials/favs_table_partial.html', user_favs=user_favs)

