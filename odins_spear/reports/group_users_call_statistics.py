import csv
import os

from tqdm import tqdm

from .report_utils.report_entities import call_records_statistics

def main(api: object, service_provider_id: str, group_id: str, 
         start_date:str, end_date: str = None, start_time: str = "00:00:00", 
         end_time:str = "23:59:59", time_zone: str = "Z"):
    
    print("\nStart.")
    
    group_users_statistics = []
    
    print(f"Fetching list of users in {group_id}.")
    users = api.get.users(service_provider_id, group_id)
    
    for user in tqdm(users, "Fetching individual stats for each user. This may take several minutes."):
        user_statistics = api.get.users_stats(
            user["userId"],
            start_date,
            end_date,
            start_time,
            end_time,
            time_zone
        )
        
        # Correction for API removing userId if no calls made by user
        if user_statistics["userId"] is None:
            user_statistics["userId"] = user["userId"]
        
        user_statistic_record = call_records_statistics.from_dict(user["extension"], user_statistics)
        group_users_statistics.append(user_statistic_record)
      
    output_directory = "./os_reports"
    file_name = os.path.join(output_directory, f"{group_id} User Call Statistics - {start_date} to {end_date}.csv")
       
    # Ensure the directory exists
    os.makedirs(output_directory, exist_ok=True)   
    
    with open(file_name, mode="w", newline="") as file:
        
        fieldnames = [field.name for field in call_records_statistics.__dataclass_fields__.values()]
    
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for user in group_users_statistics:
            writer.writerow(user.__dict__)
    
    print("\nEnd.")
            