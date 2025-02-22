import streamlit as st
from streamlit_firebase_auth import FirebaseAuth

if "auth" not in st.session_state or not st.session_state.auth:
    st.session_state.auth = FirebaseAuth({
        "apiKey": "AIzaSyAui6XKx8DhSomOIj9_gpnIiriEsjmBm8Q",
        "authDomain": "ai-system-integration.firebaseapp.com",
        "projectId": "ai-system-integration",
        "storageBucket": "ai-system-integration.firebasestorage.app",
        "messagingSenderId": "848407305043",
        "appId": "1:848407305043:web:fec56bb2a8015343b95fa6"},
        lang="jp")
if "login" not in st.session_state or not st.session_state.login:
    st.session_state.login = st.session_state.auth.check_session()

pages = [
    st.Page("page1.py"),
    st.Page("page2.py"),
    st.Page("page3.py"),
]

with st.sidebar:
    result = st.session_state.auth.logout_form()
    if result:
        st.session_state.login = result["success"]
        if result["success"]:
            st.session_state.login = False
            st.success("ログアウトしました")
        else:
            st.error("ログアウトに失敗しました")

pg = st.navigation(pages)
pg.run()