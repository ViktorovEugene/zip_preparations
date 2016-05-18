import os
import zipfile
import tempfile


def form_valid(form):

    zip_ref = zipfile.ZipFile(self.request.FILES['archive'], 'r')
    if not os.path.exists('/tmp/tmpdir'):
        os.mkdirs('/tmp/tmpdir')
    zip_ref.extractall('/tmp')
    zip_ref.close()

    print(zip_ref.filename)

    return super(CompressView, self).form_valid(form)