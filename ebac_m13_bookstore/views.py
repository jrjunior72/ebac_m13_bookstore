import os
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update_server(request):
    """Atualiza o código no PythonAnywhere via webhook do GitHub"""
    if request.method in ["POST", "GET"]:
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo('/home/ricardoferreirajr/ebac_m13_bookstore')
        origin = repo.remotes.origin

        origin.pull()
        # força reload do WSGI (sem precisar acessar painel manualmente)
        os.system("touch /var/www/ricardoferreirajr_pythonanywhere_com_wsgi.py")
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere", status=405)


def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())