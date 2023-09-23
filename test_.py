import os

dir_name = 'dir'
file_name = 'file_'

os.mkdir(dir_name)
#os.makedirs(dir_name, exist_ok=True)

for i in range(1,101):
    file_path = './' + dir_name + '/' + file_name + str(i).zfill(5) + '.txt'
    with open(file_path, 'w') as f:
        f.write('')
#        f.write('ファイル_' + str(i).zfill(5))
#        f.write('メモ書き')

