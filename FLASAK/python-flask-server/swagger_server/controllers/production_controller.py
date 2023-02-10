import connexion
import six

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.models.production import Production  # noqa: E501
from swagger_server import util


def add_new_process(body):  # noqa: E501
    """Add a new process to the list

     # noqa: E501

    :param body: Production line that needs to add at the list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Production.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_pets_by_tags(tags):  # noqa: E501
    """Finds Pets by tags

    Muliple tags can be provided with comma separated strings. Use         tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def find_production_by_status(status):  # noqa: E501
    """Finds Production lines by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def get_production_by_id(productionId):  # noqa: E501
    """Find production by ID

    Returns a single production # noqa: E501

    :param productionId: ID of production to return
    :type productionId: int

    :rtype: Production
    """
    return 'do some magic!'


def update_pet_with_form(productionId, name=None, status=None):  # noqa: E501
    """Updates a pet in the store with form data

     # noqa: E501

    :param productionId: ID of production that needs to be updated
    :type productionId: int
    :param name: Updated name of the production
    :type name: str
    :param status: Updated status of the production
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def update_production(body):  # noqa: E501
    """Update an existing production

     # noqa: E501

    :param body: Productin that needs to be added to the list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Production.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
