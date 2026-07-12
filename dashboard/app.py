import streamlit as st
import pandas as pd
from PIL import Image
from charts import histogram, neighbourhood_chart, revenue_chart
from charts import room_chart
from charts import singapore_map
from charts import ( avg_price_roomtype, professional_hosts, rating_distribution, revenue_roomtype)
from report import create_pdf
from datetime import datetime
from zoneinfo import ZoneInfo




# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Airbnb Analytics Dashboard",
    page_icon="dashboard/assets/logo.png",
    layout="wide"
)

# -----------------------------
# Load Logo
# -----------------------------

logo = Image.open("dashboard/assets/logo.png")

# -----------------------------
# Set Timezone
# -----------------------------
now = datetime.now(ZoneInfo("Asia/Colombo"))

#------------------------------
# Load CSS
# -----------------------------

with open("dashboard/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/processed/featured_listings.csv")

# -----------------------------
# Title
# -----------------------------

col1, col2, col3 = st.columns([0.8, 5.5, 1.2], vertical_alignment="center")

with col1:
    st.image(logo, width=95)

with col2:
    st.markdown(
        """
        <h1 style="
            margin-bottom:0px;
            margin-top:20px;
            color:white;
        ">
        Airbnb Data Engineering Dashboard
        </h1>

        <p style="
            color:#cfd8dc;
            font-size:20px;
            margin-top:0px;
        ">
        Singapore Airbnb Analytics
        </p>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(f"""
    <div style="
        background:#17375E;
        border-radius:12px;
        padding:15px;
        border:1px solid #2EA8FF;
        text-align:center;
    ">

    <div style="font-size:14px;color:#9CCBFF;">📅 Today</div>
    <div style="font-size:18px;font-weight:bold;color:white;">
        {now.strftime("%d %b %Y")}
    </div>

    <hr style="border:0.5px solid #2EA8FF;">

    <div style="font-size:14px;color:#9CCBFF;">🕒 Time</div>
    <div style="font-size:18px;font-weight:bold;color:white;">
        {now.strftime("%I:%M %p")}
    </div>

    </div>
    """, unsafe_allow_html=True)




# ===================================
# Sidebar
# ===================================

col1, col2, col3 = st.sidebar.columns([1,3,1])

with col2:
    st.image(logo, width=120)

st.sidebar.markdown(
    """
    <h2 style='text-align:center;'>Airbnb Dashboard</h2>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# Navigation Title
st.sidebar.markdown("""
<h3 style="
color:#53b8ff;
font-weight:700;
margin-top:15px;
margin-bottom:8px;
">
🧭 Navigation
</h3>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "",
    [
        "🏠 Dashboard",
        "📊 Analytics",
        "🗺 Map",
        "📈 Statistics",
        "ℹ️ About"
    ]
)

# Default dataset (used by all pages)
filtered_df = df.copy()

if page == "🏠 Dashboard":

    st.sidebar.markdown("---")
    st.sidebar.header("Filters")

    #Room Type Filter
    room_type = st.sidebar.selectbox(
        "Room Type",
        ["All"] + sorted(df["room_type"].dropna().unique().tolist())
    )


    #Property Type Filter
    property_type = st.sidebar.selectbox(
        "Property Type",
        ["All"] + sorted(df["property_type"].dropna().unique().tolist())
    )

    #Neighbourhood Filter
    neighbourhood = st.sidebar.selectbox(
        "Neighbourhood",
        ["All"] + sorted(df["neighbourhood_cleansed"].dropna().unique().tolist())
    )


    #Apply Filters

    if room_type != "All":
        filtered_df = filtered_df[
            filtered_df["room_type"] == room_type
        ]

    if property_type != "All":
        filtered_df = filtered_df[
            filtered_df["property_type"] == property_type
        ]

    if neighbourhood != "All":
        filtered_df = filtered_df[
            filtered_df["neighbourhood_cleansed"] == neighbourhood
        ]

    

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    st.markdown("---")

    left, right = st.columns(2)

    st.markdown("---")

    left2, right2 = st.columns(2)

    # ==========================
    # KPI Cards
    # ==========================

    with col1:
        st.metric(
            "🏠 Total Listings",
            f"{len(filtered_df):,}"
        )

    with col2:
        st.metric(
            "💰 Average Price",
            f"${filtered_df['price'].mean():.2f}"
        )

    with col3:
        st.metric(
            "⭐ Average Rating",
            f"{filtered_df['review_scores_rating'].mean():.2f}"
        )

    with col4:
        st.metric(
            "📈 Occupancy Rate",
            f"{filtered_df['occupancy_rate'].mean():.1f}%"
        )

    with left:

        st.plotly_chart(
            histogram(filtered_df),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            room_chart(filtered_df),
            use_container_width=True
        )

    with left2:
        st.plotly_chart(
            revenue_chart(filtered_df),
            use_container_width=True
        )

    with right2:
        st.plotly_chart(
            neighbourhood_chart(filtered_df),
            use_container_width=True
        )


    st.markdown("---")

    st.subheader("🗺 Singapore Airbnb Listings")

    st.plotly_chart(

        singapore_map(filtered_df),

        use_container_width=True

    )


    # Add Top 10 Expensive Listings
    st.markdown("---")

    st.subheader("💰 Top Premium Listings")

    top = filtered_df.sort_values(

        "price",

        ascending=False

    ).head(10)

    st.dataframe(

        top[
            [
                "name",

                "price",

                "room_type",

                "review_scores_rating"
            ]
        ],

        use_container_width=True
    )


# Business Insights
elif page == "📊 Analytics":

    st.markdown("---")

    st.header("📊 Analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            avg_price_roomtype(df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            professional_hosts(df),
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            rating_distribution(df),
            use_container_width=True
        )

    with col4:
        st.plotly_chart(
            revenue_roomtype(df),
            use_container_width=True
        )


# Interactive Map
elif page == "🗺 Map":

    st.markdown("---")

    st.title("🗺 Singapore Airbnb Map")

    st.plotly_chart(
        singapore_map(filtered_df),
        use_container_width=True
    )


# Statistical Results
elif page == "📈 Statistics":

    st.markdown("---")

    st.title("📈 Statistical Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
### H1

✅ Accepted

Entire homes are significantly more expensive than private rooms.

P < 0.001
""")

        st.success("""
### H2

✅ Accepted

Superhosts receive significantly higher review ratings.

P < 0.001
""")

    with col2:

        st.success("""
### H3

✅ Accepted

Listings with many reviews show a significant price difference.

P = 0.0034
""")

        st.success("""
### H4

✅ Accepted

Average prices differ significantly across neighbourhoods.

P < 0.001
""")
        
    #Hypothesis Results Table
    st.markdown("---")

    st.subheader("📋 Hypothesis Test Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Tests", "4")

    c2.metric("Accepted", "4")

    c3.metric("Rejected", "0")

    c4.metric("Confidence", "95%")

    results = pd.DataFrame({

        "Hypothesis": [
            "H1",
            "H2",
            "H3",
            "H4"
        ],

        "Description": [
            "Entire Home vs Private Room Price",
            "Superhost vs Review Rating",
            "Review Count vs Price",
            "Neighbourhood Price Difference"
        ],

        "P-Value": [
            "<0.0001",
            "<0.0001",
            "0.0034",
            "0.000007"
        ],

        "Decision": [
            "Reject H0",
            "Reject H0",
            "Reject H0",
            "Reject H0"
        ]

    })

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )

    #Statistical Interpretation
    st.markdown("---")

    st.subheader("📖 Interpretation")

    st.success("""
    ✔ Entire home apartments are significantly more expensive.

    ✔ Superhosts receive significantly higher ratings.

    ✔ Listings with many reviews show significant price differences.

    ✔ Average prices differ significantly across neighbourhoods.
    """)

    # ==========================================
    # Download Professional PDF Report
    # ==========================================

    st.markdown("---")

    st.subheader("📄 Generate Report")

    if st.button("Generate PDF Report"):

        create_pdf(filtered_df)

        with open("Airbnb_Analytics_Report.pdf", "rb") as pdf_file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf_file,
                file_name="Airbnb_Analytics_Report.pdf",
                mime="application/pdf"
            )
            

