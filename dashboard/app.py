import streamlit as st
import pandas as pd
from charts import histogram, neighbourhood_chart, revenue_chart
from charts import room_chart
from charts import singapore_map

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Airbnb Analytics Dashboard",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
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

st.title("🏠 Airbnb Data Engineering Dashboard")

st.write("Singapore Airbnb Analytics")


# ===================================
# Sidebar
# ===================================

st.sidebar.title("🏠 Airbnb Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Map",
        "Statistics",
        "About"
    ]
)



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
filtered_df = df.copy()

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


if page == "Dashboard":

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
elif page == "Analytics":

    st.title("💡 Business Insights")

    st.info("""
### 💰 Premium Listings

Entire home apartments generate the highest revenue.
""")

    st.info("""
### ⭐ Superhosts

Superhosts consistently receive higher ratings.
""")

    st.info("""
### 📍 Top Locations

River Valley and Orchard command premium prices.
""")

    st.info("""
### 📈 Revenue

Professional hosts dominate premium listings.
""")


# Interactive Map
elif page == "Map":

    st.title("🗺 Singapore Airbnb Map")

    st.plotly_chart(
        singapore_map(filtered_df),
        use_container_width=True
    )


# Statistical Results
elif page == "Statistics":

    st.title("📊 Statistical Analysis")

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
        

# About Project
elif page == "About":

    st.title("ℹ About This Project")

    st.markdown("""

## Airbnb Data Engineering Project

This project was developed as part of the Expernetic Data Engineer Internship Assessment.

### Technologies Used

- Python
- Pandas
- DuckDB
- SQL
- Plotly
- Streamlit

### Dataset

Inside Airbnb Singapore Dataset

### Author

**Dinali Chamodya**

2026

""")
    



