import json

with open("test/reports.json") as f:
    reports = json.load(f)

# Collect the last report for each config_id
last_reports = {}
default_exec_time = None

for report in reports:
    config_id = report.get("config_id")
    last_reports[config_id] = report  # Overwrites, so last occurrence stays
    if config_id == "default":
        default_exec_time = report.get("total_query_execution_time")

# Print total_query_execution_time for default, and total_completed_query_execution_time for others
if default_exec_time is not None:
    print(f"default: total_query_execution_time = {default_exec_time:.4f} seconds")

for config_id, report in last_reports.items():
    if config_id == "default":
        continue
    exec_time = report.get("total_completed_query_execution_time")
    print(f"{config_id}: total_completed_query_execution_time = {exec_time:.4f} seconds")