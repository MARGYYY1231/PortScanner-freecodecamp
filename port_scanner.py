import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    try:
        ip = socket.gethostbyname(target)
        for port in range(port_range[0], port_range[1]):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    except:
        print("Hello")

    return(open_ports)