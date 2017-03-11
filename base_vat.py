# -*- coding: utf-8 -*-
from openerp import models, fields, api
import re

class res_partner(models.Model):
    _inherit = 'res.partner'

    def check_vat_cl(self, vat):
        body, vdig = '', ''
        if vat == '555555555':
            return True
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
