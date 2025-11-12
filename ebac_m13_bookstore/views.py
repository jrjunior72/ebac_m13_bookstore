import os
import subprocess
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_server(request):
    """Atualiza o código no PythonAnywhere via webhook do GitHub"""
    if request.method in ["POST", "GET"]:
        try:
            project_path = '/home/ricardoferreirajr/ebac_m13_bookstore'
            
            # Debug: verifique se o diretório existe
            if not os.path.exists(project_path):
                return HttpResponse(f"❌ Diretório não existe: {project_path}", status=500)
            
            # Execute os comandos git
            commands = [
                ['git', 'fetch', 'origin'],
                ['git', 'reset', '--hard', 'origin/main'],
            ]
            
            results = []
            for cmd in commands:
                result = subprocess.run(
                    cmd, 
                    capture_output=True, 
                    text=True,
                    cwd=project_path
                )
                results.append({
                    'command': ' '.join(cmd),
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                    'returncode': result.returncode
                })
            
            # Debug: mostre todos os resultados
            debug_output = "<br>".join([
                f"Comando: {r['command']}<br>"
                f"Return: {r['returncode']}<br>"
                f"Stdout: {r['stdout']}<br>"
                f"Stderr: {r['stderr']}<br>"
                f"---<br>"
                for r in results
            ])
            
            # Verifique se algum comando falhou
            for result in results:
                if result['returncode'] != 0:
                    return HttpResponse(f"❌ Erro no git:<br>{debug_output}", status=500)
            
            # Recarrega o WSGI
            wsgi_result = os.system("touch /var/www/ricardoferreirajr_pythonanywhere_com_wsgi.py")
            
            return HttpResponse(f"✅ Código atualizado com sucesso!<br>{debug_output}<br>WSGI touch: {wsgi_result}")
                
        except Exception as e:
            import traceback
            error_details = f"Exception: {str(e)}<br>Traceback: {traceback.format_exc()}"
            return HttpResponse(f"❌ Erro na atualização:<br>{error_details}", status=500)
    
    return HttpResponse("Método não permitido", status=405)

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())