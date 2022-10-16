import pandas as  pd
import plotly.express as px
import streamlit as st 
from st_fn import st_button, load_css


st.set_page_config(page_title="NFT SALES DASHBOARD",page_icon=":bar_chart:",layout="wide")

df = pd.read_excel("NFT_Sales 1 (1).xlsx")

df2 = pd.read_excel("nft_bands 1.xlsx")

# print(df)

# st.dataframe(df)


st.sidebar.header("Please Filter Here:")

year = st.sidebar.multiselect(
    "Select the year:",
    options=df["year"].unique(),
    #  default=df["year"].unique()
)




df_select = df.query(
    "year == @year"
)


st.title(":cyclone: NFT Sales Dashboard")
st.markdown("##")

total_sales = int(df_select["Number_of_Sales"].sum())
sales_usd = int(df_select["Sales_USD"].sum())

left_co, right_co = st.columns(2)
with left_co:
    st.subheader("Total Sales:")
    st.subheader(f" {total_sales:,}")
with right_co:
    st.subheader("Sales in USD")
    st.subheader(f"US $ {sales_usd:,}")
    
st.markdown("---")

# st.dataframe(df_select)

sales_by_year = (
    df_select.groupby(by=["year"]).sum()[["Number_of_Sales"]].sort_values(by="Number_of_Sales")
)



sales_by_month = (
    df_select.groupby(by=["month"]).sum()[["Number_of_Sales"]].sort_values(by="Number_of_Sales")
)

sales_in_usd = (
    df_select.groupby(by=["year"]).sum()[["Sales_USD"]].sort_values(by="Sales_USD")
)

primary_sales = (
    df_select.groupby(by=["year"]).sum()[["Primary_Sales"]].sort_values(by="Primary_Sales")
)

fig_product_sales = px.bar(
    
    sales_by_year,
    x="Number_of_Sales",
    y=sales_by_year.index,
    orientation="h",
    title="<b>Sales by Year</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_year),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = (dict(showgrid=False))
)

fig_product_month = px.bar(
    
    sales_by_month,
    x="Number_of_Sales",
    y=sales_by_month.index,
    orientation="h",
    title="<b>Sales by month</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_month),
    template="plotly_white",
)

fig_product_month.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = (dict(showgrid=False))
)

line_chart = px.line(
    
    sales_in_usd,
    x=sales_in_usd.index,
    y="Sales_USD",
    # orientation="h",
    title="<b>Sales in USD</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_in_usd),
    template="plotly_white",
    )

line_chart.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = (dict(showgrid=False)),
    yaxis = (dict(showgrid=False))
)

primary_sales_chart = px.line(
    
    primary_sales,
    x=primary_sales.index,
    y="Primary_Sales",
    # orientation="h",
    title="<b>Primary Sales</b>",
    color_discrete_sequence=["#0083B8"] * len(primary_sales),
    template="plotly_white",
    )

primary_sales_chart.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = (dict(showgrid=False)),
    yaxis = (dict(showgrid=False))
)

pie_chart = px.pie(df,
                   title='Active Market Wallets',
                   values='Active_Market_Wallets',
                   names='year'
                   )

hide = """
      <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      </style>
      """
st.markdown(hide,unsafe_allow_html=True)

st.plotly_chart(fig_product_sales)

st.plotly_chart(fig_product_month)

st.plotly_chart(primary_sales_chart)

st.plotly_chart(line_chart)

st.plotly_chart(pie_chart)

load_css()

icon_size = 20

st.title(":cyclone: Analyse more on COGNOS")

st_button('IBM', 'https://keshava369.github.io/abcd/', 'COGNOS ANALYTICS', icon_size)

st.info('Login or sign up to explore more on cognos')




