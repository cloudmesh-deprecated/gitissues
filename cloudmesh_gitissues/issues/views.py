from __future__ import unicode_literals
from __future__ import print_function
from pprint import pprint
import json

from django.shortcuts import render
from cloudmesh_client.common.ConfigDict import ConfigDict
from cloudmesh_client.util import banner, path_expand


from ..views import dict_table, list_table
from ..GitPriority import GitPriority

def url(msg, link):
    print (locals())
    data = {
        'msg': msg,
        'link': link
    }
    return '<a href="{link}"> {msg} </a>'.format(**data)


def issue_list(request, cloud=None):

    git = GitPriority("cloudmesh", "client")
    git.get()

    order = git.order
    data = git.table(compact=False)
    return (list_table(request,
                       title="Cloudmesh Issues",
                       data=data,
                       location="cloudmesh/client",
                       order=order))