# ======================================
# ABOUT PAGE
# ======================================

elif page == "ℹ️ About":

    st.markdown("---")

    st.title("ℹ️About This Project")

    st.markdown("""
## 🏠 Airbnb Data Engineering Dashboard

This project was developed as part of the **Expernetic Data Engineer Internship Assessment**.

The objective of this project is to demonstrate an end-to-end data engineering workflow including data ingestion,
cleaning, feature engineering, analytical visualization, statistical hypothesis testing and automated reporting.

---
""")

    # ======================================
    # Project Information
    # ======================================

    c1, c2 = st.columns(2)

    with c1:

        st.info("""
### 📌 Project Information

- **Project Name**
  Airbnb Data Engineering Dashboard

- **Dataset**
  Singapore Airbnb Listings

- **Domain**
  Hospitality Analytics

- **Development Language**
  Python

- **Framework**
  Streamlit

- **Visualization**
  Plotly

- **Database**
  DuckDB
""")

    with c2:

        st.success("""
### 🚀 Project Features

✅ Interactive Dashboard

✅ Dynamic Filtering

✅ Business Insights

✅ Interactive Singapore Map

✅ Statistical Hypothesis Testing

✅ Professional PDF Report Generation

✅ Responsive Dark UI
""")

    st.markdown("---")

    st.subheader("🛠 Technology Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:

        st.markdown("""
### Backend

- Python
- Pandas
- NumPy
- DuckDB
""")

    with tech2:

        st.markdown("""
### Visualization

- Streamlit
- Plotly
- Mapbox
- ReportLab
""")

    with tech3:

        st.markdown("""
### Data Engineering

- Data Cleaning
- Feature Engineering
- SQL
- Statistical Analysis
""")

    st.markdown("---")

    st.subheader("📊 Project Workflow")

    st.markdown("""

1️⃣ Data Collection

⬇

2️⃣ Data Cleaning

⬇

3️⃣ Feature Engineering

⬇

4️⃣ Exploratory Data Analysis

⬇

5️⃣ Dashboard Development

⬇

6️⃣ Statistical Testing

⬇

7️⃣ Business Insights

⬇

8️⃣ PDF Report Generation

""")

    st.markdown("---")

    st.subheader("🎯 Project Objectives")

    st.success("""
• Analyze Singapore Airbnb listings.

• Discover pricing patterns.

• Compare neighbourhood performance.

• Understand room type behaviour.

• Validate business hypotheses.

• Generate automated analytical reports.
""")

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    col1, col2 = st.columns([1,4])

    with col1:
        st.image("dashboard/assets/logo.png", width=120)

    with col2:

        st.markdown("""
### Dinali Chamodya

**Data Science Undergraduate**

SLIIT

📍 Sri Lanka

**Expernetic Data Engineer Internship Assessment**
""")

    st.markdown("---")

    st.caption("© 2026 Airbnb Data Engineering Dashboard | Developed using Python & Streamlit")
    



