import os

def commit(days):
    if days<1:
        return os.system('git push')
    else:
        dates = f'{days} days ago'

        with open('data.txt','a') as file:
            file.write(f'{dates}\n')

            os.system('git add *')

            os.system('git commit --date="'+dates+'" -m "commits"')
            return days*commit(days-1)

commit(455)