import streamlit as st
import os

# --- عداد الزوار ---
COUNTER_FILE = "counter.txt"

def get_visitor_count():
    """قراءة عدد الزوار من الملف أو تهيئته إذا غير موجود"""
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")
    try:
        with open(COUNTER_FILE, "r") as f:
            count = int(f.read().strip())
    except:
        count = 0
    return count

def increment_visitor_count():
    """زيادة العدد وتخزينه دائمًا في الملف"""
    count = get_visitor_count() + 1
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))
    return count

# --- شغل الكود عند فتح الصفحة ---
visitor_count = increment_visitor_count()

# --- عرض العداد في واجهة التطبيق ---
st.sidebar.success(f"Number of visitors: {visitor_count}")

# --- بقية الكود ---
from utils import check_url_safety

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
