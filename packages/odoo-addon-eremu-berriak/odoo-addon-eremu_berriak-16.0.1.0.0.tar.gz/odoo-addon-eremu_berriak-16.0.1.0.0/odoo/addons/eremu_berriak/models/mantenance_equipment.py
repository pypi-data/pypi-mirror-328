#Mantenu moduloko ekipoetan eremu berriak gehitzeko modulua

from odoo import models, fields, api

class  MaintenanceEquipement(models.Model):
    _inherit = 'maintenance.equipment'

    x_cpu = fields.Char(string="CPU")
    x_ram = fields.Char(string="RAM")
    x_lizentzia_gakoa = fields.Char(string="Lizentzia Gakoa")
    x_sistema_eragilea = fields.Char(string="Sistema Eragilea")

