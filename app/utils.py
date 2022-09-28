import uuid, os
from sharyx.settings import UPLOADS_PATH
from app.models import Uploads

def rename_upload(file):
    # TODO: maybe change uuid in the future
    # new_name is renamed to new uuid4 hex, and we are also giving it the old extension
    new_name = f"{uuid.uuid4().hex}.{file.name.split('.').pop()}"

    # checking if there is any file with the name we are about to use for renaming, in the uploads directory, if there is not, rename and upload
    if not os.path.isfile(os.path.join(UPLOADS_PATH, new_name)):
        file.name = new_name
        return Uploads.objects.create(name=new_name, uploaded_file=file), file.name
    else:
        rename_upload(file)