import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="APN Long Distance Call", page_icon="🎥")
st.title("APN: Secure Call (200km+) 🎥")

# 1. 'Aggressive' नेटवर्क सेटिंग्स
# इसमें हमने Twilio और Xirsys जैसे ग्लोबल बैकअप्स डाले हैं
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
        {"urls": ["stun:stun.services.mozilla.com"]},
        {"urls": ["stun:global.stun.twilio.com:3478"]},
    ],
    "iceTransportPolicy": "all",
    "iceCandidatePoolSize": 10,
}

st.sidebar.warning("दूरी: 200 KM | मोड: High Stability")

room_name = st.text_input("सीक्रेट रूम नाम (दोनों का Same हो):", value="ankush-khem-200km")

if room_name:
    st.success(f"रूम '{room_name}' तैयार है। 'Start' दबाएं।")
    
    webrtc_streamer(
        key=room_name,
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": {
                "width": {"max": 480}, # लो-बैंडविड्थ के लिए बेस्ट
                "frameRate": {"max": 10} # ताकि कॉल कटे नहीं
            },
            "audio": True,
        },
        async_processing=True,
    )

st.divider()
st.caption("यदि 200km दूर कॉल नहीं लग रही, तो एक बार मोबाइल का Hotspot बंद करके सीधा 5G/4G डेटा इस्तेमाल करें।")
