from system.core.router import routes

# Index
routes['default_controller'] = 'Registrations'

# Add favorite
routes['POST']['/search/add_favourite'] = 'Searches#add_favourite'

# Partial
routes['GET']['/search/get_favs_table_partial'] = 'Searches#favs_partial_html'

# Registration
routes['POST']['/login'] = 'Registrations#login'
routes['POST']['/register'] = 'Registrations#register'
routes['POST']['/logout'] = 'Registrations#logout'