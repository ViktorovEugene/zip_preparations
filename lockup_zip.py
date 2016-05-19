import zipfile


def get_zips_png_file_names(zip_object):
    return [name for name in zip_object.namelist() if name[-4:] == '.png']


def check_zip_names_on_archive_bomb(zf, names_to_check):
    total_size_diff = 0
    for info in map(zf.getinfo, names_to_check):
        total_size_diff += info.file_size - info.compress_size
    print('\tTotal size diff:\t', total_size_diff, 'bytes')
    if total_size_diff > 10 ** 9:
        raise MemoryError


if __name__ == "__main__":
    zf = zipfile.ZipFile('png_html_page.zip', 'r')
    png_files = get_zips_png_file_names(zf)
    check_zip_names_on_archive_bomb(zf, png_files)
