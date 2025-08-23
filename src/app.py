import streamlit as st
import sqlite3
from utils import check_url_safety

# --- إعداد قاعدة البيانات لعداد الزوار ---
conn = sqlite3.connect("visitors.db")
c = conn.cursor()

# إنشاء جدول لو ما موجود
c.execute("""
CREATE TABLE IF NOT EXISTS counter (
    id INTEGER PRIMARY KEY,
    count INTEGER
)
""")

# جلب العدد الحالي
c.execute("SELECT count FROM counter WHERE id=1")
row = c.fetchone()
if row is None:
    c.execute("INSERT INTO counter (id, count) VALUES (1, 0)")
    conn.commit()
    visitor_count = 0
else:
    visitor_count = row[0]

# زيادة العدد وتخزينه
visitor_count += 1
c.execute("UPDATE counter SET count=? WHERE id=1", (visitor_count,))
conn.commit()

# --- عرض العداد ---
st.sidebar.success(f"Number of visitors: {visitor_count}")

# --- إعداد الصفحة ---
st.set_page_config(page_title="🔒 URL Safety Checker", page_icon="🛡️", layout="centered")
st.title("🔒 URL Safety Checker")
st.write("Enter a link and check if it’s safe or potentially harmful.")

# Input field
url = st.text_input("Enter a URL:")

if st.button("🔍 Check URL"):
    if url:
        result = check_url_safety(url)
        if not result["valid"]:
            st.error(f"❌ {result['reason']}")
        else:
            if result["safe"]:
                st.success(f"✅ Safe: {result['reason']}")
            else:
                st.warning(f"⚠️ Warning: {result['reason']}")
    else:
        st.error("Please enter a URL first 🚨")
