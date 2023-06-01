
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConsumModel(models.Model):
    _name = 'hidro_isca_app.consumo_model'
    _description = 'Consum model'

    mes = fields.Selection(
        string="Mes",
        selection=[('1','Enero'),('2','Febrero'),('3',('Marzo')),
                   ('4','Abril'),('5','Mayo'),('6',('Junio')),
                   ('7','Julio'),('8','Agosto'),('9',('Septiembre')),
                   ('10','Octubre'),('11','Nobiembre'),('12','Diciembre')],
        default="1",
    required=True)
    anyo = fields.Integer("Año", required=True)

    @api.constrains('anyo')
    def _check_anyo(self):
        for record in self:
            if len(str(record.anyo)) != 4:
                raise ValidationError('El año debe ser un número de 4 dígitos.')
    MCC = fields.Integer("Metros cúbicos consumidos del contador del usuario", required=True)
    VPMCCT = fields.Char('Valor por metros cúbicos consumidos total del contador del usuario:' , compute="_compute_valor_VPMCCT", store=True)
    usuario = fields.Many2one("hidro_isca_app.usuarios_model", "usuario", required=True)
    empresa = fields.Many2one('hidro_isca_app.entidad_model', 'empresa', default=lambda self: self.env['hidro_isca_app.entidad_model'].search([], limit=1))
    contador = fields.Many2one("hidro_isca_app.contador_model", "contador", required=True)
    agua = fields.Many2one('hidro_isca_app.agua_model', 'Agua', default=lambda self: self.env['hidro_isca_app.agua_model'].search([], limit=1))
    _sql_constraints = [
        ('consum_uniq', 'unique(mes, anyo, usuario, contador)', 'El consumo ya existe para este mes, contador y usuario.'),
    ]
    @api.depends('MCC')
    def _compute_valor_VPMCCT(self):
        for record in self:
            calculo = self.MCC * record.agua.valor_agua
            record.VPMCCT = "{}€".format(calculo)