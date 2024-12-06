import re


def find_entity_with_number_type(
    number: str, number_type: str, broadwork_entities: list
):
    """
    Finds the phone number, extension, or alias in list of broadwork entities
    and returns that entity once found.

    Args:
        number (str): Target number looking for e.g. +1-123456789 or alias 0
        number_type (str): Number type of either phone number, extenion, or alias
        broadwork_entities (list): List of broadwork entities number can be assigned to

    Returns:
        object: Broadwork entity where number is assigned.
    """

    for entity in broadwork_entities:
        try:
            if number_type == "dn" and number in entity.phone_number:
                return entity
            elif number_type == "extension" and number in entity.extension:
                return entity
            elif number_type == "alias":
                for alias in entity.aliases:
                    if re.search(rf"\b{re.escape(alias)}\b", number):
                        return entity
        except TypeError:
            # issue when entity does not have a number, extenion, or alias assigned
            continue
    return None
