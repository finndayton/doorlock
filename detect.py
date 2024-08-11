# NEXT STEPS
# 1. Listen for the relative not absolute times 
    # a) listen for all the knocks
    # b) divide by lowest interval. 
    # c) enforce buffer logic (on normalized intervals)
# 2. TIMEOUT error edge case
# 3. Generate code by averaging two sequences
# 4. Classify things, flags, etc

import math
from util import unlock, check_knock
BUF = 100 # absolute version
BUF_REL = 0.25 # 0.0 - 1.0 | represents a percentage
MAX_ATTEMPTS = 3
PUNISH_TIME = 1000 * 10
MAX_GAP = 10 * 1000


def main(seq):
    attempts = 0
    while True:
        if wait_and_check_seq(seq):
            unlock()
            attempts = 0
        else: 
            print("Wrong password")
            attempts += 1
            if attempts >= MAX_ATTEMPTS: 
                attempts = 0
                punish(PUNISH_TIME)

# block new attempts, block the user from new attempts for PUNISH_TIME
def punish(punish_time: int) -> None:
    increment = 10 # 1 ms increment
    iters = punish_time / increment
    for i in range(int(iters)):
        if check_knock(increment): 
            print(f"stop! new knocks are disabled for {(punish_time - i * increment) / 1000} more seconds")
        elif i % 100 == 0: 
            print(f"new knocks are disabled for {(punish_time - i * increment) / 1000} more seconds")
    print("lock re-ennabled")

# checks one sequence of knocks. Quits early if sequence is wrong already
def wait_and_check_seq(seq: list[int]) -> bool:
    # detect the first knock. There could be a long pause before we here it!
    
    while True: # poll for the first knock
        if check_knock(10 * 1000): break

    for i in range(len(seq)):
        print(f'here, checking {seq[i]}')

        # if the knock is heard before the expected delay 
        if check_knock(seq[i] - BUF): return False

        # if no knock in your window, return false
        if not check_knock(BUF * 2): return False


    return True



if __name__ == "__main__":
    seq2 = [0.40 * 1000, 0.20 * 1000, 0.20 * 1000, 0.40 * 1000, 0.85 * 1000, 0.45 * 1000]
    main(seq2)
