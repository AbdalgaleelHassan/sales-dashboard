
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="تحليل المبيعات", layout="wide")

st.title("📊 لوحة تحليل بيانات المبيعات")

uploaded_file = st.file_uploader("📁 ارفع ملف CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # معالجة البيانات
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total_Sales'] = df['Quantity'] * df['Unit_Price']
    df['Month'] = df['Date'].dt.to_period('M')

    st.subheader("👁️ عرض البيانات")
    st.dataframe(df)

    st.subheader("📈 المبيعات حسب الفئة")
    sales_by_category = df.groupby('Category')['Total_Sales'].sum()
    fig1, ax1 = plt.subplots()
    ax1.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')
    st.pyplot(fig1)

    st.subheader("📊 المبيعات حسب الشهر")
    sales_by_month = df.groupby('Month')['Total_Sales'].sum()
    fig2, ax2 = plt.subplots()
    sales_by_month.plot(kind='bar', color='skyblue', ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    st.subheader("🏆 أكثر المنتجات مبيعًا")
    sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_product)
