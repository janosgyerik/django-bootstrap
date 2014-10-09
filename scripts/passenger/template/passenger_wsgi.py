import sys
import os

CWD = os.getcwd()

projectname = 'djbootstrap'
releasename = 'beta'
PROJECT_ROOT = os.path.join(CWD, projectname)
VIRTUALENV = os.path.join(PROJECT_ROOT, 'virtualenv')

INTERP = os.path.join(VIRTUALENV, 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = '%s.%s_settings' % (projectname, releasename)
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

# pip install paste and uncomment these lines for easier debugging
#from paste.exceptions.errormiddleware import ErrorMiddleware
#application = ErrorMiddleware(application, debug=True)
