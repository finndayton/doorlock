# CLI interface with our doorlock
MARGIN = 100 # absolute version
MAX_ATTEMPTS = 3
PUNISH_TIME = 1000 * 1

import argparse
import sys
from doorlock import DoorLock

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--margin', type=int, default=100, help='Margin value for the door lock')
    parser.add_argument('--max-attempts', type=int, default=3, help='Maximum number of attempts allowed')
    parser.add_argument('--punish-time', type=int, default=1000 * 1, help='Punishment time in seconds for failed attempts')

    args = parser.parse_args()
    doorlock = DoorLock(margin=args.margin, max_attempts=args.max_attempts, punish_time=args.punish_time)

    # basic CLI interface
    while True:
        user_input = input("Welcome home! Options: 'set-knock', 'attempt-knock', 'exit': ").strip().lower()

        if user_input == 'set-knock':
            doorlock.set_knock()
        elif user_input == 'attempt-knock':
            doorlock.poll()
        elif user_input == 'exit':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()