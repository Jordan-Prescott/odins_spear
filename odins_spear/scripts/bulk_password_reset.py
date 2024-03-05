import json

import odins_spear.logger as logger


def main(api, service_provider_id: str, group_id: str, users: list, password_type: str):
    
    # define which type of password/ passcode to reset
    if password_type == "SIP":
        
        logger.log_info("Generating new SIP passwords.")
        new_passwords = api.get.passwords_generate(service_provider_id, group_id, len(users))['passwords']
        users_and_new_passwords = list(zip(users, new_passwords))
        
        logger.log_info("Setting new SIP passwords.")
        for user in users_and_new_passwords:
            api.put.user_authentication_service(user[0], user[1])
            
        return json.dumps(dict(users_and_new_passwords))

    else: # voicemail
        
        logger.log_info("Generating new voicemail passcodes.")
        new_passcodes = api.get.passcodes_generate(service_provider_id, group_id, len(users))['passwords']
        users_and_new_passcodes = list(zip(users, new_passcodes))
        
        logger.log_info("Setting new voicemail passcodes.")
        for user in users_and_new_passcodes:
            api.put.user_portal_passcode(user[0], user[1])
            
        return json.dumps(dict(users_and_new_passcodes))