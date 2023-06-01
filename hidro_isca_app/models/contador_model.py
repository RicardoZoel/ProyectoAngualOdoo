
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ContadorModel(models.Model):
    _name = 'hidro_isca_app.contador_model'
    _description = 'Contador model'
    name = fields.Char(string="Contador name ")
    usuario = fields.Many2one("hidro_isca_app.usuarios_model", "usuario", required=True)
    empresa = fields.Many2one("hidro_isca_app.entidad_model", "empresa", required=True)

    consumos_mensuales = fields.One2many("hidro_isca_app.consumo_model", inverse_name="contador",string="Consumos Mensuales")

    _sql_constraints = [
        ('contador_uniq', 'unique(name, usuario, empresa)', 'El contadoro ya existe.'),
    ]