# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.models.production import Production  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductionController(BaseTestCase):
    """ProductionController integration test stubs"""

    def test_add_new_process(self):
        """Test case for add_new_process

        Add a new process to the list
        """
        body = Production()
        response = self.client.open(
            '/v2/production',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_pets_by_tags(self):
        """Test case for find_pets_by_tags

        Finds Pets by tags
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open(
            '/v2/production/findByTags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_production_by_status(self):
        """Test case for find_production_by_status

        Finds Production lines by status
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/v2/production/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_production_by_id(self):
        """Test case for get_production_by_id

        Find production by ID
        """
        response = self.client.open(
            '/v2/pet/{petId}'.format(productionId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pet_with_form(self):
        """Test case for update_pet_with_form

        Updates a pet in the store with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/v2/pet/{petId}'.format(productionId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_production(self):
        """Test case for update_production

        Update an existing production
        """
        body = Production()
        response = self.client.open(
            '/v2/production',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
