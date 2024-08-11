import signal
import time
import sys

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
    except EOFError:
        sys.exit(0)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


def parse_knock(times: list[float]) -> list[float]:
    result = []
    for i in range(len(times) - 1):
        result.append(round(times[i + 1] - times[i], 2))
    
    # normalize 
    # result = [round(n / min(result), 2) for n in result]
    return result