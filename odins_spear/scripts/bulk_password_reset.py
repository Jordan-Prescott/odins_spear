from ..exceptions import OSInvalidPasswordType


def main(
    api, service_provider_id: str, group_id: str, users: list, password_type: str
) -> list:
    # SIP auth password
    if password_type.lower() == "sip":
        print("Generating new SIP passwords.")
        new_passwords = api.password_generate.get_sip_passwords_generate(len(users))[
            "passwords"
        ]
        users_and_new_passwords = list(zip(users, new_passwords))

        print("Setting new SIP passwords.")
        for user in users_and_new_passwords:
            api.authentication.put_user_authentication_service(user[0], user[1])

        print("Setting new SIP passwords complete.")
        return [
            {"userId": user[0], "newPassword": user[1]}
            for user in users_and_new_passwords
        ]

    # intigration password
    elif password_type.lower() == "web":
        print("Generating new SIP passwords.")
        new_passwords = api.password_generate.get_passwords_generate(
            service_provider_id, group_id, len(users)
        )["passwords"]
        users_and_new_passwords = list(zip(users, new_passwords))

        print("Setting new SIP passwords.")
        for user in users_and_new_passwords:
            api.authentication.put_user_web_authentication_password(user[0], user[1])

        print("Setting new SIP passwords complete.")
        return [
            {"userId": user[0], "newPassword": user[1]}
            for user in users_and_new_passwords
        ]

    # voicemail/ portal
    elif password_type.lower() == "vm":
        print("Generating new voicemail passcodes.")
        new_passcodes = api.password_generate.get_passcodes_generate(
            service_provider_id, group_id, len(users)
        )["passcodes"]
        users_and_new_passcodes = list(zip(users, new_passcodes))

        print("Setting new voicemail passcodes.")
        for user in users_and_new_passcodes:
            api.users.put_user_portal_passcode(user[0], user[1])

        print("Setting new voicemail passcodes complete.")
        return [
            {"userId": user[0], "newPasscode": user[1]}
            for user in users_and_new_passcodes
        ]

    else:
        # raise error if user attempts to change another type of password.
        raise OSInvalidPasswordType
