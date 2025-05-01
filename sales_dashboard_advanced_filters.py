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

    # 🎯 الفلاتر التفاعلية المتقدمة
    with st.sidebar:
        st.header("🎛️ فلاتر")
        selected_category = st.multiselect("اختر الفئة:", df['Category'].unique(), default=df['Category'].unique())
        selected_product = st.multiselect("اختر المنتج:", df['Product'].unique(), default=df['Product'].unique())
        date_range = st.date_input("اختر نطاق التاريخ:", [df['Date'].min(), df['Date'].max()])

    # تطبيق الفلاتر
    filtered_df = df[
        (df['Category'].isin(selected_category)) &
        (df['Product'].isin(selected_product)) &
        (df['Date'] >= pd.to_datetime(date_range[0])) &
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]

    st.subheader("📋 البيانات بعد التصفية")
    st.dataframe(filtered_df)

    st.subheader("📌 إجمالي المبيعات بعد التصفية:")
    total_sales = filtered_df['Total_Sales'].sum()
    st.metric(label="إجمالي المبيعات", value=f"{total_sales:.2f} ريال")

    # 📈 المبيعات حسب الفئة
    st.subheader("📈 المبيعات حسب الفئة")
    sales_by_category = filtered_df.groupby('Category')['Total_Sales'].sum()
    fig1, ax1 = plt.subplots()
    if not sales_by_category.empty:
        ax1.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')
        st.pyplot(fig1)
    else:
        st.info("لا توجد بيانات لعرضها.")

    # 📊 المبيعات حسب الشهر
    st.subheader("📊 المبيعات حسب الشهر")
    sales_by_month = filtered_df.groupby(filtered_df['Date'].dt.to_period('M'))['Total_Sales'].sum()
    fig2, ax2 = plt.subplots()
    if not sales_by_month.empty:
        sales_by_month.plot(kind='bar', color='skyblue', ax=ax2)
        plt.xticks(rotation=45)
        st.pyplot(fig2)
    else:
        st.info("لا توجد بيانات لعرضها.")

    # 🏆 المنتجات الأعلى مبيعًا
    st.subheader("🏆 أكثر المنتجات مبيعًا")
    sales_by_product = filtered_df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
    if not sales_by_product.empty:
        st.bar_chart(sales_by_product)
    else:
        st.info("لا توجد بيانات لعرضها.")
