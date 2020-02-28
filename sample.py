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

            file.write(f'{dates}\n\n')
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "commits"')
            time.sleep(1)
            os.system('git push')
            time.sleep(1)

            file.write(f'{dates}\n\n\n')
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "updates"')
            time.sleep(1)
            os.system('git push')
            time.sleep(1)

            file.write(f'{dates}\n\n\n\n')
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "version change"')
            time.sleep(1)
            os.system('git push')
            time.sleep(1)

            file.write(f'{dates}\n\n\n\n\n')
            os.system('git add *')
            os.system('git commit --date="'+dates+'" -m "final changes"')
            time.sleep(1)
            os.system('git push')
            time.sleep(1)
            return days*commit(days-1)

commit(750)