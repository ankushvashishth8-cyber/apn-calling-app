import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="APN 24/7 Call", page_icon="📞")

# 1. CSS ताकि बटन और वीडियो हमेशा एक ही जगह फिक्स रहें
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        position: sticky;
        top: 0;
        z-index: 999;
        background-color: #0e1117;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_header=True)

st.title("APN: Continuous Call 📞")

RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
        {"urls": ["stun:stun2.l.google.com:19302"]},
    ]
}

# यूज़र नाम (इनपुट हमेशा ऊपर रहेगा)
user_name = st.text_input("आपका नाम:", value="Ankush", key="user")
friend_name = st.text_input("दोस्त का नाम:", value="Khem", key="friend")

st.divider()

# WebRTC इंजन
# 'always_ask_for_permission=False' और 'async_processing=True' बैकग्राउंड में मदद करते हैं
webrtc_streamer(
    key="apn-bg-call",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": True, 
        "audio": True
    },
    async_processing=True, # यह बैकग्राउंड प्रोसेसिंग में मदद करता है
)

st.info("प्रो टिप: बैकग्राउंड में चलाने के लिए ब्राउज़र टैब को खुला रखें और उसे बंद (Minimize) न करें।")
