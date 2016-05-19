import datetime
import zipfile


def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print(info.filename,
              '\tModified:\t%s' % datetime.datetime(*info.date_time),
              '\tCompressed:\t%s bytes' % info.compress_size,
              '\tUncompressed:\t%s bytes' % info.file_size,
              sep='\n')

if __name__ == '__main__':
    print_info('example.zip')