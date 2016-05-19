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
    print("--------------\nCreate archive")
    zf = zipfile.ZipFile("tmp.zip", mode='w')
    try:
        zf.write('random_text.txt')
        zf.write('random_text.txt', arcname='random_text_compressed.txt',
                 compress_type=compression)
    finally:
        zf.close()
    return zf.filename


def copy_archive(zipfile_name):
    print('--------------\nCopy "%s"\n--------------' % zipfile_name)

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

            with os.popen(
                    'find . -name "*.png" -exec '
                    'pngquant --ext ".png" --force 16 {} \;') as file_:
                console_run_result = file_.read()

            if console_run_result:
                raise Exception('Failed to perform PNG compression')

            names_to_copy = zf_copy_source.namelist()
            for name in names_to_copy:
                    zf_copy_to.write(name, compress_type=compression)

    except Exception:
        os.remove(zf_copy_to.filename)

    finally:
        os.chdir(curr_cwd)
        zf_copy_source.close()
        zf_copy_to.close()

    if os.path.exists(zf_copy_to.filename):
        print('Done => "%s"' % zf_copy_to.filename)
        print('--------------')
        # print_info(zf_copy_to.filename)
        # print('--------------')

        # TODO: Delete cleanup
        # print("Do cleanup...")
        # os.remove(zf_copy_to.filename)
    else:
        raise FileExistsError("Failed to copy archive")


if __name__ == "__main__":
    name_to_copy = 'png_html_page.zip'
    copy_archive(name_to_copy)
