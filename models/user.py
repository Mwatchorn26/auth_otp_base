#
#  user.py
#
#  Created by Nicolas Bessi (OpenERP V5)
#  Modified by Michael Watchorn (Odoo V8)
#  Copyright (c) 2010 CamptoCamp & Transformix Engineering Inc.
#   All rights reserved.
#
from openerp import models, fields, api

class ResUSers(models.Model):
    """override the user classto add the private/secret key """
    ## login session
    _loginsession = {}
    ##OTP time to live (may not be applicable to your provider)
    _otp_ttl = 300 #sec
    _inherit = 'res.users'
    _columns = {
        ##otp sercet key of user
        'otp_key' =  fields.Char(
                                        'OTP key', 
                                        size=128, 
                                        help="This is the OTP secret (private) key"
                                    ),
        'otp_show' = fields.Boolean(
                                        string='Show characters'
                                    ),
 }
ResUSers()
