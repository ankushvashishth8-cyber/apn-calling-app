import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import time

st.set_page_config(page_title="APN Long Distance", page_icon="🎥")
st.title("APN: High Stability Video Call 🎥")

# 1. बेहतर नेटवर्क सेटिंग्स (STUN/TURN)
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:global.stun.twilio.com:3478"]},
    ],
    "iceTransportPolicy": "all",
}

# 2. रूम और यूनीक की (Unique Key) मैनेजमेंट
# यह पुराने 'NoneType' एरर को रोकने के लिए बहुत जरूरी है
if "unique_key" not in st.session_state:
    st.session_state.unique_key = str(int(time.time()))

room_name = st.text_input("रूम का नाम (Ankush और Khem दोनों का सेम हो):", value="ankush-khem-call")

# ऐप को पूरी तरह रीसेट करने का बटन
if st.button("ऐप रीसेट करें (यदि एरर आए)"):
    st.session_state.unique_key = str(int(time.time()))
    st.rerun()

st.write("---")

if room_name:
    webrtc_streamer(
        key=f"{room_name}-{st.session_state.unique_key}", 
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": {"width": 640, "frameRate": 15}, # हल्की क्वालिटी ताकि 200km दूर लैग न हो
            "audio": True
        },
        async_processing=True,
    )

st.warning("⚠️ ध्यान दें: 'START' दबाने के बाद 10-15 सेकंड का इंतज़ार करें।")
st.divider()
st.caption("यदि 200km दूर कॉल नहीं लग रही, तो एक बार मोबाइल का Hotspot बंद करके सीधा 5G/4G डेटा इस्तेमाल करें।")
