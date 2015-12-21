Authentication for One Time Password (2 Factor Authentication)
==============================================================

This generic One Time Password (OTP) login module provides basic 
session and mechanism for OTP. This module allows for 2 Factor Authentication
(Related to 2 Step Verification)

The intent here is to increase security to your Odoo installation (in case users have weak passwords).
    
The auth_opt_base module provides the base mechanism for OTP  authentication
function overriding, user session, login management, timeout management, mutli connection, etc.
You have one function to override in a provider module. The function is check_otp.
This modules does not work on it's own. It requires a provider module.
The providor module lets you to write a provider for a specific OTP system. 
The original (V5) code had an example using the c2c_one_time_password_login_yubikey_provider module.
Now (V8) there is a new example for use with Google Authenticator (check out the
auth_google_authenticator module for an example on how to create a OTP provider, or 
feel free to use the Google Authenticator module exactly as is. Just install the app on your
mobile phone.

Configuration:
The OTP configuration is done on the company view, and on each user view.
The Company view allows for the module to be on for certain database companies and off for others.
The User view allows the setting of set the secret key for each user.

