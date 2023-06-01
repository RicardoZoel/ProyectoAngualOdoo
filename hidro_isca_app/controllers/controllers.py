# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import json,request


class HidoApp(http.Controller):

    ####################################GETS###########################################
    
    @http.route(['/hidro_isca_app/getUsuario',"/hidro_isca_app/getUsuario/<int:usuid>"], auth='public', type='http')
    def getUsuario(self, usuid=None, **kw):
        if usuid:
            domain=[("id","=", usuid)]
        else:
            domain=[]
        usudata=http.request.env["hidro_isca_app.usuarios_model"].sudo().search_read(domain,["name","apellido","nif","direccion","poblacion","provincia","cuenta_bancaria","telefono"])
        data={"status":200,
               "data":usudata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/hidro_isca_app/getEmpresa'], auth='public', type='http')
    def getEmpresa(self, **kw):
        
        domain=[("id","=", 1)]
        empresadata=http.request.env["hidro_isca_app.entidad_model"].sudo().search_read(domain,["name","direccion","poblacion","provincia"])
        data={"status":200,
               "data":empresadata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/hidro_isca_app/getAgua'], auth='public', type='http')
    def getAgua(self, usuid=1, **kw):
        
        domain=[("id","=", usuid)]
        aguadata=http.request.env["hidro_isca_app.agua_model"].sudo().search_read(domain,["valor_agua"])
        data={"status":200,
               "data":aguadata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/hidro_isca_app/getContadores',"/hidro_isca_app/getContadores/<int:contadorid>"], auth='public', type='http')
    def getContadores(self, contadorid=None, **kw):
        if contadorid:
            domain=[("id","=", contadorid)]
        else:
            domain=[]
        usudata=http.request.env["hidro_isca_app.contador_model"].sudo().search_read(domain,["id","name","usuario","empresa"])
        data={"status":200,
               "data":usudata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    
    @http.route(["/hidro_isca_app/getContadoresPorUsuario/<int:contadorid>"], auth='public', type='http')
    def getContadoresPorUsuario(self, contadorid=None, **kw):
        if contadorid:
            domain=[("usuario","=", contadorid)]
        else:
            domain=[]
        usudata=http.request.env["hidro_isca_app.contador_model"].sudo().search_read(domain,["id","name","usuario","empresa"])
        data={"status":200,
               "data":usudata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    
    @http.route(['/hidro_isca_app/getConsumos',"/hidro_isca_app/getConsumos/<int:consumoid>"], auth='public', type='http')
    def getConsumos(self, consumoid=None, **kw):
        if consumoid:
            domain=[("id","=", consumoid)]
        else:
            domain=[]
        usudata=http.request.env["hidro_isca_app.consumo_model"].sudo().search_read(domain,["id","mes","anyo","MCC","VPMCCT", "contador", "usuario", "empresa","agua"])
        data={"status":200,
               "data":usudata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/hidro_isca_app/getRecivos',"/hidro_isca_app/getRecivos/<int:recivoid>"], auth='public', type='http')
    def getRecivos(self, recivoid=None, **kw):
        if recivoid:
            domain=[("id","=", recivoid)]
        else:
            domain=[]
        usudata=http.request.env["hidro_isca_app.recivo_model"].sudo().search_read(domain,["id","periodo_trimestral","anyo","MCCT","VPMCCT", "usuario", "estado", "empresa"])
        data={"status":200,
               "data":usudata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    ###############################################################################
    
        
    @http.route('/hidro_isca_app/postUsuario', auth='public', type='json', method="POST")
    def addUsuario(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["hidro_isca_app.usuarios_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/hidro_isca_app/postContador', auth='public', type='json', method="POST")
    def addContador(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["hidro_isca_app.contador_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    @http.route('/hidro_isca_app/postConsumo', auth='public', type='json', method="POST")
    def addConsumo(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["hidro_isca_app.consumo_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    @http.route('/hidro_isca_app/postRecivo', auth='public', type='json', method="POST")
    def addRecivo(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["hidro_isca_app.recivo_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
        ###############################################################################3
    @http.route('/hidro_isca_app/putUsuario/<int:usuid>', auth='public', type='json', method="PUT")
    def updateUsuario(self, usuid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["hidro_isca_app.usuarios_model"].sudo().search([("id", "=", usuid)])
            result.write(response)
            data = {
                "status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = {
                "status": 404,
                "error": str(e)
            }
            return data

    @http.route('/hidro_isca_app/putEmpresa/', auth='public', type='json', method="PUT")
    def updateEmpresa(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["hidro_isca_app.entidad_model"].sudo().search([("id", "=", 1)])
            result.write(response)
            data = {
                "status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = {
                "status": 404,
                "error": str(e)
            }
            return data
    @http.route('/hidro_isca_app/putAgua/', auth='public', type='json', method="PUT")
    def updateAgua(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["hidro_isca_app.agua_model"].sudo().search([("id", "=", 1)])
            result.write(response)
            data = {
                "status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = {
                "status": 404,
                "error": str(e)
            }
            return data

    @http.route('/hidro_isca_app/putContador/<int:contadorid>', auth='public', type='json', method="PUT")
    def updateContador(self, contadorid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["hidro_isca_app.contador_model"].sudo().search([("id", "=", contadorid)])
            result.write(response)
            data = {
                "status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = {
                "status": 404,
                "error": str(e)
            }
            return data

        
    @http.route('/hidro_isca_app/putConsumo/<int:consumoid>', auth='public', type='json', method="PUT")
    def updateConsumo(self, consumoid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["hidro_isca_app.consumo_model"].sudo().search([("id", "=", consumoid)])
            result.write(response)
            data = {
                "status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = {
                "status": 404,
                "error": str(e)
            }
            return data

    
    http.route('/hidro_isca_app/putRecivos/<int:recivoid>', auth='public', type='json', method="PUT")
    def updateRecivo(self, recivoid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["hidro_isca_app.recivo_model"].sudo().search([("id", "=", recivoid)])
            result.write(response)
            data = {
                "status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = {
                "status": 404,
                "error": str(e)
            }
            return data
        ###############################################################################3

    
    
    

    

    @http.route('/hidro_isca_app/delContador', auth='public', type='json', method="DELETE")
    def delContador(self, **kw):
        contadorid = request.jsonrequest["id"]
        try:
            result=http.request.env["hidro_isca_app.contador_model"].sudo().search([("id", "=", contadorid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

        ###############################################################################