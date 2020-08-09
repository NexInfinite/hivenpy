from ping3 import ping


def Ping():
    ping_time = ping("api.hiven.io") * 1000
    return ping_time
