from system.core.controller import *
import json
import os
import re

KEY = os.environ['ACCESS_SECRET']
TOKEN = os.environ['ACCESS_TOKEN']
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class Registrations(Controller):
    def __init__(self, action):
        super(Registrations, self).__init__(action)
        self.load_model('Registration')

    def index(self):
        if 'id' in session:
            return self.load_view('search.html', id=session['id'])
        
        return self.load_view('search.html')

    def login(self):
        if 'accessToken' in request.form:
            token = request.form['accessToken']
            url = 'https://graph.facebook.com/debug_token?input_token=' + request.form['accessToken'] + '&access_token=' + TOKEN
            response = json.loads(requests.get(url).content)
            valid = response['data']['is_valid']

            if valid:
                result = self.models['Registration'].get_user(request)

                if not result:
                    print "Log in failed!"
                    return redirect('/')

                session['id'] = result
                print "Successful login for " + request.form['email']

            return redirect('/')

        # 'not in request.form' handles the case of html modification (?)
        if 'email' not in request.form or len(request.form['email']) == 0:
            flash('Please type a valid email.', 'login_email')
            return redirect('/')

        if 'pw' not in request.form or len(request.form['pw']) == 0:
            flash('Please type a valid password.', 'login_pw')
            return redirect('/')

        result = self.models['Registration'].get_user(request)

        if not result:
            flash('Login failed! Are you sure your credenticals are correct?', 'global')
            return redirect('/')

        session['id'] = result
        print "Successful login for " + request.form['email']
        return redirect('/')

    def register(self):
        if 'accessToken' in request.form:
            name = request.form['name']
            email = request.form['email']
            token = request.form['accessToken']
            url = 'https://graph.facebook.com/debug_token?input_token=' + request.form['accessToken'] + '&access_token=' + TOKEN
            response = json.loads(requests.get(url).content)
            valid = response['data']['is_valid']

            print "IS VALID: " + str(valid)

            if valid:
                result = self.models['Registration'].add_facebook_user(request)

                print "RESULT: " + str(result)

                if result:
                    session['id'] = result
                    print "Register Success for USER: " + str(result)
                    return redirect('/home')

            else:
                # There is a user with the same email existing in the db
                pass

            return redirect('/')

        if 'name' not in request.form or len(request.form['name']) == 0:
            flash('Please type a valid name.', 'name')
            return redirect('/')

        name = request.form['name']

        if len(name) < 2:
            flash('Name must be longer than 1 character.', 'name')
            return redirect('/')

        if 'email' not in request.form:
            flash('Please type a valid email.', 'register_email')
            return redirect('/')

        email = request.form['email']

        if not EMAIL_REGEX.match(email):
            flash('Please type a valid email.', 'register_email')
            return redirect('/')

        if 'pw' not in request.form:
            flash('Please type a valid password.', 'register_pw')
            return redirect('/')

        password = request.form['pw']

        if len(password) < 8:
            flash('Passwords must be longer than 8 characters.', 'register_pw')
            return redirect('/')

        result = self.models['Registration'].add_user(request)

        if not result:
            # There is a user with the same email existing in the db
            return redirect('/')

        session['id'] = result
        return redirect('/')

    def logout(self):
        print "Clearing session"
        session.clear()
        return redirect('/')

    # def testroute(self):
    #     print request.form['accessToken']
    #     url = 'https://graph.facebook.com/debug_token?input_token=' + request.form['accessToken'] + '&access_token=' + TOKEN
    #     response = json.loads(requests.get(url).content)
    #     print response['data']['is_valid']
    #     return redirect('/')


