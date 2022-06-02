import socket
import threading

is_server_stop=False
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',80))
s.listen(3)

def stop_server():
    input("输入任意值停止服务器:")
    s.close()
    conn.close()
    global is_server_stop
    is_server_stop=True
    
    
t = threading.Thread(target=stop_server)
t.start()

while is_server_stop==False:
    try:   
        conn,address = s.accept()
        data = conn.recv(800)
        infor = data.decode()
        file_name = infor.split(" ")[1][1:]
        header = "HTTP/1.0 200 OK\r\n\r\n"
        if file_name =='':
            file_name ="index.html"
        try:
            file = open(file_name,"rb")
        except:
            file = open("error.html","rb")
            header = "HTTP/1.0 404 NOT FOUND\r\n\r\n"
        finally:
            conn.send(header.encode())
            conn.send(file.read())
            file.close()
        conn.close()
    except:  
        if is_server_stop==True:
           break
        pass
        
print("服务器已停止...")