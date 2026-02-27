import os
import shutil

files = os.listdir("target")

for filename in files:
    path = os.path.join("target",filename)

    if os.path.isfile(path):
        name,ext = os.path.splitext(filename)

        os.makedirs(f'target/{ext}', exist_ok = True) 

        shutil.move(f'target/{filename}',f'target/{ext}/{filename}')