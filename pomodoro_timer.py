from tqdm import tqdm
from time import sleep
import argparse
from pygame import mixer

def timer(total_minutes:int = 25)-> None:
    """
    Gets the total_minutes you want to use the pomodoro clock for.
    """

    for i in tqdm(range(total_minutes*60)):
        sleep(1)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-m" ,"--minutes", help="Get the number of minutes for pomodoro",
                    type=int)
    args = parser.parse_args()
    if args.minutes:
        timer(int(args.minutes))
    else:
        timer() # default 25 minutes
    # play a beep sound
    mixer.init()
    sound = mixer.Sound('./small-bell-ring-01a.wav') ### From https://www.soundjay.com/bell-sound-effect.html
    sound.play()
    print(f"Congratulations, You did {args.minutes} minutes of focused work!!!")
    
