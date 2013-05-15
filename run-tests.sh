#!/bin/sh
PYTHONPATH=`dirname \`pwd\`` DJANGO_SETTINGS_MODULE=`basename \`pwd\``.settings django-admin.py test
