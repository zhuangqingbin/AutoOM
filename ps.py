import psutil
import datetime
# 获取系统性能信息【CPU、内存、磁盘、网络】

## CPU信息
### User Time, 执行用户进程的时间百分比
### System Time, 执行内核进程和中断的时间百分比
### Wait IO, 由于IO等待而使CPU处于idle（空闲）状态的时间百分比
### Idle, CPU处于idle状态的时间百分比

# 使用cpu_times获取CPU完整信息，需要显示所有逻辑CPU信息，指定percpu=True即可
psutil.cpu_times() # 几个之和
psutil.cpu_times(percpu=True) # 单个显示
# 获取CPU的逻辑个数，默认logical为True
psutil.cpu_count()
# 获取CPU的物理个数
psutil.cpu_count(logical = False)

## 内存信息
### total 内存总数
### used 已使用内存数
### free 空闲内存数
### buffers 缓冲使用数
### cache 缓存使用数
### swap 交换分区使用数
psutil.virtual_memory() # 获取内存完整信息
psutil.swap_memory() # 获取SWAP分区信息

## 磁盘信息
### 磁盘利用率
psutil.disk_usage()
### 磁盘IO信息[read_count读IO数、write_count写IO数、IO读字节数read_bytes、
### IO写字节数write_bytes、磁盘读时间read_time、磁盘写时间write_time]
psutil.disk_partitions() # 获取磁盘完整信息
psutil.disk_io_counters() # 获取硬盘总的IO个数、读写信息
psutil.disk_io_counters(perdisk=True) # 获取单个硬盘的IO个数、读写信息

## 网络信息
### bytes_sent 发送字节数
### bytes_recv 接收字节数
### packet_sent 发送数据包数
psutil.net_io_counters() # 获取网络总的IO信息
psutil.net_io_counters(pernic=True) # 获取每个网络接口的IO信息

## 其他系统信息
psutil.users() # 返回当前登录系统的用户信息
psutil.boot_time() # 开始时间
datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

# 系统进程管理
## 进程信息
psutil.pids() # 列出所有进程的PID
p = psutil.Process(psutil.pids()[0]) # 实例化一个Process对象，参数为一进程PID
p.name() # 进程名
p.exe() # 进程的bin路径
p.cwd() # 进程的工作目录的绝对路径
p.status() # 进程状态
p.create_time() # 进程创建时间，时间戳格式
p.uids() # 进程uid信息
p.gids() # 进程gid信息
p.cpu_times() # 进程CPU时间信息，包括user、system两个CPU时间
p.memory_percent() # 进程内存利用率
p.memory_info() # 进程内存rss、vms信息
p.io_counters() # 进程IO信息，包括读写IO数及字节数
p.connections() # 返回打开进程socket的namedutples列表，包括fs、family、laddr等信息
p.num_threads() # 进程开启的线程数

## popen类的使用 获取用户启动的应用程序进程信息
from subprocess import PIPE
p = psutil.Popen()