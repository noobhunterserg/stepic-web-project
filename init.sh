sudo ln -sf /home/serg/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/serg/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo gunicorn hello:application 
