import pandas as pd

def export_to_xlsx(data: dict):
    rows = []

    for userId, linePort in data.items():
        if linePort:
            for linePort, deviceDetails in linePort.items():
                rows.append({
                    "UserID": userId,
                    "Lineport": linePort,
                    "Device Name": deviceDetails.get("Device", ""),
                    "Registered": deviceDetails.get("Registered", "")
                })
        else:
            rows.append({
                    "UserID": userId,
                    "Lineport": "",
                    "Device Name": "",
                    "Registered": ""
                })

    dataframe = pd.DataFrame(rows)
    dataframe.to_excel("out.xlsx", index=False)