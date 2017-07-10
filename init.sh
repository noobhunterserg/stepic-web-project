sudo ln -sf /home/serg/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -c /home/serg/web/etc/gunicorn.py hello:app
gunicorn -c /home/serg/web/etc/gunicorn_django.py ask.wsgi:application
