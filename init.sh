sudo ln -sf etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -c etc/gunicorn.py hello:app
gunicorn -c etc/gunicorn_django.py ask.wsgi:application
  
