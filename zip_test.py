import os
import zipfile


def search_zip_for_png(zip_file_name):
    zf = zipfile.ZipFile(zip_file_name, 'r')
    for name in zf.namelist():
        if name[-4:] == '.png':
            print('"%s" - found PNG in "%s"' % (name.split('/')[-1],
                                                zip_file_name))
            return zf
    print('Not found PNG in "%s"' % zip_file_name)
    return False

if __name__ == "__main__":
    search_zip_for_png('python_html.zip')
    search_zip_for_png('python_html_no_png.zip')
