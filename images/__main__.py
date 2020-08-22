import os
import sys
from shutil import copyfile, make_archive

from PIL import Image

API = ""
URL = ""
service_credencials = {}


def convert_images_to_jpg(path_in, path_out):
    for infile in os.listdir(path_in):
        f, e = os.path.splitext(infile)
        outfile = f + ".jpg"
        if infile != outfile:
            try:
                with Image.open(path_in + infile) as im:
                    rgb_im = im.convert('RGB')
                    rgb_im.save(path_out + outfile)
            except OSError:
                print("cannot convert", infile)
        else:
            copyfile(path_in + infile, path_out + infile)

# Ensure same format
path = "/tmp/home/monthly/daily"

os.makedirs('converted/percevejo_marrom/')
os.makedirs('converted/percevejo_pequeno/')
os.makedirs('converted/percevejo_verde/')
os.makedirs('converted/lagarta/')
os.makedirs('converted/negative/')
convert_images_to_jpg(path_in='data/percevejo_marrom/', path_out='converted/percevejo_marrom/')
convert_images_to_jpg(path_in='data/percevejo_pequeno/', path_out='converted/percevejo_pequeno/')
convert_images_to_jpg(path_in='data/percevejo_verde/', path_out='converted/percevejo_verde/')
convert_images_to_jpg(path_in='data/lagarta/', path_out='converted/lagarta/')
convert_images_to_jpg(path_in='data/negative/', path_out='converted/negative/')

make_archive('upload/percevejo_marrom', 'zip', 'converted/percevejo_marrom')
make_archive('upload/percevejo_pequeno', 'zip', 'converted/percevejo_pequeno')
make_archive('upload/percevejo_verde', 'zip', 'converted/percevejo_verde')
make_archive('upload/lagarta', 'zip', 'converted/lagarta')
make_archive('upload/negative', 'zip', 'converted/negative')
# Resize files

