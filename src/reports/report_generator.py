from pathlib import Path
from datetime import datetime


def save_report(
    anomaly_type,
    confidence,
    priority,
    action,
    latitude,
    longitude
):

    # Generate Report Metadata
    report_id = f"RAI-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    inspector = "AI Railway Inspector"

    report_text = f"""
==================================================
RAILWAY INSPECTION REPORT
==================================================

Report ID      : {report_id}
Timestamp      : {timestamp}
Inspector Name : {inspector}

--------------------------------------------------

Anomaly Type     : {anomaly_type}
Confidence Score : {confidence:.2f}%
Priority Level   : {priority}

Recommended Action:
{action}

--------------------------------------------------
Location Information
--------------------------------------------------

Latitude  : {latitude}
Longitude : {longitude}

==================================================
END OF REPORT
==================================================
"""

    report_path = (
        Path(__file__).resolve().parent
        / "inspection_report.txt"
    )

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    print("\nReport Saved Successfully")
    print("Report Path :", report_path)

    return report_path