import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("APN: Secure Web Call 📞")

# 1. पहले RTC_CONFIGURATION को डिफाइन करें (यह हिस्सा मिसिंग था)
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]} 
    ]
}

# 2. अब कॉल शुरू करने का कोड
user_name = st.text_input("अपना नाम दर्ज करें:")
friend_name = st.text_input("किसे कॉल करना है?")

if user_name and friend_name:
    st.success(f"नमस्ते {user_name}! {friend_name} से जुड़ने के लिए START दबाएं।")
    
    webrtc_streamer(
        key="apn-audio-call",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION, # अब यहाँ एरर नहीं आएगा!
        media_stream_constraints={
            "video": False, 
            "audio": True
        },
    )
