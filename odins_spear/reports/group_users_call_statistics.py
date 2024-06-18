import csv

from .report_utils.report_entities import call_records_statistics

def main(api: object, service_provider_id: str, group_id: str, 
         start_date:str, end_date: str = None, start_time: str = "00:00:00", 
         end_time:str = "23:59:59", time_zone: str = "Z"):
    
    group_users_statistics = []
    users = api.get.users(service_provider_id, group_id)
    
    for user in users:
        user_statistics = api.get.users_stats(
            user["userId"],
            start_date,
            end_date,
            start_time,
            end_time,
            time_zone
        )
        
        # Correction for API removing userId if no calls made by user
        if user_statistics["userId"] == None:
            user_statistics["userId"] = user["userId"]
        
        user_statistic_record = call_records_statistics.from_dict(user_statistics)
        group_users_statistics.append(user_statistic_record)
        
    file_name = f"./os_reports/{group_id} User Call Statistics - {start_date} to {end_date}"
        
    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=group_users_statistics[0].keys())
        writer.writeheader()
        
        for user in group_users_statistics:
            writer.writerow(user)
            