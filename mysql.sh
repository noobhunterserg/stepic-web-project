sudo /etc/init.d/mysql start
mysql -uroot -p1 -e 'DROP DATABASE QA;'
mysql -uroot -p1 -e 'CREATE DATABASE QA;'
mysql -uroot -p1 -e "CREATE USER serguser@localhost IDENTIFIED BY 'topsecret';"
mysql -uroot -p1 -e 'GRANT ALL ON QA.* TO serguser@localhost;'
python3 ask/manage.py makemigrations
python3 ask/manage.py migrate
