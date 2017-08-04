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
    for i in range (1, 51):
        mysql_part3 = 'USE QA; INSERT qa_question(id, title, text, added_at, rating, author_id) VALUES'
        id_ = str(i)
        title = 'title' + str(i)
        text  = 'text' + str(i)
        added_at = '201' + str(random.randrange(1, 4)) + '-' + str(random.randrange(1, 10)) + '-' + str(random.randrange(11, 25))
        rating = str(random.randrange(10))
        author_id = str(random.randrange(1,6))
        f.write (mysql_part + '"' + mysql_part3 + "('" + id_ + "'," + "'" + title + "'," + "'" + text + "'," + "'" + added_at + "'," + "'" + rating + "'," + "'" + author_id + "');" + '"')
        f.write('\n')
    for i in range (1, 51):
        mysql_part4 = 'USE QA; INSERT qa_answer(text, added_at, question_id, author_id) VALUES'
        k = random.randrange(2,5)
        question_id = str(i)
        for z in range(1, k):
            text = 'answer' + str(z)
            author_id = str(random.randrange(1, 6))
            added_at = '201' + str(random.randrange(4,6)) + '-' + str(random.randrange(1, 10)) + '-' + str(random.randrange(11, 25))
            f.write (mysql_part + '"' + mysql_part4 + "('" + text + "'," + "'" + added_at + "'," + "'" + question_id + "'," + "'" + author_id + "');" + '"')
            f.write('\n')
