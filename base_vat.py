# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import re
from openerp.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat')
    def _rut_unique(self):
        partner = self.env['res.partner'].search([('vat','=',self.vat),('id','!=', self.id)])
        if self.vat !="CL555555555" and partner:
            raise UserError(_('El rut debe ser único'))
            return False

    def check_vat_cl(self, vat):
        body, vdig = '', ''
        if len(vat) != 9:
            return False
        else:
            body, vdig = vat[:-1], vat[-1].upper()
        try:
            vali = range(2,8) + [2,3]
            operar = '0123456789K0'[11 - (
                sum([int(digit)*factor for digit, factor in zip(
                    body[::-1],vali)]) % 11)]
            if operar == vdig:
                return True
            else:
                return False
        except IndexError:
            return False
