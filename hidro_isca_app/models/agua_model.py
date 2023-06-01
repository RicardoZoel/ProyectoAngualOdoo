
from xml.dom import ValidationErr
from odoo import models, fields, api
from datetime import datetime, timedelta

class AguaModel(models.Model):
    _name = 'hidro_isca_app.agua_model'
    _description = 'Agua model'
    
    valor_agua=fields.Float('Valor agua')
    valor_agua_with_euro = fields.Char(string="Valor agua con €", compute="_compute_valor_agua_with_euro")

    @api.depends('valor_agua')
    def _compute_valor_agua_with_euro(self):
        for record in self:
            record.valor_agua_with_euro = f"{record.valor_agua}€"