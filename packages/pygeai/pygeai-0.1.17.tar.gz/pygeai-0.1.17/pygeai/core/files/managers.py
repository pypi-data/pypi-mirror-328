from pygeai.core.base.mappers import ErrorMapper, ResponseMapper
from pygeai.core.base.responses import EmptyResponse
from pygeai.core.files.clients import FileClient
from pygeai.core.files.models import UploadFile, File, FileList
from pygeai.core.files.mappers import FileResponseMapper
from pygeai.core.files.responses import UploadFileResponse


class FileManager:
    """
    Manages file-related operations such as uploading, retrieving, and deleting files
    within an organization and project.
    """

    def __init__(self, api_key: str = None, base_url: str = None, alias: str = "default"):
        self.__client = FileClient(
            api_key,
            base_url,
            alias
        )

    def upload_file(
            self,
            file: UploadFile,
            organization_id: str,
            project_id: str
    ) -> UploadFileResponse:
        """
        Uploads a file to the specified organization and project.

        :param file: UploadFile - The file object containing file path, name, and folder details.
        :param organization_id: str - The ID of the organization to which the file belongs.
        :param project_id: str - The ID of the project under which the file is stored.
        :return: UploadFileResponse - The response object containing the uploaded file details.
        """
        response_data = self.__client.upload_file(
            file_path=file.path,
            organization_id=organization_id,
            project_id=project_id,
            folder=file.folder,
            file_name=file.name,
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = FileResponseMapper.map_to_upload_file_response(response_data)
        return result

    def get_file_data(
            self,
            organization_id: str,
            project_id: str,
            file_id: str
    ) -> File:
        """
        Retrieves metadata of a specific file by its ID.

        :param organization_id: str - The ID of the organization that owns the file.
        :param project_id: str - The ID of the project associated with the file.
        :param file_id: str - The unique identifier of the file.
        :return: File - A file object containing metadata about the requested file.
        """
        response_data = self.__client.get_file(
            organization=organization_id,
            project=project_id,
            file_id=file_id
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = FileResponseMapper.map_to_file(response_data)
        return result

    def delete_file(
            self,
            organization_id: str,
            project_id: str,
            file_id: str
    ) -> EmptyResponse:
        """
        Deletes a file from the specified organization and project.

        :param organization_id: str - The ID of the organization that owns the file.
        :param project_id: str - The ID of the project associated with the file.
        :param file_id: str - The unique identifier of the file to be deleted.
        :return: EmptyResponse - Response indicating the success or failure of the operation.
        """
        response_data = self.__client.delete_file(
            organization=organization_id,
            project=project_id,
            file_id=file_id
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = ResponseMapper.map_to_empty_response(response_data)
        return result

    def get_file_content(
            self,
            organization_id: str,
            project_id: str,
            file_id: str
    ) -> bytes:
        """
        Retrieves the raw content of a specific file.

        :param organization_id: str - The ID of the organization that owns the file.
        :param project_id: str - The ID of the project associated with the file.
        :param file_id: str - The unique identifier of the file.
        :return: bytes - The binary content of the file.
        """
        response_data = self.__client.get_file_content(
            organization=organization_id,
            project=project_id,
            file_id=file_id
        )
        if isinstance(response_data, dict) and "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = response_data
        return result

    def get_file_list(
            self,
            organization_id: str,
            project_id: str
    ) -> FileList:
        """
         Retrieves a list of all files associated with a given organization and project.

        :param organization_id: str - The ID of the organization.
        :param project_id: str - The ID of the project.
        :return: FileList - A list of file objects associated with the organization and project.
        """
        response_data = self.__client.get_file_list(
            organization=organization_id,
            project=project_id
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = FileResponseMapper.map_to_file_list_response(response_data)
        return result

