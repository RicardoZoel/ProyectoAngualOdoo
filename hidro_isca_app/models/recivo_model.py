
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RecivoModel(models.Model):
    _name = 'hidro_isca_app.recivo_model'
    _description = 'Recivo model'

    periodo_trimestral = fields.Selection(
        string="Trimestres",
        selection=[('1','Enero/Febrero/Marzo'),('2','Abril/Mayo/Junio'),('3',('Julio/Agosto/Septiembre')),('4','Octubre/Noviembre/Diciembre')],
        default="1"
    )
    anyo = fields.Integer("Año", required=True)

    @api.constrains('anyo')
    def _check_anyo(self):
        for record in self:
            if len(str(record.anyo)) != 4:
                raise ValidationError('El año debe ser un número de 4 dígitos.')
                
    MCCT = fields.Integer("Metros cúbicos consumidos del contador del usuario", compute="_compute_valor_MCCT", store=True)
    VPMCCT = fields.Char('Valor por metros cúbicos consumidos total del contador del usuario:', compute="_compute_valor_MCCT", store=True)
    usuario = fields.Many2one("hidro_isca_app.usuarios_model", "usuario")
    estado = fields.Selection(
        string="Estado",
        selection=[('1','Pendiente'),('2','Pagado')],
        default="1"
    )
    _sql_constraints = [
        ('consum_uniq', 'unique(periodo_trimestral, anyo, usuario)', 'El recivo ya existe para este trimestre y usuario.'),
    ]
    empresa = fields.Many2one('hidro_isca_app.entidad_model', 'empresa', default=lambda self: self.env['hidro_isca_app.entidad_model'].search([], limit=1))
    @api.depends('periodo_trimestral','anyo','usuario')
    def _compute_valor_MCCT(self):
        for record in self:
            calculoMCCT = 0
            calculoVPMCCT=0
            for consumos in record.usuario.consumos_mensuales:
                if consumos.anyo==self.anyo:
                    if self.periodo_trimestral=='1':
                        if consumos.mes=='1' or consumos.mes=='2' or consumos.mes=='3':
                            calculoMCCT +=consumos.MCC
                            calculoVPMCCT+=float(consumos.VPMCCT[:-1])
                    elif self.periodo_trimestral=='2':
                        if consumos.mes=='4' or consumos.mes=='5' or consumos.mes=='6':
                            calculoMCCT +=consumos.MCC
                            calculoVPMCCT+=float(consumos.VPMCCT[:-1])
                    elif self.periodo_trimestral=='3':
                        if consumos.mes=='7' or consumos.mes=='8'or consumos.mes=='9':
                            calculoMCCT +=consumos.MCC
                            calculoVPMCCT+=float(consumos.VPMCCT[:-1])
                    elif self.periodo_trimestral=='4':
                        if consumos.mes=='10' or consumos.mes=='11' or consumos.mes=='12':
                            calculoMCCT +=consumos.MCC
                            calculoVPMCCT+=float(consumos.VPMCCT[:-1])
            self.MCCT=calculoMCCT
            self.VPMCCT = "{}€".format(calculoVPMCCT)