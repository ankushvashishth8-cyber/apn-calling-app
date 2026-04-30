import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="APN Secure Call", page_icon="📞")

st.title("APN: Private Video Call 🎥")

# 1. बेहतर कनेक्शन के लिए ज्यादा STUN सर्वर्स
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
        {"urls": ["stun:stun2.l.google.com:19302"]},
        {"urls": ["stun:stun3.l.google.com:19302"]},
        {"urls": ["stun:stun4.l.google.com:19302"]},
    ]
}

# 2. रूम सिस्टम (ताकि आप दोनों एक ही पाइपलाइन में जुड़ें)
room_name = st.text_input("रूम का नाम लिखें (आप और दोस्त का सेम होना चाहिए):", value="apn-call-123")

if room_name:
    st.info(f"रूम '{room_name}' में जुड़ने के लिए तैयार।")
    
    webrtc_streamer(
        key=room_name, # यही सबसे जरूरी है, दोनों का Key सेम होना चाहिए
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": True, 
            "audio": True
        },
        # मोबाइल डेटा पर बेहतर चलने के लिए
        video_html_attrs={
            "autoPlay": True,
            "controls": False,
            "style": {"width": "100%"},
            "playsinline": True,
        },
        async_processing=True,
    )

st.warning("⚠️ ध्यान दें: अगर आप मोबाइल डेटा पर हैं, तो नेटवर्क की वजह से देरी हो सकती है।")
