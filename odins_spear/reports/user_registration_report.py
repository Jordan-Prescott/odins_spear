import pandas as pd


def export_to_xlsx(data: dict, group_id: str):
    rows = []
    print("Start.\n")
    print("Generating report.\n")

    for user_id, user_data in data.items():
        registration = user_data.get("registration", {})

        if not registration:
            rows.append([user_id, None, None, False])
        else:
            for device_name, registration_info in registration.items():
                rows.append(
                    [
                        user_id,
                        registration_info.get("deviceName", device_name),
                        registration_info.get("linePort"),
                        registration_info.get("registered", False),
                    ]
                )

    dataframe = pd.DataFrame(
        rows, columns=["User ID", "Device Name", "Line Port", "Registered"]
    )
    dataframe.to_excel(
        f"./os_reports/Registration_report_for_{group_id}.xlsx",
        index=False,
    )
    print("End.\n")


def main(api, service_provider_id: str, group_id: str):
    """Generates an Excel Worksheet detailing each Users ID, device name and registration status within a group.

    Args:
        service_provider_id (str):  Service Provider/ Enterprise where group is hosted.
        group_id (str): Target Group you would like to check the registration of.

    Returns:
            Xlsx File into .os_reports/ named "Registration_report_for_(GroupID)"
    """
    data = api.scripter.user_registration(service_provider_id, group_id)

    export_to_xlsx(data, group_id)
