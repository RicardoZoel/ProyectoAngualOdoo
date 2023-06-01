
from xml.dom import ValidationErr
from odoo import models, fields, api
from datetime import datetime, timedelta

class EntidadModel(models.Model):
    _name = 'hidro_isca_app.entidad_model'
    _description = 'Entidad model'

    name = fields.Char("Nombre de la empresa", required=True)
    direccion = fields.Char('Dirección:')
    poblacion = fields.Char('Poblacion')
    provincia = fields.Char('Provincia')

    contadores = fields.One2many("hidro_isca_app.contador_model", inverse_name="empresa",string="Contadores")

