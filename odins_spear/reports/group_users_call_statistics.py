import csv
import os

from tqdm import tqdm

from .report_utils.file_manager import copy_single_file_to_target_directory
from .report_utils.report_entities import call_records_statistics

def main(api: object, service_provider_id: str, group_id: str, 
         start_date:str, end_date: str = None, start_time: str = "00:00:00", 
         end_time:str = "23:59:59", time_zone: str = "Z"):
    """Generates a CSV deatiling each users incoming and outgoing call statistics over 
        a specified period for a single group. Each row contains user extension, user ID, and call stats.

    Args:
        service_provider_id (str):  Service Provider/ Enterprise where group is hosted.
        group_id (str): Target Group you would like to know user statistics for.
        start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
        end_date (str, optional): End date of desired time period. Date must follow format 'YYYY-MM-DD'.\
            If this date is the same as Start date you do not need this parameter. Defaults to None.
        start_time (_type_, optional): Start time of desired time period. Time must follow formate 'HH:MM:SS'. \
            If you do not need to filter by time and want the whole day leave this parameter. Defaults to "00:00:00". MAX Request is 3 months.
        end_time (_type_, optional): End time of desired time period. Time must follow formate 'HH:MM:SS'. \
            If you do not need to filter by time and want the whole day leave this parameter. Defaults to "23:59:59". MAX Request is 3 months.
        time_zone (str, optional): A specified time you would like to see call records in. \
    """
    
    print("\nStart.")
    
    # List of report_entities.call_records_statistics
    group_users_statistics = []
    
    print(f"Fetching list of users in {group_id}.")
    
    # Fetches complete list of users in group
    users = api.get.users(service_provider_id, group_id)
    failed_users = []
    
    # Pulls stats for each user, instantiates call_records_statistics, and append to group_users_statistics
    for user in tqdm(users, "Fetching individual stats for each user. This may take several minutes"):
        
        try:
            user_statistics = api.get.users_stats(
                user["userId"],
                start_date,
                end_date,
                start_time,
                end_time,
                time_zone
            )
            
            user_services = api.get.user_services(
                user_id=user["userId"]
            )
            
        except Exception:
            # attempt 2
            try:
                user_statistics = api.get.users_stats(
                    user["userId"],
                    start_date,
                    end_date,
                    start_time,
                    end_time,
                    time_zone
                )
                
                user_services = api.get.user_services(
                user_id=user["userId"]
                )
                
            except Exception:
                failed_users.append(user)
                continue
        
        user_statistics["servicePackServices"] = [service["serviceName"] for service in user_services["servicePackServices"] if service["assigned"]]
        
        # Correction for API removing userId if no calls made by user
        if user_statistics["userId"] is None:
            user_statistics["userId"] = user["userId"]
        
        user_statistic_record = call_records_statistics.from_dict(user["firstName"], user["lastName"], user["extension"], user_statistics)
        group_users_statistics.append(user_statistic_record)
    
    # replace none with 0 if data returns None. Output is better if 0 allows user to make use of data better
    for record in tqdm(group_users_statistics, "Formatting individual stats for each user"):
        record.replace_none_with_0()
    
    output_directory = "./os_reports"
    file_name = os.path.join(output_directory, f"{group_id} User Call Statistics - {start_date} to {end_date}.csv")

    # Ensure the directory exists
    os.makedirs(output_directory, exist_ok=True)   
    
    # Write statistics to csv 
    with open(file_name, mode="w", newline="") as file:
        fieldnames = [field.name for field in call_records_statistics.__dataclass_fields__.values()]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for user in group_users_statistics:
            writer.writerow(user.__dict__)
        
        # Adds list of failed users to the bottom 
        if failed_users:
            writer.writerow({})
            writer.writerow({fieldnames[1]: "Failed Users"})
            
            for failed_user in failed_users:
                writer.writerow({fieldnames[1]: failed_user['userId']})
    
    # Add made_with_os.png for output   
    copy_single_file_to_target_directory("./odins_spear/assets/images/", "./os_reports/", "made_with_os.png")        
    print("\nEnd.")
            