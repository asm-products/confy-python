import re

from .client import Client

def config(url={}):

    if type(url) is str:
        regex = re.compile('(https?:\/\/)(.*):(.*)@(.*)\/orgs\/([a-z0-9]*)\/projects\/([a-z0-9]*)\/envs\/([a-z0-9]*)\/config', re.I)
        matches = regex.match(url)

        url = {
            'host': matches.group(1) + matches.group(4), 'user': matches.group(2), 'pass': matches.group(3),
            'org': matches.group(5), 'project': matches.group(6), 'env': matches.group(7)
        }

    client = Client({
        'username': url['user'], 'password': url['pass']
    }, { 'base': url['host'] })

    return client.config(url['org'], url['project'], url['env']).retrieve().body
