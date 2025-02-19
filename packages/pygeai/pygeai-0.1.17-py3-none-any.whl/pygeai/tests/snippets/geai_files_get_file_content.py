from pygeai.core.base.models import Organization, Project
from pygeai.core.files.managers import FileManager
from pygeai.core.files.models import UploadFile, File

organization = Organization(id="4aa15b61-d3c7-4a5c-99b8-052d18a04ff2")
project = Project(id="1956c032-3c66-4435-acb8-6a06e52f819f")
file = File(id="7433c276-81e8-405e-9990-82158326f839")

file_manager = FileManager()

response = file_manager.get_file_content(organization_id=organization.id, project_id=project.id, file_id=file.id)
print(response)
