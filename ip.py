from IPy import IP

# 通过version方法可以区分IPv4和IPv6
IP('10.0.0.0/8').version() # 4 代表IPv4类型
IP('::1').version() # 6 代表IPv6类型

ip = IP('192.168.0.0/16')
print(ip.len()) # 输出 192.168.0.0/16 网段的IP个数
for i in ip:  # 输出 192.168.0.0/16 网段的所有IP清单
    print(i)


ip = IP('192.168.1.20')
ip.reverseName() # 反向解析地址格式
ip.iptype() # 为私网类型 PRIVATE
IP('8.8.8.8').iptype() # 为公网类型 PUBLIC
IP('8.8.8.8').int() # 转换成整型格式
IP('8.8.8.8').strHex() # 转换十六进制格式
IP('8.8.8.8').strBin() # 转换二进制格式

# 根据IP与掩码生成网段格式
print(IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.1.0/255.255.255.0', make_net=True))
print(IP('192.168.1.0-192.168.1.255', make_net=True))


def a():
    print('d')

def a1():
    return a()