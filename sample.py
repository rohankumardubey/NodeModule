import os
import time

def commit(days):
    if days<500:
        pass
    else:
        dates = f'{days} days ago'

        with open('data.txt','a') as file:
            file.write(f'{dates}\n')
            print(dates)

            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "commits"')
            file.write(f'{dates}\n\n')
            time.sleep(1)
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "updates"')
            file.write(f'{dates}\n\n\n')
            time.sleep(1)
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "version change"')
            file.write(f'{dates}\n\n\n\n')
            time.sleep(1)
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "final changes"')
            time.sleep(1)
            os.system('git push')
            time.sleep(1)
            return days*commit(days-1)

commit(750)