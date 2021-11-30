import telnetlib, os


os.system("zebra -d;ripd -d;")
tn = telnetlib.Telnet(host="127.0.0.1", port=2602)
tn.read_until(": ".encode('ascii'))
tn.write("zebra\n".encode('ascii'))
tn.read_until("> ".encode('ascii'))
tn.write("en\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("config t\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("router rip\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 117.0.17.0/24\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 154.0.9.0/24\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("end\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("copy running-config startup-config\n".encode('ascii'))
tn.close()
