import os

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
            os.system('git push')

            return days*commit(days-1)

commit(700)