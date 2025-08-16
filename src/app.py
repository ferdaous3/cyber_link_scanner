import streamlit as st
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