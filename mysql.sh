sudo /etc/init.d/mysql start
mysql -uroot -p -e 'DROP DATABASE QA;'
mysql -uroot -p -e 'CREATE DATABASE QA;'
mysql -uroot -p -e "CREATE USER serguser@localhost IDENTIFIED BY 'topsecret';"
mysql -uroot -p -e 'GRANT ALL ON QA.* TO serguser@localhost;'
python3 ask/manage.py makemigrations
python3 ask/manage.py migrate
