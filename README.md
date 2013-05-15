# Simple Django Project Template

This is a simple django project meant to quickly test or prototype something in Django. The settings file serves as the main urls file and view file.

#### Quick start
    virtualenv test_env
    cd test_env
    source bin/activate
    git clone https://github.com/jeffmax/simple-django-template.git myapp
    cd myapp
    pip install -r requirements.txt
    ./run-server.sh
    
Navigate to `http://localhost:8000` and you should see `OK`.

#### Features:

* No separate app directory. The root directory itself will be put on the PYTHONPATH and serve as an app directory.
* Two bash scripts to setup the necessary environment variables and run a django test server (now uses uwsgi, not runserver) and run django tests. The runtests.sh must be run from the directory it resides in for PYTHONPATH reasons.

#### A couple of things:

* The settings file is setup to use a sqlite3 database to make the django TestCase happy.
* There is an empty models.py file because the django testrunner insists on finding one or it will not find your tests.py.
* DEBUG is set to True in the settings file.

* * * 
### Credits
* Inspired by http://olifante.blogs.com/covil/2010/04/minimal-django.html

* [bruth](https://github.com/bruth) provided django expertise

* Server configurations taken from https://github.com/bruth/badass-django-template. Use that template for a much more complete template and deployment

* Bash scripts originally taken from https://github.com/cbmi/avocado