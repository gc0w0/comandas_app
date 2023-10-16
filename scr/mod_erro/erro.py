from flask import Blueprint, render_template
#tem q fazer a referencia dentro da main no caso os END point (eu acho kkkk)
bp_erro = Blueprint('erro', __name__,
template_folder='templates')

@bp_erro.app_errorhandler(404)
def erro404(error):
    return render_template("form404.html", erroHttp=error)

@bp_erro.app_errorhandler(405)
def erro405(error):
    return render_template("form405.html", erroHttp=error)

@bp_erro.app_errorhandler(500)
def erro500(error):
    return render_template("form500.html", erroHttp=error)
