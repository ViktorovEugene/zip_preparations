import os
import zipfile
import tempfile

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except Exception:
    compression = zipfile.ZIP_STORED

from zip_infolist import print_info
from lockup_zip import get_zips_png_file_names


def copy_archive(zipfile_name):
    print('--------------\nCopy "%s"\n--------------' % zipfile_name)

    zf_copy_source = zipfile.ZipFile(zipfile_name, mode='r')
    zf_abs_path = os.path.abspath(zf_copy_source.filename)
    names_to_copy = get_zips_png_file_names(zf_copy_source)

    curr_cwd = os.getcwd()

    try:
        with tempfile.TemporaryDirectory(suffix='_zip') as tmpdirname:
            zf_copy_source.extractall(tmpdirname, names_to_copy)
            zf_copy_source.close()

            input('Check files!')

            os.chdir(tmpdirname)

            print("Processing PNG files...")
            with os.popen(
                    'find . -name "*.png" -exec '
                    'pngquant --ext ".png" --force 16 {} \;'):
                pass
            input('Check compressed files!')
            print("Update the source archive...")

            with os.popen('zip -r %s %s' %
                          (zf_abs_path, ' '.join(names_to_copy))
                          ) as file_:
                console_run_result = file_.read()

            print("-----------------"
                  '"zip" console call'
                  'VVVVVVVVVVVVVVVVVV',
                  console_run_result,
                  '-----------------', sep='\n')

    finally:
        os.chdir(curr_cwd)
        zf_copy_source.close()



if __name__ == "__main__":
    name_to_copy = 'archive.zip'
    copy_archive(name_to_copy)
