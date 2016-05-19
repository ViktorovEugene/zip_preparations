import os
import tempfile

with tempfile.TemporaryDirectory(suffix='_zip') as tmpdirname:
    print('created temporary directory', tmpdirname)
    input('We well add some file to it.')
    temp_file_name = tmpdirname + "/foo.txt"
    with open(temp_file_name, 'w')as f_:
        f_.write('some content')
    print(os.listdir(tmpdirname))
    input('----------\nCheck it!')


print('Finish!')