import signal
import time

def unlock() -> None:
    print("door unlocked!")

class TimeoutException(Exception):
    pass

# called when the alarm expires and no knock heard!
def handler(signum, frame):
    raise TimeoutException

# knock is detected before time runs out -> True
# no knock detected before time runs out -> False
def check_knock(timeout: int) -> bool:    
    # poll for time ms checking for a KEY_INTERUPT.
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, timeout / 1000)
        while True:
            time.sleep(0.1)
    except TimeoutException:
        return False
    except KeyboardInterrupt:        
        return True 
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


def parse_knock(times: list[float]) -> list[float]:
    result = []
    for i in range(len(times) - 1):
        result.append(round(times[i + 1] - times[i], 2))
    return result

def generate_knock():
    print("press enter and then knock your sequence. When you are done, hit enter")
    input()
    seq = []
    while True: 
        try:             
            user_input = input()  # Wait for user input
            if user_input == "":
                print("Knock sequence recorded:")
                print(parse_knock(seq))
                print("set a new lock? YES / NO")
                user_input = input()                    
                break  # Exit the loop if Enter is pressed without any input
        except KeyboardInterrupt: 
            seq.append(time.time())



def main(time):
    generate_knock()
    # if check_knock(time):
    #     print("Knock detected!")
    # else: 
    #     print("Knock not detected!")

if __name__ == "__main__":
    main(time=2000) 
