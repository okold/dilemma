# ITERATED PRISONER'S DILEMMA - SERVER
# February 2022
# Olga Koldachenko

from multiprocessing import Process
from multiprocessing.connection import Listener
import time

class DilemmaServer(Process):
    def __init__(self, address, num_rounds):
        Process.__init__(self, daemon = True, name="Server")
        self.address = address
        self.num_rounds = num_rounds

    class Prisoner():
        def __init__(self, name, conn):
            self.name = name
            self.conn = conn
            self.score = 0
            self.last_move = None

    def run(self):
        print("------------------------------------------------------------------")
        listener = Listener(self.address)
        player_list = []

        # connects to players
        for i in range(0,2):
            print(time.asctime(), ">", self.name, "> waiting for Prisoner", i)
            conn = listener.accept()
            conn.send(i) #sends player number upon accepting
            player_list.append(self.Prisoner(i, conn))
        
        time.sleep(2)

        # loops through the rounds
        for round in range(0, self.num_rounds):
            print()
            print("------------------------------------------------------------------")
            print(time.asctime(), ">", self.name, "> ROUND", round, "...!")
            

            waiting_list = []

            # informs the players of the next round
            for i in range(0, 2):
                msg = player_list[(i+1)%2].last_move
                player_list[i].conn.send(msg)
                waiting_list.append(player_list[i])
            
            # waits for all players to respond
            while waiting_list != []:
                for player in waiting_list:
                    if player.conn.poll():
                        msg = player.conn.recv()
                        player.last_move = msg
                        waiting_list.remove(player)

            # calculate scores
            if player_list[0].last_move == player_list[1].last_move:
                if player_list[0].last_move == True:
                    player_list[0].score -= 1
                    player_list[1].score -= 1
                else:
                    player_list[0].score -= 2
                    player_list[1].score -= 2
            else:
                if player_list[0].last_move == True:
                    player_list[0].score -= 3
                else:
                    player_list[1].score -= 3

            print()
            print("\t\t\t\tPrisoner 0:", player_list[0].score, "| Prisoner 1:", player_list[1].score)
            time.sleep(2)

        print()
        if player_list[0].score == player_list[1].score:
            print("\t\t\t\tIt's a tie!")
        elif player_list[0].score > player_list[1].score:
            print("\t\t\t\tPrisoner 0 wins!")
        else:
            print("\t\t\t\tPrisoner 1 wins!")

        for player in player_list:
            player.conn.send("close")
            player.conn.close()
