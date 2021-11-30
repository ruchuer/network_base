import telnetlib, os


os.system("zebra -d;ripd -d;ospfd -d;")
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
tn.write("network 117.0.15.0/24\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 117.0.12.0/24\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 117.0.13.0/24\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 154.0.7.0/24\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("redistribute ospf metric 1\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("end\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("copy running-config startup-config\n".encode('ascii'))
tn.close()
tn = telnetlib.Telnet(host="127.0.0.1", port=2604)
tn.read_until(": ".encode('ascii'))
tn.write("zebra\n".encode('ascii'))
tn.read_until("> ".encode('ascii'))
tn.write("en\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("config t\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("router rip\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("router ospf\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 117.0.15.0/24 area 0\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 117.0.12.0/24 area 0\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 117.0.13.0/24 area 0\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("network 154.0.7.0/24 area 0\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("redistribute rip metric 1\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("end\n".encode('ascii'))
tn.read_until("# ".encode('ascii'))
tn.write("copy running-config startup-config\n".encode('ascii'))
tn.close()
