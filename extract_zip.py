import os
import zipfile

from lockup_zip import get_zips_png_file_names


def extract_file(zf, file_name, path_extract_to):
    return zf.extract(file_name, path=path_extract_to)

if __name__ == "__main__":
    zf = zipfile.ZipFile('png_html_page.zip', 'r')
    png_files = get_zips_png_file_names(zf)
    print(extract_file(zf, png_files[0], os.getcwd() + '/tmp'))
