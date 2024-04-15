import json

import odins_spear.utils.loggers as loggers
from odins_spear.exceptions import OSInvalidPasswordType

def main(api, service_provider_id: str, group_id: str, users: list, password_type: str):
    
    # SIP auth password
    if password_type.lower() == "sip":
        
        loggers.log_info("Generating new SIP passwords.")
        new_passwords = api.get.sip_passwords_generate(len(users))['passwords']
        users_and_new_passwords = list(zip(users, new_passwords))
        
        loggers.log_info("Setting new SIP passwords.")
        for user in users_and_new_passwords:
            api.put.user_authentication_service(user[0], user[1])
        
        loggers.log_info("Setting new SIP passwords complete.")
        formatted_user_and_new_passwords = [{"userId": user[0], "newPassword": user[1]} for user in users_and_new_passwords]
        return json.dumps(formatted_user_and_new_passwords)
    
    # intigration password
    elif password_type.lower() == "web":
        
        loggers.log_info("Generating new SIP passwords.")
        new_passwords = api.get.passwords_generate(service_provider_id, group_id, len(users))['passwords']
        users_and_new_passwords = list(zip(users, new_passwords))
        
        loggers.log_info("Setting new SIP passwords.")
        for user in users_and_new_passwords:
            api.put.user_web_authentication_password(user[0], user[1])
        
        loggers.log_info("Setting new SIP passwords complete.")
        formatted_user_and_new_passwords = [{"userId": user[0], "newPassword": user[1]} for user in users_and_new_passwords]
        return json.dumps(formatted_user_and_new_passwords)
    
    # voicemail/ oortal
    elif password_type.lower() == "vm": # voicemail
        
        loggers.log_info("Generating new voicemail passcodes.")
        new_passcodes = api.get.passcodes_generate(service_provider_id, group_id, len(users))['passcodes']
        users_and_new_passcodes = list(zip(users, new_passcodes))
        
        loggers.log_info("Setting new voicemail passcodes.")
        for user in users_and_new_passcodes:
            api.put.user_portal_passcode(user[0], user[1])
          
        loggers.log_info("Setting new voicemail passcodes complete.")    
        formatted_user_and_new_passcodes = [{"userId": user[0], "newPasscode": user[1]} for user in users_and_new_passcodes]
        return json.dumps(formatted_user_and_new_passcodes)
    
    # raise error if user attempts to change another type of password.
    else:
        raise OSInvalidPasswordType