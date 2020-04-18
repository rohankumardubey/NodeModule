import os
import time

def commit(days):
    if days<1:
        pass
    else:
        dates = f'{days} days ago'

        with open('data.txt','a') as file:
            file.write(f'{dates}\n')
            print(dates)

            os.system('git add *')

            os.system('git commit --date="'+dates+'" -m "commits"')
            os.system('git commit --date="'+dates+'" -m "updates"')
            os.system('git commit --date="'+dates+'" -m "version change"')
            os.system('git commit --date="'+dates+'" -m "final changes"')
            os.system('git push')
            time.sleep(1)
            return days*commit(days-1)

commit(700)