import zipfile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except Exception:
    compression = zipfile.ZIP_STORED

from zip_infolist import print_info


print("----------\nCreate archive")
zf = zipfile.ZipFile("zipfile_append.zip", mode='w')
try:
    zf.write('random_text.txt')
finally:
    zf.close()

print()
print_info('zipfile_append.zip')


print('--------------\nAppending to archive.')
zf = zipfile.ZipFile('zipfile_append.zip', mode='a')
try:
    zf.write('random_text.txt', arcname='random_text_compressed.txt',
             compress_type=compression)
finally:
    zf.close()

print()
print_info('zipfile_append.zip')