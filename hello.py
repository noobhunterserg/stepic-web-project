#!/usr/bin/env python
def application(env, start_response):
    string = env['QUERY_STRING']
    spl = string.split('&')
    body = '\n'.join(spl)

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

    return body
