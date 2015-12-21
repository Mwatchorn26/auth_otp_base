#
#  company.py
#
#  Created by Nicolas Bessi
#  Modified by Michael Watchorn
#  Copyright (c) 2015 CamptoCamp & Transformix Engineering Inc. All rights reserved.
#
from openerp import models, fields, api

class ResCompany(models.Model):
    """override the company in order to add OTP functionality to companies on demand (not all)"""
    _inherit = 'res.company'
    _columns = {
        'otp_active' =  fields.Boolean(string='OTP active'),     
    }
ResCompany()
