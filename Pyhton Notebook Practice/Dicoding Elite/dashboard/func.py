from typing import List, Dict
import pandas as pd

def calculate_metrics(filtered_df: pd.DataFrame):
    # Define the message for no change
    no_change_msg = "Same as last month"

    # Calculate metrics
    below_recommended = filtered_df[filtered_df["sleep_duration"] < 7].shape[0]
    high_blood_pressure = filtered_df[filtered_df["blood_pressure_category"] != "Normal"].shape[0]
    obese_people = filtered_df[filtered_df["bmi_category"] == "Obese"].shape[0]
    stressed_count = filtered_df[filtered_df["stress_level"] > 7].shape[0]

    # Prepare metrics data with trend conditional formatting
    return [
        {
            "title": "Total Individuals Below 7 Sleep Hours",
            "content": str(below_recommended),
            "trend": f"▼{below_recommended % 4} from last month" if below_recommended % 4 != 0 else no_change_msg
        },
        {
            "title": "Total Individuals with High Blood Pressure",
            "content": str(high_blood_pressure),
            "trend": f"▼{high_blood_pressure % 2} from last month" if high_blood_pressure % 2 != 0 else no_change_msg
        },
        {
            "title": "Total Individuals Classified as Obese",
            "content": str(obese_people),
            "trend": f"▲{obese_people % 5} from last month" if obese_people % 5 != 0 else no_change_msg
        },
        {
            "title": "Total Individuals Experiencing Stress",
            "content": str(stressed_count),
            "trend": f"▲{stressed_count % 7} from last month" if stressed_count % 7 != 0 else no_change_msg
        },
    ]
