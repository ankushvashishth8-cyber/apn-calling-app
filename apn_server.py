import socket

# यह डिक्शनरी (लिस्ट) आपके दोस्तों के नाम और उनके एड्रेस याद रखेगी
directory = {}

def start_network_brain():
    # UDP सॉकेट बनाना (तेज़ कनेक्शन के लिए)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 0.0.0.0 का मतलब है कि यह आपके लोकल नेटवर्क पर सबकी सुनेगा
    server.bind(('0.0.0.0', 9999))
    print("APN (Ankush Private Network) का सर्वर चालू हो गया है...")
    print("पोर्ट 9999 पर दोस्तों का इंतज़ार है...\n")

    while True:
        # दोस्तों से मैसेज रिसीव करना
        data, addr = server.recvfrom(1024)
        msg = data.decode('utf-8')
        
        # अगर कोई दोस्त ऐप खोलता है (Register)
        if msg.startswith("ONLINE:"):
            friend_name = msg.split(":")[1]
            directory[friend_name] = addr
            print(f"[+] {friend_name} नेटवर्क में आ गया है! (Address: {addr})")
            
        # अगर कोई कॉल मिलाना चाहता है
        elif msg.startswith("CALL:"):
            target = msg.split(":")[1]
            if target in directory:
                # सर्वर कॉलर को उसके दोस्त का एड्रेस दे देगा
                target_addr = directory[target]
                response = f"FOUND:{target_addr[0]}:{target_addr[1]}"
                server.sendto(response.encode('utf-8'), addr)
                print(f"[*] कॉल कनेक्ट की जा रही है... -> {target}")
            else:
                # यहाँ हमने एरर को ठीक कर दिया है
                server.sendto("ERROR: दोस्त अभी ऑफलाइन है!".encode('utf-8'), addr)

# सर्वर को स्टार्ट करने का कमांड
if __name__ == "__main__":
    start_network_brain()