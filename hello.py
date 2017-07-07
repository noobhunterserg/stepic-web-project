#!/usr/bin/env python
def application(env, start_response):
    # string = env
    # ind = string.index('?')
    # parsing_line=string[ind+1:]
    # spl = parsing_line.split('&')
    # body = '\n'.join(spl)
    body = '2'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

    return body
