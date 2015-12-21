#
#  login.py
#
#  Created by Nicolas Bessi
#  Copyright (c) 2010 CamptoCamp. All rights reserved.
#
from service import security
from openerp import models,fields,api
import netsvc
import pooler
import tools
import datetime


#Function to override
def check_otp(otp, user, res_user_obj):
    """Validate OTP"""
    #Your stuff here
    print "here the OTP is check for value ",otp,"but the service model is not done"
    #end of your stuff
    res_user_obj._loginsession[user.id][otp] = datetime.datetime.now()
    return user.id


def check_otp_timeout(otp, user, res_user_obj):
    """Check the OTP time to live"""
    if res_user_obj._loginsession[user.id].has_key(otp):
        delta =  datetime.datetime.now() - res_user_obj._loginsession[user.id][otp]
        if delta.seconds <  res_user_obj._otp_ttl :
            return 'valid'
        else :
            try:
                del(res_user_obj._loginsession[user.id][otp])
            except Exception, e:
                pass #we pass
            print 'OTP expired'
            return False
    else :
        return True
    
    
def handle_login_session(user, res_user_obj):
    """Ensure that the login session in initialized"""
    if not res_user_obj._loginsession.has_key(user.id) :
        res_user_obj._loginsession[user.id] = {}
    #we remove deprecated password 
    if len(res_user_obj._loginsession[user.id]) < 2 :
        return
    todel = []    
    for otp in res_user_obj._loginsession[user.id] :
        delta = datetime.datetime.now() - res_user_obj._loginsession[user.id][otp]
        if delta.seconds >  res_user_obj._otp_ttl :
            todel.append(otp)
    for key in todel :
        try:
            del(res_user_obj._loginsession[user.id][key]) 
        except Exception, e:
            pass #we pass
            
        
        

def auth(db, identifier, password, mode='login'):
    """Do the General OTP autentification stuff"""
    if not password:
        return False
    passes = password.split('--otpsep--')
    password = passes[0]
    if len(passes) > 1:
        otp = passes[1]
    else :
        return False
    pool = pooler.get_pool(db)
    res_user_obj =pool.get('res.users')
    user_id = identifier
    cr = pooler.get_db(db).cursor()  
    if mode == 'login' :
        cr.execute('select id from res_users where login=%s and password=%s and active', (tools.ustr(identifier), tools.ustr(password)))
        res = cr.fetchone()
        if res:
            user_id = res[0]
        else:
            return False
    # import pdb
    # pdb.set_trace()
    user = res_user_obj.browse(cr, user_id, user_id)
    if user.company_id.otp_active :
        handle_login_session(user, res_user_obj)
        timeoutcheck = check_otp_timeout(otp, user, res_user_obj) 
        if not check_otp_timeout(otp, user, res_user_obj) :
            return False
        if timeoutcheck == 'valid' :
            return user_id
        return  check_otp(otp, user, res_user_obj )
    else :
        return user_id


## @param db the name of the db
## @param login the login (utf string)
## @param password the login (utf string)
## @return the user id or false
def login(db, login, password):
    """Override of the security.login function in order to
    loging using ldap if enable in company else
    using the calssic loging"""
    res = auth(db, login, password)
    return res
    
## @param db the name of the db
## @param uid 'res.users' id
## @param password the login (utf string)
## @return the True if user as access else False
def check(db, uid, passwd):
    """Override of the security.check function in order to
    loging using ldap if enable in company else
    using the calssic loging"""
    print 'check'
    if security._uid_cache.has_key(uid) and (security._uid_cache[uid]==passwd):
        return True
        
    res = auth(db, uid, passwd, mode='id')
    if not res:
        raise Exception('AccessDenied')
    if res:
        security._uid_cache[uid] = passwd
    return bool(res)

## @param db the name of the db
## @param uid 'res.users' id
## @param password the login (utf string)
## @return the True if user as access else False
def access(db, uid, passwd, sec_level, ids):
    """Override of the security.access function in order to
    loging using ldap if enable in company else
    using the calssic loging"""
    res = auth(db, uid, passwd, mode='id')
    if not res:
        raise Exception('Bad username or password')
    return res

security.login=login
security.check=check
security.access=access
