import plotly.express as px


def histogram(df):

    fig = px.histogram(
        df,
        x="price",
        nbins=30,
        title="Price Distribution",
        color_discrete_sequence=["#00C2FF"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F2A52",
        plot_bgcolor="#0F2A52",
        font_color="white",
        height=380
    )

    return fig


def room_chart(df):

    room = (
        df["room_type"]
        .value_counts()
        .reset_index()
    )

    room.columns = ["Room Type", "Listings"]

    fig = px.bar(
        room,
        x="Room Type",
        y="Listings",
        title="Room Types",
        color="Listings",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F2A52",
        plot_bgcolor="#0F2A52",
        font_color="white",
        height=380
    )

    return fig

#Revenue Distribution
def revenue_chart(df):

    fig = px.histogram(
        df,
        x="estimated_revenue_l365d",
        nbins=30,
        title="Revenue Distribution",
        color_discrete_sequence=["#6C63FF"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F2A52",
        plot_bgcolor="#0F2A52",
        font_color="white",
        height=380
    )

    return fig

#Top Neighbourhoods
def neighbourhood_chart(df):

    area = (
        df.groupby("neighbourhood_cleansed")["price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        area,
        x="neighbourhood_cleansed",
        y="price",
        title="Top Neighbourhoods",
        color="price",
        color_continuous_scale="Tealgrn"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F2A52",
        plot_bgcolor="#0F2A52",
        font_color="white",
        height=380
    )

    return fig

#Singapore Interactive Map
def singapore_map(df):

    fig = px.scatter_map(
        df,
        lat="latitude",
        lon="longitude",

        color="price",

        size="price",

        hover_name="name",

        hover_data={
            "room_type":True,
            "price":True,
            "review_scores_rating":True,
            "latitude":False,
            "longitude":False
        },

        zoom=10,

        height=650,

        color_continuous_scale="Turbo"
    )

    fig.update_layout(

        map_style="carto-darkmatter",

        paper_bgcolor="#0F2A52",

        font_color="white",

        margin=dict(
            l=0,
            r=0,
            t=40,
            b=0
        )
    )

    return fig

