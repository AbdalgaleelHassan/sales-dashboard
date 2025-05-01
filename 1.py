import pandas as pd
import matplotlib.pyplot as plt

# تأكد من أن الملف موجود بنفس المجلد
df = pd.read_csv("sales.csv")

##################################################################
# عرض أول 5 صفوف من البيانات
print(df.head())
###############
# معلومات عامة عن الأعمدة
print(df.info())

# إحصائيات عددية
print(df.describe())
####################################
# إنشاء عمود جديد اسمه "Total_Sales" لحساب المبيعات الكاملة
df['Total_Sales'] = df['Quantity'] * df['Unit_Price']

# عرض البيانات بعد الإضافة
print(df)
###############################################
# تجميع المبيعات حسب المنتج
sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)

print(sales_by_product)
############################################
# تجميع المبيعات حسب الفئة
sales_by_category = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)

print(sales_by_category)
############################################
# تحويل العمود Date إلى تاريخ
df['Date'] = pd.to_datetime(df['Date'])

# تجميع المبيعات حسب التاريخ
sales_by_date = df.groupby('Date')['Total_Sales'].sum()

print(sales_by_date)
########################################################
import matplotlib.pyplot as plt

# مثال على الرسم البياني:
sales_by_date.plot(kind='line', marker='o')
#plt.title('مبيعات حسب الأيام')
#plt.xlabel('التاريخ')
#plt.ylabel('إجمالي المبيعات')

plt.title('Sales by days')
plt.xlabel('Date')
plt.ylabel('Total sales')
plt.grid(True)
plt.show()

###################################################
import matplotlib.pyplot as plt

# تجميع المبيعات حسب الفئة
sales_by_category = df.groupby('Category')['Total_Sales'].sum()

# رسم المخطط الدائري
plt.figure(figsize=(6, 6))
plt.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%', startangle=140)
#plt.title('نسبة المبيعات حسب الفئة')
plt.title('Sales percentage by category')
plt.axis('equal')  # لتكون الدائرة متوازنة
plt.show()
#########################################
# التأكد من أن العمود Date بصيغة datetime
df['Date'] = pd.to_datetime(df['Date'])

# استخراج اسم الشهر
df['Month'] = df['Date'].dt.to_period('M')  # أو dt.month_name() لعرض الاسم الكامل

# تجميع المبيعات حسب الشهر
sales_by_month = df.groupby('Month')['Total_Sales'].sum()

# عرض النتائج
print(sales_by_month)

# رسم المبيعات حسب الشهر
sales_by_month.plot(kind='bar', color='skyblue')
#plt.title('إجمالي المبيعات الشهرية')
plt.title('Total monthly sales')
plt.xlabel('month')
#plt.ylabel('إجمالي المبيعات')
plt.ylabel('Total sales')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
