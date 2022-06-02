import socket
import threading
import time
is_stop = False
def recv_infor(s):
    while True:
        try:
            data = s.recv(1024) 
            infor  = data.decode()
            infor_list = infor.split("|*|")
            print("来自用户id为: {0}  的消息：\n\t{1}".format(infor_list[0],infor_list[1]))
            time.sleep(0.3)
        except:
            break         
id = input("请输入用户 id：")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('103.46.128.53',16836))

s.send(id.encode())
t = threading.Thread(target=recv_infor,args=(s,))
t.start()
while True:
    data = input("输入要发送消息：")
    data_user = list(input("输入要接受的用户空格分开：").split(" "))
    string = data + "|*|" + id +"|*|"+"|*|".join(data_user)
    s.send(string.encode())
    try:
        if int(data) == -1:
            is_stop = True
            break
    except:
        pass
s.close()
print("已于服务器断开连接")       