import pandas as pd
from pathlib import Path

HISTORY_FILE = Path("prediction_history.csv")


def save_prediction(
    anomaly,
    confidence,
    priority,
    track_status
):

    data = {
        "Anomaly": [anomaly],
        "Confidence": [confidence],
        "Priority": [priority],
        "Track Status": [track_status]
    }

    df = pd.DataFrame(data)

    if HISTORY_FILE.exists():

        old_df = pd.read_csv(HISTORY_FILE)

        df = pd.concat(
            [old_df, df],
            ignore_index=True
        )

    df.to_csv(
        HISTORY_FILE,
        index=False
    )


def load_history():

    if HISTORY_FILE.exists():

        return pd.read_csv(
            HISTORY_FILE
        )

    return pd.DataFrame(
        columns=[
            "Anomaly",
            "Confidence",
            "Priority",
            "Track Status"
        ]
    )