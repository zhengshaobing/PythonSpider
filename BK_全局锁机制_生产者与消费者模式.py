import threading, random, time


Qmoney = 1000
# Value_data = 0
gLock = threading.Lock()
gTotal_times = 10
gtimes = 0
#
#
# class CountThread(threading.Thread):
#     def run(self):
#         global Value_data
#         # 锁主要用于:修改全局变量的地方
#         gLock.acquire()
#         for x in range(1000000):
#             Value_data += 1
#         gLock.release()
#         print(Value_data)
#
#
# def main():
#     for x in range(2):
#         t = CountThread()
#         t.start()

'''
这种方法十分占用cpu资源，
不推荐使用

'''
# class Producer(threading.Thread):
#     def run(self):
#         global Qmoney
#         global gtimes
#         global gTotal_times
#         while 1:
#             money = random.randint(100, 1000)
#             gLock.acquire()
#             if gtimes >= gTotal_times:
#                 gLock.release()
#                 break
#             Qmoney += money
#             gtimes += 1
#             gLock.release()
#             print('生产了%d元，剩余了%d元'%(money, Qmoney))
#             time.sleep(0.5)
#
#
# class Consumer(threading.Thread):
#     def run(self):
#         global Qmoney
#         global gTotal_times
#         global gtimes
#         while 1:
#             money = random.randint(100, 1000)
#             gLock.acquire()
#             if Qmoney >= money:
#                 Qmoney -= money
#                 gLock.release()
#                 print('消费了%d元，剩余了%d元' % (money, Qmoney))
#             else:
#                 #if gtimes > gTotal_times:
#                 gLock.release()
#                 break
#
#             time.sleep(0.5)
#
#
# def main():
#
#     for x in range(1):
#         t = Producer(name='生产者%d'%x)
#         t.start()
#     for x in range(3):
#         t = Consumer(name='消费者%d'%x)
#         t.start()
#
#
# if __name__ == '__main__':
#     main()
