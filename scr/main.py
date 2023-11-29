from flask import Flask, session 
from datetime import timedelta
from settings import HOST, PORT, DEBUG, TEMPO_SESSION
from flask import Flask, render_template
import os

# import blueprint criado
from mod_funcionario.funcionario import bp_funcionario
from mod_cliente.cliente import bp_cliente
from mod_index.index import bp_index
from mod_produto.produto import bp_produto
from mod_erro.erro import bp_erro #atv 11
from mod_login.login import bp_login #atv 17

app = Flask(__name__)

# gerando uma chave randômica para secret_key
app.secret_key = os.urandom(12).hex()

#renova tempo da sessão
@app.before_request
def before_request():
    session.permanent = True
    session['tempo'] = int(TEMPO_SESSION)
    #ta ta o padrão é 31 dias ok tendi
    app.permanent_session_lifetime = timedelta(minutes=session['tempo'])

# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_index)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_erro)#atv 11
app.register_blueprint(bp_login)#atv 17
#ajusta o SAMESITE
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE='True'
)




''' chamadas dos formulários '''
@app.route('/home')
def formIndex():
    return render_template('formIndex.html'), 200

@app.route('/funcionario/')
def formListaFuncionario():
    return render_template ('formListaFuncionario.html'), 200

@app.route('/cliente/')
def formListaCliente():
    return render_template('formListaCliente.html'), 200

@app.route('/produto/')
def formListaProduto():
    return render_template('formListaProduto.html'), 200

@app.route('/login')
def formLogin():
    return render_template('formLogin.html'), 200

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG) #tive  qcolocar 8001 pq a 5000 não tava indo :))))