import re
from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class UsuariosModel(models.Model):
    _name = 'hidro_isca_app.usuarios_model'
    _description = 'Usuarios model'

    name = fields.Char("Nombre del usuario", required=True)
    apellido = fields.Char("Apellido del usuario", required=True)
    nif = fields.Char("Nif del usuario", required=True)
    direccion = fields.Char('Dirección:')
    poblacion = fields.Char('Poblacion')
    provincia = fields.Char('Provincia')
    cuenta_bancaria=fields.Char('Cuenta bancaria', required=True)
    telefono=fields.Integer('Telefono de contato')

    consumos_mensuales = fields.One2many("hidro_isca_app.consumo_model", inverse_name="usuario",string="Consumos Mensuales")

    recivos = fields.One2many("hidro_isca_app.recivo_model", inverse_name="usuario",string="Recivos Trimestrales")

    contadores = fields.One2many("hidro_isca_app.contador_model", inverse_name="usuario",string="Contadores")
 
    @api.constrains('cuenta_bancaria')
    def _validate_cuenta_bancaria(self):
        for partner in self:
            if partner.cuenta_bancaria:
                cuenta_bancaria = re.sub(r'\s|-', '', partner.cuenta_bancaria)
                if len(cuenta_bancaria) != 24:
                    raise ValidationError("El número de cuenta bancaria debe tener 24 dígitos.")
                if not cuenta_bancaria.startswith('ES'):
                    raise ValidationError("El número de cuenta bancaria debe comenzar con ES (para España).")
                iban = cuenta_bancaria[4:] + cuenta_bancaria[:4]
                iban = iban.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15').replace('G', '16').replace('H', '17').replace('I', '18').replace('J', '19').replace('K', '20').replace('L', '21').replace('M', '22').replace('N', '23').replace('O', '24').replace('P', '25').replace('Q', '26').replace('R', '27').replace('S', '28').replace('T', '29').replace('U', '30').replace('V', '31').replace('W', '32').replace('X', '33').replace('Y', '34').replace('Z', '35')
                if int(iban) % 97 != 1:
                    raise ValidationError("El número de cuenta bancaria no es válido.")