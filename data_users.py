import random

with open('data.sh', 'w') as f:
    for i in range(1, 6):
        mysql_part  = "mysql -userguser -ptopsecret -e "
        mysql_part2 = 'USE QA; INSERT auth_user(id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES'
        b = '0'
        date = '2010-10-10'
        id__ = str(i)
        auth = 'auth' + id__
        f.write (mysql_part + '"' + mysql_part2 + "(" + id__ + "," + "'" + b + "'," + "'" + date + "',"  + b + "," + "'" + auth + "'," + "'" + auth + "'," + "'" + auth + "'," + "'" + 'afsfasdas' + "',"  + b + "," + b + "," + "'" + date + "');" + '"')
        f.write('\n')
