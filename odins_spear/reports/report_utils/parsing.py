from ...store import broadwork_entities as bre
from .report_entities import external_number

# nodes needed for graph generation
NODES = []
MAX_LEVEL = 30


def call_flow_module(node: object, data_store: object):
    # create mapping for easier searchability when gathering nodes
    data_store.build_number_mapping()

    # traverses the enities that forward to eachother and adds all to NODES
    _traverse_connecting_entities(node, data_store)

    return NODES


def _traverse_connecting_entities(entity: object, data_store: object, visited=None):
    if visited is None:
        visited = []

    if entity in visited:
        return
    else:
        visited.append(entity)

    try:
        if isinstance(entity, bre.User):
            # Checks to see if the number is external first and creates external number object for parsing later
            if (
                data_store.number_mapping.get(entity.call_forwarding_always) == None
                and len(str(entity.call_forwarding_always)) >= 3
                and str(entity.call_forwarding_always)[2].isdigit()
            ):
                entity.call_forwarding_always = external_number(
                    str(entity.call_forwarding_always)
                )
            else:
                entity.call_forwarding_always = data_store.number_mapping.get(
                    entity.call_forwarding_always
                )
                if (
                    entity.call_forwarding_always
                    and entity.call_forwarding_always not in visited
                ):
                    _traverse_connecting_entities(
                        entity.call_forwarding_always, data_store, visited
                    )

            if (
                data_store.number_mapping.get(entity.call_forwarding_busy) == None
                and len(str(entity.call_forwarding_busy)) >= 3
                and str(entity.call_forwarding_busy)[2].isdigit()
            ):
                entity.call_forwarding_busy = external_number(
                    str(entity.call_forwarding_busy)
                )
            else:
                entity.call_forwarding_busy = data_store.number_mapping.get(
                    entity.call_forwarding_busy
                )
                if (
                    entity.call_forwarding_busy
                    and entity.call_forwarding_busy not in visited
                ):
                    _traverse_connecting_entities(
                        entity.call_forwarding_busy, data_store, visited
                    )

            if (
                data_store.number_mapping.get(entity.call_forwarding_no_answer) == None
                and len(str(entity.call_forwarding_no_answer)) >= 3
                and str(entity.call_forwarding_no_answer)[2].isdigit()
            ):
                entity.call_forwarding_no_answer = external_number(
                    str(entity.call_forwarding_no_answer)
                )
            else:
                entity.call_forwarding_no_answer = data_store.number_mapping.get(
                    entity.call_forwarding_no_answer
                )
                if (
                    entity.call_forwarding_no_answer
                    and entity.call_forwarding_no_answer not in visited
                ):
                    _traverse_connecting_entities(
                        entity.call_forwarding_no_answer, data_store, visited
                    )

            if (
                data_store.number_mapping.get(entity.call_forwarding_not_reachable)
                == None
                and len(str(entity.call_forwarding_not_reachable)) >= 3
                and str(entity.call_forwarding_not_reachable)[2].isdigit()
            ):
                entity.call_forwarding_not_reachable = external_number(
                    str(entity.call_forwarding_not_reachable)
                )
            else:
                entity.call_forwarding_not_reachable = data_store.number_mapping.get(
                    entity.call_forwarding_not_reachable
                )
                if (
                    entity.call_forwarding_not_reachable
                    and entity.call_forwarding_not_reachable not in visited
                ):
                    _traverse_connecting_entities(
                        entity.call_forwarding_not_reachable, data_store, visited
                    )

        if isinstance(entity, bre.CallCenter):
            if entity.bounced_calls_enabled:
                # Checks to see if the number is external first and creates external number object for parsing later
                if (
                    data_store.number_mapping.get(
                        str(entity.bounced_calls_transfer_to_phone_number)
                    )
                    == None
                    and len(str(entity.bounced_calls_transfer_to_phone_number)) >= 3
                    and str(entity.bounced_calls_transfer_to_phone_number)[2].isdigit()
                ):
                    entity.bounced_calls_transfer_to_phone_number = external_number(
                        str(entity.bounced_calls_transfer_to_phone_number)
                    )
                else:
                    entity.bounced_calls_transfer_to_phone_number = (
                        data_store.number_mapping.get(
                            str(entity.bounced_calls_transfer_to_phone_number)
                        )
                    )
                    if (
                        entity.bounced_calls_transfer_to_phone_number
                        and entity.bounced_calls_transfer_to_phone_number not in visited
                    ):
                        _traverse_connecting_entities(
                            entity.bounced_calls_transfer_to_phone_number,
                            data_store,
                            visited,
                        )

            if entity.overflow_calls_action:
                if (
                    data_store.number_mapping.get(
                        str(entity.overflow_calls_transfer_to_phone_number)
                    )
                    == None
                    and len(str(entity.overflow_calls_transfer_to_phone_number)) >= 3
                    and str(entity.overflow_calls_transfer_to_phone_number)[2].isdigit()
                ):
                    entity.overflow_calls_transfer_to_phone_number = external_number(
                        str(entity.overflow_calls_transfer_to_phone_number)
                    )
                else:
                    entity.overflow_calls_transfer_to_phone_number = (
                        data_store.number_mapping.get(
                            str(entity.overflow_calls_transfer_to_phone_number)
                        )
                    )
                    if (
                        entity.overflow_calls_transfer_to_phone_number
                        and entity.overflow_calls_transfer_to_phone_number
                        not in visited
                    ):
                        _traverse_connecting_entities(
                            entity.overflow_calls_transfer_to_phone_number,
                            data_store,
                            visited,
                        )

            if entity.stranded_calls_action:
                if (
                    data_store.number_mapping.get(
                        str(entity.stranded_calls_transfer_to_phone_number)
                    )
                    == None
                    and len(str(entity.stranded_calls_transfer_to_phone_number)) >= 3
                    and str(entity.stranded_calls_transfer_to_phone_number)[2].isdigit()
                ):
                    entity.stranded_calls_transfer_to_phone_number = external_number(
                        str(entity.stranded_calls_transfer_to_phone_number)
                    )
                else:
                    entity.stranded_calls_transfer_to_phone_number = (
                        data_store.number_mapping.get(
                            str(entity.stranded_calls_transfer_to_phone_number)
                        )
                    )
                    if (
                        entity.stranded_calls_transfer_to_phone_number
                        and entity.stranded_calls_transfer_to_phone_number
                        not in visited
                    ):
                        _traverse_connecting_entities(
                            entity.stranded_calls_transfer_to_phone_number,
                            data_store,
                            visited,
                        )

            if entity.stranded_call_unavailable_action:
                if (
                    data_store.number_mapping.get(
                        str(entity.stranded_call_unavailable_transfer_to_phone_number)
                    )
                    == None
                    and len(
                        str(entity.stranded_call_unavailable_transfer_to_phone_number)
                    )
                    >= 3
                    and str(entity.stranded_call_unavailable_transfer_to_phone_number)[
                        2
                    ].isdigit()
                ):
                    entity.stranded_call_unavailable_transfer_to_phone_number = external_number(
                        str(entity.stranded_call_unavailable_transfer_to_phone_number)
                    )
                else:
                    entity.stranded_call_unavailable_transfer_to_phone_number = data_store.number_mapping.get(
                        str(entity.stranded_call_unavailable_transfer_to_phone_number)
                    )
                    if (
                        entity.stranded_call_unavailable_transfer_to_phone_number
                        and entity.stranded_call_unavailable_transfer_to_phone_number
                        not in visited
                    ):
                        _traverse_connecting_entities(
                            entity.stranded_call_unavailable_transfer_to_phone_number,
                            data_store,
                            visited,
                        )

        if isinstance(entity, bre.HuntGroup):
            if entity.forward_after_timeout_enabled:
                if (
                    data_store.number_mapping.get(
                        entity.no_answer_forward_to_phone_number
                    )
                    is None
                    and len(str(entity.no_answer_forward_to_phone_number)) >= 4
                    and str(entity.no_answer_forward_to_phone_number)[2].isdigit()
                ):
                    entity.no_answer_forward_to_phone_number = external_number(
                        str(entity.no_answer_forward_to_phone_number)
                    )
                else:
                    entity.no_answer_forward_to_phone_number = (
                        data_store.number_mapping.get(
                            str(entity.no_answer_forward_to_phone_number)
                        )
                    )
                    if (
                        entity.no_answer_forward_to_phone_number
                        and entity.no_answer_forward_to_phone_number not in visited
                    ):
                        _traverse_connecting_entities(
                            entity.no_answer_forward_to_phone_number,
                            data_store,
                            visited,
                        )

            if entity.call_forward_not_reachable_enabled:
                if (
                    data_store.number_mapping.get(
                        str(entity.call_forward_not_reachable_transfer_to_phone_number)
                    )
                    == None
                    and len(
                        str(entity.call_forward_not_reachable_transfer_to_phone_number)
                    )
                    >= 3
                    and str(entity.call_forward_not_reachable_transfer_to_phone_number)[
                        2
                    ].isdigit()
                ):
                    entity.call_forward_not_reachable_transfer_to_phone_number = external_number(
                        str(entity.call_forward_not_reachable_transfer_to_phone_number)
                    )
                else:
                    entity.call_forward_not_reachable_transfer_to_phone_number = data_store.number_mapping.get(
                        str(entity.call_forward_not_reachable_transfer_to_phone_number)
                    )
                    if (
                        entity.call_forward_not_reachable_transfer_to_phone_number
                        and entity.call_forward_not_reachable_transfer_to_phone_number
                        not in visited
                    ):
                        _traverse_connecting_entities(
                            entity.call_forward_not_reachable_transfer_to_phone_number,
                            data_store,
                            visited,
                        )

        if isinstance(entity, bre.AutoAttendant):
            for key in entity.business_hours_menu.keys:
                if "Transfer" in key.action:
                    if (
                        data_store.number_mapping.get(str(key.phone_number)) == None
                        and len(str(key.phone_number)) >= 3
                        and str(key.phone_number)[2].isdigit()
                    ):
                        key.phone_number = external_number(str(key.phone_number))
                    else:
                        key.phone_number = data_store.number_mapping.get(
                            str(key.phone_number)
                        )
                        if key.phone_number and key.phone_number not in visited:
                            _traverse_connecting_entities(
                                key.phone_number, data_store, visited
                            )

            for key in entity.after_hours_menu.keys:
                if "Transfer" in key.action:
                    if (
                        data_store.number_mapping.get(str(key.phone_number)) == None
                        and len(str(key.phone_number)) >= 3
                        and str(key.phone_number)[2].isdigit()
                    ):
                        key.phone_number = external_number(str(key.phone_number))
                    else:
                        key.phone_number = data_store.number_mapping.get(
                            str(key.phone_number)
                        )
                        if key.phone_number and key.phone_number not in visited:
                            _traverse_connecting_entities(
                                key.phone_number, data_store, visited
                            )
    except TypeError:
        # this object is further up the tree and a loop has occured - Move one and come back
        pass

    NODES.append(entity)  # Append outside of the if condition
