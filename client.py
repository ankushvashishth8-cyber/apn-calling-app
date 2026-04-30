import socket
import threading
import pyaudio
from cryptography.fernet import Fernet

# 1. एन्क्रिप्शन की चाबी (यह आपके सभी दोस्तों के ऐप में सेम होनी चाहिए)
# यह एक असली 32-byte हैकिंग प्रूफ की (Key) है:
SECRET_KEY = b'cw_0x689ShIjaZB7A0b9D1v0X3_q1K9nJ7X8O2w8kH4='
cipher = Fernet(SECRET_KEY)

# 2. ऑडियो सेटिंग्स (माइक और स्पीकर के लिए)
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

# 3. नेटवर्क सेटिंग्स
# चूंकि अभी सर्वर आपके ही लैपटॉप पर चल रहा है, हम लोकल IP डालेंगे
SERVER_IP = '127.0.0.1' 
SERVER_PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('0.0.0.0', 0)) # अपने आप कोई भी खाली पोर्ट ले लेगा

# आवाज़ सुनने का सिस्टम (Receiver)
def receive_audio():
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    while True:
        try:
            encrypted_data, addr = client_socket.recvfrom(4096)
            # जैसे ही दोस्त की आवाज़ आए, उसे अपनी चाबी से 'अनलॉक' करो
            raw_audio = cipher.decrypt(encrypted_data)
            stream.write(raw_audio) # स्पीकर पर बजाओ
        except:
            pass

# आवाज़ भेजने का सिस्टम (Sender)
def send_audio(target_ip, target_port):
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("\n[+] कॉल कनेक्ट हो गई है! अब आप बोल सकते हैं... (कॉल काटने के लिए Ctrl+C दबाएं)")
    while True:
        try:
            raw_audio = stream.read(CHUNK)
            # आपकी आवाज़ बाहर जाने से पहले पूरी तरह 'लॉक' (Encrypt) हो जाएगी
            encrypted_audio = cipher.encrypt(raw_audio)
            client_socket.sendto(encrypted_audio, (target_ip, target_port))
        except:
            print("\n[-] कॉल कट गई।")
            break

# मेन ऐप इंटरफेस
def start_client():
    print("="*30)
    print("   APN ENCRYPTED CALLING   ")
    print("="*30)
    
    my_name = input("अपना नाम दर्ज करें: ")
    
    # 1. सर्वर को बताएं कि आप ऑनलाइन आ गए हैं
    client_socket.sendto(f"ONLINE:{my_name}".encode('utf-8'), (SERVER_IP, SERVER_PORT))
    
    target_name = input("\nकिसे कॉल करना है? (दोस्त का नाम डालें): ")
    print("सिग्नलिंग सर्वर से संपर्क किया जा रहा है...")
    
    # 2. सर्वर से दोस्त का एड्रेस मांगें
    client_socket.sendto(f"CALL:{target_name}".encode('utf-8'), (SERVER_IP, SERVER_PORT))
    
    # 3. सर्वर का जवाब सुनें
    response, _ = client_socket.recvfrom(1024)
    response_msg = response.decode('utf-8')
    
    if response_msg.startswith("FOUND:"):
        _, target_ip, target_port = response_msg.split(":")
        target_port = int(target_port)
        
        # सुनने वाला सिस्टम बैकग्राउंड (Thread) में चलाएं
        threading.Thread(target=receive_audio, daemon=True).start()
        
        # आवाज़ भेजना चालू करें
        send_audio(target_ip, target_port)
    else:
        print(f"\n[-] {response_msg}")

if __name__ == "__main__":
    start_client()