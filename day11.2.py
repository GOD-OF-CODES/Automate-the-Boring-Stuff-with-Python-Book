#mclip.py- A multi-clipboard program
text={'agree':'yes i agree. that sounds fine to me.',
      'busy': 'sorry, can we do this later.',
      'upsell':'woudl you consider making it a monthly donation?'}
import sys, pyperclip
if len(sys.argv)<2:
    print('Usage: python day11.2[keyphrase] - copy phrase text')
    sys.exit
keyphrase=sys.argv[1]