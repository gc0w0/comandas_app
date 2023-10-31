from flask import Blueprint, render_template
import requests
from settings import HEADERS_API, ENDPOINT_CLIENTE
bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''
@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    try:
        response = requests.get(ENDPOINT_CLIENTE, headers=HEADERS_API)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result[0])
        return render_template('formListaCliente.html', result=result[0])
    except Exception as e:
          return render_template('formListaCliente.html', msgErro=e.args[0])

   
@bp_cliente.route('/form-cliente', methods=['GET', 'POST'])
def formCliente():
    return render_template('formCliente.html'), 200
'''
Rota antiga de app...
@app.route('/cliente/')
def formListaCliente():
    # return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
    return render_template('formListaCliente.html'), 200
'''