import os

from projects.models import Project
from core.services.minio_admin import minio_admin
from core.services.minio_client import MinioClient
from projects.services.project_cloud_storage import project_minio


def init_project_cloud_storage(project: Project):
    access_key, secret_key = minio_admin.add_access_key()
    project.s3_access_key = access_key
    project.s3_secret_key = secret_key
    project.save()

def project_upload_file(project: Project):
    project_minio.upload_file(
        project=project,
        bucket_name=str(project.id),
        object_name=str(os.path.basename(project.file.name)),
        file_path=project.file.path
    )

