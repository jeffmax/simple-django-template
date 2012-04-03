# Simple Django Project Template

This is a simple django project meant to quickly test or prototype something in Django. The settings file serves as the main urls file and view file. 
Features:
* No separate app directory. The template directory itself will be put on the PYTHONPATH and serve as an app directory.
* Two bash scripts to setup the necessary environment variables and run the django test server or django tests. They must be run from the directory they are contained in.

A couple of things:
* The settings file is setup to use a sqlite3 database to make the django TestCase happy.
* There is an empty models.py file because the django testrunner insists on finding one or it will not find your tests.py.
* DEBUG is set to True in the settings file.

*Settings file structure taken from http://olifante.blogs.com/covil/2010/04/minimal-django.html*
*Bash scripts structure taken from https://github.com/cbmi/avocado*