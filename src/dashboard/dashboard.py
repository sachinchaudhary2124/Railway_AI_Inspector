from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.prediction.predict import predict_image
from src.dashboard.analytics import (
    save_prediction,
    load_history
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Railway AI Inspector",
    page_icon="🚆",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "entered" not in st.session_state:
    st.session_state.entered = False

# ==================================================
# LANDING PAGE
# ==================================================

if not st.session_state.entered:

    image_path = Path(__file__).parent / "assets" / "hero.jpg"

    st.markdown(
        """
        <style>

        .main > div {
            padding-top:1rem;
        }

        .hero-title{
            text-align:center;
            font-size:64px;
            font-weight:800;
            color:#60A5FA;
            margin-top:10px;
        }

        .hero-subtitle{
            text-align:center;
            font-size:22px;
            color:white;
            margin-top:10px;
        }

        .hero-project{
            text-align:center;
            color:#9CA3AF;
            margin-top:10px;
            margin-bottom:20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    center1, center2, center3 = st.columns([1,8,1])

    with center2:

        st.image(
            str(image_path),
            use_container_width=True
        )

    st.markdown(
        """
        <div class="hero-title">
        Railway AI Inspector
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-subtitle">
        AI-Powered Railway Track Monitoring<br>
        & Predictive Maintenance System
        </div>
        """,
        unsafe_allow_html=True
    )

    

    c1, c2, c3 = st.columns([3,2,3])

    with c2:

        if st.button(
            "ENTER CONTROL CENTER",
            use_container_width=True
        ):
            st.session_state.entered = True
            st.rerun()

    st.stop()

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("Railway AI Inspector")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Analytics",
            "Reports",
            "About"
        ]
    )

    st.markdown("---")

    
# ==================================================
# HEADER
# ==================================================

st.title("Railway AI Inspector")

st.subheader(
    "AI-Powered Railway Track Monitoring System"
)

st.markdown("---")

# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    anomaly = "No Data"
    confidence = 0
    priority = "-"
    track_status = "Normal"
    action = "Upload an image to begin inspection."

    left, right = st.columns([1,1])

    with left:

        uploaded_file = st.file_uploader(
            "Upload Railway Track Image",
            type=["jpg","jpeg","png"]
        )

        if uploaded_file:

            temp_path = "temp_upload.jpg"

            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.image(
                uploaded_file,
                use_container_width=True
            )

            result = predict_image(
                temp_path
            )

            anomaly = result["anomaly"]
            confidence = result["confidence"]
            priority = result["priority"]
            action = result["action"]

            if anomaly == "broken_rail":
                track_status = "Critical"

            elif anomaly == "crack":
                track_status = "Warning"

            elif anomaly == "misalignment":
                track_status = "Warning"

            elif anomaly == "surface_wear":
                track_status = "Monitor"

            else:
                track_status = "Normal"

            save_prediction(
                anomaly,
                confidence,
                priority,
                track_status
            )

    st.header(
        "Railway Monitoring Overview"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Anomaly Type",
        anomaly
    )

    c2.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    c3.metric(
        "Priority",
        priority
    )

    c4.metric(
        "Track Status",
        track_status
    )

    st.markdown("---")

    st.info(
        "Upload railway images and monitor track health."
    )

    with right:

        st.subheader(
            "Inspection Results"
        )

        if uploaded_file:

            st.success(
                f"{anomaly} Detected"
            )

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

            st.metric(
                "Priority",
                priority
            )

            st.warning(
                action
            )

        else:

            st.info(
                "Upload an image to generate predictions."
            )

# ==================================================
# ANALYTICS
# ==================================================

elif page == "Analytics":

    st.header(
        "Analytics Dashboard"
    )

    history = load_history()

    if history.empty:

        st.warning(
            "No prediction history available."
        )

    else:

        st.subheader(
            "Anomaly Distribution"
        )

        anomaly_counts = (
            history["Anomaly"]
            .value_counts()
        )

        fig, ax = plt.subplots()

        anomaly_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel(
            "Count"
        )

        st.pyplot(fig)

        st.subheader(
            "Confidence Trend"
        )

        fig2, ax2 = plt.subplots()

        history["Confidence"].plot(
            ax=ax2
        )

        ax2.set_ylabel(
            "Confidence (%)"
        )

        st.pyplot(fig2)

# ==================================================
# REPORTS
# ==================================================

elif page == "Reports":

    st.header(
        "Inspection Reports"
    )

    history = load_history()

    if history.empty:

        st.warning(
            "No reports generated yet."
        )

    else:

        st.dataframe(
            history,
            use_container_width=True
        )

        csv = history.to_csv(
            index=False
        )

        st.download_button(
            "Download Report",
            csv,
            "inspection_report.csv",
            "text/csv"
        )

# ==================================================
# ABOUT
# ==================================================

elif page == "About":

    st.header(
        "About Project"
    )

    st.write(
        """
        Railway AI Inspector uses Deep Learning,
        Computer Vision and Predictive Analytics
        to identify railway track defects,
        prioritize maintenance actions and
        improve railway safety.

        Features:
        • Crack Detection
        • Broken Rail Detection
        • Misalignment Detection
        • Surface Wear Detection
        • Analytics Dashboard
        • Inspection Reports
        """
    )