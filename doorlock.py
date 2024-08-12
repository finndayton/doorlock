# NEXT STEPS
# 1. ctrl + D
# 2. Proper CLI. 
# 3. TIMEOUT error edge case
# 4. Generate code by averaging two sequences

import math
from util import *

class DoorLock:
    # margin: buffer time in milliseconds
    # max_attempts: number of trys before device freezes for punish_time
    # punish_time: freeze time, in milliseconds
    def __init__(self, margin: int, max_attempts: int, punish_time: int):
        self.seq : list[int] = None
        
        self.margin = margin
        self.max_attempts = max_attempts
        self.punish_time = punish_time

    def unlock(self) -> None:
        print("""
            *******************************
            *                             *
            *       Door unlocked!        *
            *                             *
            *******************************
        """)

    # actively wait and listen for a door knock
    def poll(self) -> None:
        if not self.seq:
            print("you must first set a knock sequence")
            return

        attempts = 0
        while True:
            if self.wait_and_check_seq():
                self.unlock()
                attempts = 0
                return
            else: 
                print("Wrong password")
                attempts += 1
                if attempts >= self.max_attempts: 
                    attempts = 0
                    self.punish()
                    return

    # block new attempts, block the user from new attempts for PUNISH_TIME
    def punish(self) -> None:
        increment = 10 # 10 ms increment
        iters = self.punish_time / increment
        for i in range(int(iters)):
            if check_knock(increment): 
                print(f"stop! new knocks are disabled for {(self.punish_time - i * increment) / 1000} more seconds")
            elif i % 100 == 0: 
                print(f"new knocks are disabled for {(self.punish_time - i * increment) / 1000} more seconds")
        print("lock re-ennabled")

    # checks one sequence of knocks. Quits early if sequence is wrong already
    def wait_and_check_seq(self) -> bool:
        
        # detect the first knock. There could be a long pause before we here it!        
        while True: 
            if check_knock(10 * 1000): break # use check_knock() to poll for the first knock

        for i in range(len(self.seq)):
            # if the knock is heard before the expected delay 
            if check_knock(self.seq[i] * 1000 - self.margin): return False

            # if no knock in your window, return false
            if not check_knock(self.margin * 2): return False
        return True
    
    def set_knock(self) -> None:
        print("Please knock your sequence. When you are done, hit enter")
        seq = []
        while True: 
            try:             
                user_input = input()  # Wait for user input
                if user_input == "":
                    self.seq = parse_knock(seq)
                    print(f"Knock sequence recorded: {self.seq}")                    
                    return  # Exit the loop if Enter is pressed without any input
            except KeyboardInterrupt: 
                seq.append(time.time())