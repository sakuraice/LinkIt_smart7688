import telnetlib  
host = '192.168.0.132'  
user = 'root'  
password = '123456'  
commands = ['en',password,'conf t','int fa0/1','switchport mode multi','end']  
tn = telnetlib.Telnet(host)  
tn.read_until("Username:")  
tn.write(user + "n")  
tn.read_until("Password:")  
tn.write(password + "n")  
for command in commands:  
    tn.write(command+'n')  
    tn.write("exitn") 
t = tn.read_all() 
print('111' + t)
print('Finish!')