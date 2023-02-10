import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util


def delete_pet(petId, api_key=None):  # noqa: E501
    """Deletes a pet

     # noqa: E501

    :param petId: Pet id to delete
    :type petId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(petId, additionalMetadata=None, file=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param petId: ID of pet to update
    :type petId: int
    :param additionalMetadata: Additional data to pass to server
    :type additionalMetadata: str
    :param file: file to upload
    :type file: werkzeug.datastructures.FileStorage

    :rtype: ApiResponse
    """
    return 'do some magic!'
