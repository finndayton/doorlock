# CLI interface with our doorlock
MARGIN = 100 # absolute version
MAX_ATTEMPTS = 3
PUNISH_TIME = 1000 * 1

from doorlock import DoorLock

def main():
    doorlock = DoorLock(margin = MARGIN, max_attempts = MAX_ATTEMPTS, punish_time = PUNISH_TIME)
    doorlock.set_knock()
    doorlock.poll()

if __name__ == "__main__":
    main()