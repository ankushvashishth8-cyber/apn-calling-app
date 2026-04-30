import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="APN 24/7 Call", page_icon="📞")

# 1. CSS फिक्स (HTML परमिशन को सही किया गया है)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    /* बटन और नाम को ऊपर फिक्स रखने के लिए */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    </style>
    """, unsafe_allow_html=True) # यहाँ 'html' होना चाहिए था

st.title("APN: Secure Web Call 📞")

# नेटवर्क सेटिंग्स
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]}
    ]
}

# इनपुट बॉक्स
col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("आपका नाम:", value="Ankush")
with col2:
    friend_name = st.text_input("दोस्त का नाम:", value="Khem")

st.divider()

# WebRTC इंजन - वीडियो और ऑडियो दोनों चालू
webrtc_streamer(
    key="apn-v3-call",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": True, 
        "audio": True
    },
    async_processing=True,
)

st.info("नोट: 'Start' दबाने के बाद ब्राउज़र न बदलें।")
