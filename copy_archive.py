import zipfile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except Exception:
    compression = zipfile.ZIP_STORED

from zip_infolist import print_info


def create_archive():
    print("----------\nCreate archive")
    zf = zipfile.ZipFile("zipfile_append.zip", mode='w')
    try:
        zf.write('random_text.txt')
        zf.write('random_text.txt', arcname='random_text_compressed.txt',
                 compress_type=compression)
    finally:
        zf.close()
    print()
    print_info('zipfile_append.zip - DONE!\n---------------')


def copy_archive(zipfile_name):
    print('---------------\n'
          'Copy "%s"' % zipfile_name)
    copy_name = zipfile_name[:-4] + "(copy)" + zipfile_name[-4:]
    zf = zipfile.ZipFile(copy_name, mode='x')
    try:
        zf.write('random_text.txt', arcname='random_text_compressed.txt',
                 compress_type=compression)
    finally:
        zf.close()

print()
print_info('zipfile_append.zip')