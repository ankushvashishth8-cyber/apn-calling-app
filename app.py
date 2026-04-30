import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

# 1. ऐप का डिज़ाइन
st.set_page_config(page_title="APN Calling", page_icon="📞")
st.title("APN: Secure Web Call 📞")
st.write("अपने दोस्तों से सीधा ब्राउज़र के ज़रिए एन्क्रिप्टेड बात करें!")

# 2. WebRTC की सेटिंग्स (Google का फ्री सर्वर जो फोन्स को ढूंढेगा)
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]} # यह इंटरनेट पर फोन का रास्ता खोजता है
    ]
}

# 3. कॉलिंग का इंटरफेस
st.markdown("### कॉल शुरू करने के लिए 'START' दबाएं")

webrtc_streamer(
    key="apn-audio-call",
    mode=WebRtcMode.SENDRECV, # हम भेजेंगे भी और सुनेंगे भी
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": False, # हमें वीडियो नहीं, सिर्फ ऑडियो चाहिए
        "audio": True
    },
)

st.info("नोट: यह एक सुरक्षित P2P कनेक्शन है। आपकी आवाज़ किसी सर्वर पर सेव नहीं हो रही है।")