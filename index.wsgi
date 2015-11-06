import sae
from booksite import wsgi

application = sae.create_wsgi_app(wsgi.application)