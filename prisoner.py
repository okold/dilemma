# ITERATED PRISONER'S DILEMMA - PRISONER
# February 2022
# Olga Koldachenko

from multiprocessing import Process
from multiprocessing.connection import Client
import time

class Prisoner(Process):
    def __init__(self, address, strategy):
        Process.__init__(self, daemon=True)
        self.address = address
        self.strategy = strategy

    def run(self):
        conn = Client(self.address)
        self.name = "Prisoner " + str(conn.recv()) # gets the player number from the server

        print(time.asctime(), ">", self.name, "> has strategy", self.strategy)

        while True:
            msg = conn.recv()

            if msg == "close":
                break
            else:
                #time.sleep(random.choice(range(1,4)))
                action = self.strategy(msg)

                if action == True:
                    print(time.asctime(), ">", self.name, "> stay silent")
                else:
                    print(time.asctime(), ">", self.name, "> betray")
                
                conn.send(action)

        conn.close()