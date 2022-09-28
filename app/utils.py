import uuid, os
from sharyx.settings import UPLOADS_PATH
from app.models import Uploads
from sharyx.settings import logger

def rename_upload(file):
    # TODO: maybe change uuid in the future
    # new_name is renamed to new uuid4 hex, and we are also giving it the old extension
    new_name = f"{uuid.uuid4().hex}.{file.name.split('.').pop()}"

    path = os.path.join(UPLOADS_PATH, new_name)

    # checking if there is any file with the name we are about to use for renaming, in the uploads directory, if there is not, rename and upload
    if not os.path.isfile(path):
        file.name = new_name
        return Uploads.objects.create(name=new_name, uploaded_file=file), file.name, logger.info(f"uploaded file. name={file.name}, size={round(os.path.getsize(path) / (1024 * 1024), 2)} MB")
    else:
        rename_upload(file)