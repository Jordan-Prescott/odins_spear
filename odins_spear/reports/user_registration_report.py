import pandas as pd

def export_to_xlsx(data: dict, remove_null_entries: bool, group_id: str):
    rows = []

    for userId, deviceId in data.items():
        if deviceId:
            for deviceId, deviceDetails in deviceId.items():
                rows.append({
                    "UserID": userId,
                    "Lineport": deviceDetails.get("LinePort", ""),
                    "Device Name": deviceDetails.get("Device", ""),
                    "Registered": deviceDetails.get("Registered", "")
                })
        else:
            if remove_null_entries == False:
                rows.append({
                        "UserID": userId,
                        "Lineport": "N/A",
                        "Device Name": "N/A",
                        "Registered": "N/A"
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