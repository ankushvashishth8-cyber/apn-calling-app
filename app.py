import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("APN: Secure Web Call 📞")

# नाम दर्ज करने का बॉक्स
user_name = st.text_input("अपना नाम दर्ज करें:")
friend_name = st.text_input("किसे कॉल करना है?")

if user_name and friend_name:
    st.success(f"नमस्ते {user_name}! {friend_name} से जुड़ने के लिए START दबाएं।")
    
    webrtc_streamer(
        key="apn-audio-call",
        mode=WebRtcMode.SENDRECV,
        media_stream_constraints={"video": False, "audio": True},
    )
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
