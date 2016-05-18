import os
import zipfile


def get_zips_png_file_names(zip_object):
    return [name for name in zip_object.namelist() if name[-4:] == '.png']


def check_zip_names_on_archive_bomb(zip_object, names_to_check):
    total_size_diff = 0
    for info in (info for info in zip_object.infolist()
                 if info. filename in names_to_check):
        total_size_diff += info.file_size - info.compress_size
    print('\tTotal size diff:\t', total_size_diff, 'bytes')
    if total_size_diff > 10 ** 9:
        raise MemoryError


if __name__ == "__main__":
    # search_zip_for_png('python_html.zip')
    # zf = zipfile.ZipFile('python_html_no_png.zip', 'r')
    # zf = zipfile.ZipFile('python_html.zip', 'r')
    zf = zipfile.ZipFile('png_html_page.zip', 'r')
    png_files = get_zips_png_file_names(zf)
    # print(png_files)
    print(check_zip_names_on_archive_bomb(zf, png_files))
    # get_zip_infolist('python_html_no_png.zip')
