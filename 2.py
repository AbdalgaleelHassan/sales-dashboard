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
        selected_category = st.multiselect("اختر الفئة:", df['Category'].
