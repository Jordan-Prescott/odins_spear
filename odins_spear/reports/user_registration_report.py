import pandas as pd

def export_to_xlsx(data: dict, remove_null_entries: bool, group_id: str):
    rows = []

    for user_id, devices in data.items():
        if not devices and not remove_null_entries:
            rows.append({
                "UserID": user_id,
                "Lineport": "N/A",
                "Device Name": "N/A",
                "Registered": "N/A"
            })
            continue

        device_items = devices.items() if devices else []

        for _, device_details in device_items:
            rows.append({
                "UserID": user_id,
                "Lineport": device_details.get("linePort", "N/A"),
                "Device Name": device_details.get("deviceName", "N/A"),
                "Registered": device_details.get("isRegistered", "N/A")
            })


    dataframe = pd.DataFrame(rows)
    dataframe.to_excel(f"./os_reports/Registration_report_for_{group_id}.xlsx", index=False)

def main(api, service_provider_id: str, group_id: str, remove_null_entries: bool):
    """Generates an Excel Worksheet deatiling each users device, lineport and registration status within a group.

        Args:
            service_provider_id (str):  Service Provider/ Enterprise where group is hosted.
            group_id (str): Target Group you would like to check the registration of.
            remove_null_entries (bool): If a user does not have a device endpoint assigned, setting this to true will remove them from the final Workbook.
        """
    data = api.scripter.user_registration(service_provider_id, group_id)

    export_to_xlsx(data, remove_null_entries, group_id)