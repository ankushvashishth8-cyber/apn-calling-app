import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import time

st.set_page_config(page_title="APN Final Fix", page_icon="📞")
st.title("APN: High-Stability Video Call 🎥")

# 1. सबसे भरोसेमंद STUN/TURN कॉन्फ़िगरेशन
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
        {"urls": ["stun:global.stun.twilio.com:3478"]},
    ],
    "iceTransportPolicy": "all",
    "iceCandidatePoolSize": 10,
}

# 2. रूम मैनेजमेंट (नाम और यूनीक आईडी)
if "session_id" not in st.session_state:
    st.session_state.session_id = str(int(time.time()))

room_name = st.text_input("रूम का नाम (Ankush और Khem दोनों का सेम हो):", value="apn-stable-call")

# हार्ड रिसेट बटन (एरर आने पर इसे दबाएं)
if st.button("ऐप को पूरी तरह रिफ्रेश करें"):
    st.session_state.session_id = str(int(time.time()))
    st.rerun()

st.divider()

if room_name:
    webrtc_streamer(
        # रूम नाम और समय को मिलाकर एक फ्रेश चाबी बनाना
        key=f"{room_name}-{st.session_state.session_id}", 
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": {
                "width": {"ideal": 320}, # बहुत हल्का वीडियो (200km के लिए बेस्ट)
                "frameRate": {"ideal": 10} 
            },
            "audio": True
        },
        async_processing=True,
        # मोबाइल के लिए विशेष निर्देश
        video_html_attrs={
            "autoPlay": True,
            "controls": False,
            "playsinline": True,
            "muted": False,
        },
    )

st.info("💡 टिप: 'START' दबाने के बाद 20 सेकंड तक इंतज़ार करें। 200km दूर सिग्नल पहुँचने में समय लगता है।")

st.warning("⚠️ ध्यान दें: 'START' दबाने के बाद 10-15 सेकंड का इंतज़ार करें।")
st.divider()
st.caption("यदि 200km दूर कॉल नहीं लग रही, तो एक बार मोबाइल का Hotspot बंद करके सीधा 5G/4G डेटा इस्तेमाल करें।")
