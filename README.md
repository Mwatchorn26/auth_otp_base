Authentication for One Time Password (2 Factor Authentication)
==============================================================

One Time Passwords are different for every time you log in. Hence they are only valid one-time. Technically some methods (like the Google Authenticator) are valid for a short fixed amount of time (generally 1 minute). Technically this is still a "something you know" not a "something you have"

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

2 Factor Authentication vs 2 Step Verfication
=============================================
This One Time Password module requires the user to enter the OTP at the same time as the users memorized password is entered. It is not requested after the submission of the memorized password, and (although that's a simplified reason) that is why it is not 2 steps. It does however introduce a new factor, so it is 2 factor Authentication. What would be even better is if the mobile device was used completely independently of the webpage sign-in (for another day!).
