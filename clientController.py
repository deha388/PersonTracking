import threading
import time
from clients import client1, client2, client3, client4, client5, client6, client7, client8


#per client is running 2 minute so for the 8 client is going the progress to long
#threading is helping to us for the execute per client in same time

def method_1():
    def run():
        threading.Thread(target=function_a, args=()).start()
        threading.Thread(target=function_b, args=()).start()
        threading.Thread(target=function_c, args=()).start()
        threading.Thread(target=function_d, args=()).start()
        threading.Thread(target=function_e, args=()).start()
        threading.Thread(target=function_f, args=()).start()
        threading.Thread(target=function_g, args=()).start()
        threading.Thread(target=function_h, args=()).start()

    def function_a():
        client1.runClient1()
        time.sleep(0.1)  # Add some delay here

    def function_b():
        client2.runClient2()
        time.sleep(0.1)  # and here

    def function_c():
        client3.runClient3()
        time.sleep(0.1)  # and here

    def function_d():
        client4.runClient4()
        time.sleep(0.1)  # and her

    def function_e():
        client5.runClient5()
        time.sleep(0.1)  # and here

    def function_f():
        client6.runClient6()
        time.sleep(0.1)  # and here

    def function_g():
        client7.runClient7()
        time.sleep(0.1)  # and her

    def function_h():
        client8.runClient8()
        time.sleep(0.1)  # and here

    run()
