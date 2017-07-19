sudo /etc/init.d/mysql start
mysql -uroot -e 'DROP DATABASE QA;'
mysql -uroot -e 'CREATE DATABASE QA;'
mysql -uroot -e "CREATE USER serguser@localhost IDENTIFIED BY 'topsecret';"
mysql -uroot -e 'GRANT ALL ON QA.* TO serguser@localhost;'
