import os
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

    # copy_name = zipfile_name[:-4] + "(copy)" + zipfile_name[-4:]
    # zf_copy_to = zipfile.ZipFile(copy_name, mode='x')

    with tempfile.TemporaryDirectory(suffix='_zip') as tmpdirname:
        zf_copy_source.extractall(
            tmpdirname,
            zf_copy_source.namelist()
        )
        input("Extraction done! look at it!\n%s" % os.listdir(tmpdirname))

if __name__ == "__main__":
    name_to_copy = create_archive()
    copy_archive(name_to_copy)
