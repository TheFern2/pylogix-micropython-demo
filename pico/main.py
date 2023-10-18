# from pylogix import PLC
# import time
#
# comm = PLC('192.168.0.89', 2)
# tag = 'BaseBOOL'
#
# while True:
#     ret = comm.Read(tag)
#     print(ret.Value)
#     comm.Write(tag, True)
#     time.sleep(2)
#     ret = comm.Read(tag)
#     print(ret.Value)
#     comm.Write(tag, False)
#     time.sleep(2)


def hello(name):
    print("Hello {}".format(name))
