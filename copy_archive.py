import os
from os.path import join
import zipfile
import tempfile

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except Exception:
    compression = zipfile.ZIP_STORED

from zip_infolist import print_info


def create_archive():
    print("----------\nCreate archive")
    zf = zipfile.ZipFile("tmp.zip", mode='w')
    try:
        zf.write('random_text.txt')
        zf.write('random_text.txt', arcname='random_text_compressed.txt',
                 compress_type=compression)
    finally:
        zf.close()
    print_info(zf.filename)
    return zf.filename


def copy_archive(zipfile_name):
    print('---------------\nCopy "%s"' % zipfile_name)

    zf_copy_source = zipfile.ZipFile(zipfile_name, mode='r')

    zf_copy_to = zipfile.ZipFile("(copy)" + zipfile_name, mode='x')

    curr_cwd = os.getcwd()

    try:
        with tempfile.TemporaryDirectory(suffix='_zip') as tmpdirname:
            zf_copy_source.extractall(
                tmpdirname,
                zf_copy_source.namelist()
            )
            os.chdir(tmpdirname)
            files_to_copy = os.listdir()

            for name in files_to_copy:
                    zf_copy_to.write(name, compress_type=compression)

            input("Extraction done! look at it!\n%s" % files_to_copy)
    finally:
        os.chdir(curr_cwd)
        zf_copy_source.close()
        zf_copy_to.close()


if __name__ == "__main__":
    name_to_copy = create_archive()
    copy_archive(name_to_copy)
