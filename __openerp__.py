#
#  __terp__.py
#
#  Created by Nicolas Bessi (c2c_one_time_password_login OpenERP V5)
#  Modified by Michael Watchorn (auth_otp_base Odoo V8)
#  Copyright (c) 2015 CamptoCamp & Transformix Engineering Inc.
#  All rights reserved.
#
{
    "name" : "auth_otp_base",
    "version" : "1.0",
    "description":""" Generic One Time Password (OTP) login module that provides basic 
    session and mechanism for OTP. This module allows for 2 Factor Authentication
     (Related to 2 Step Verification)
    

    The auth_opt_base module provides the base mechanism for OTP like authentication
    function overriding, user session, login management, timeout management, mutli connection, etc.
    You have one function to override in a provider module. The function is check_otp.
    This modules does not work on it's own. It requires a provider module.
    The providor module lets you to write a provider for a specific OTP system 
    You have a sample in the c2c_one_time_password_login_yubikey_provider module.
    The OTP configuration is done on the company view. Please see the help in the form. 
    
        """,
    "category" : "security",

    "depends" : [
                    "base", 
                ],
    "author" : "Camptocamp SA & Transformix Engineering Inc.",
    "init_xml" : [],
    "update_xml" : [
                        "user_view.xml",
                        "company_view.xml"
                    ],
    "installable" : True,
    "active" : False,
}
