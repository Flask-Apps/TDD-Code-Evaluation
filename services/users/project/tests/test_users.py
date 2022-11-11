import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service"""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""

        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode()) # json -> dict
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])
    
    def test_add_user(self):
        '''Ensure a new user can be added to the database'''
        # print('*'*25)
        # print(self.client)
        # print(self.client.__dir__())
        # print('*'*25)
        with self.client:
            response = self.client.post(
                '/users', # /users route
                data=json.dumps({ # dict -> json string
                    'username': 'mikeyy',
                    'email': 'mikeyy@tokyo.com'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('mikeyy@tokyo.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        '''Ensure error is thrown if the JSON object is empty'''
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        '''
        Ensure error is thrown if the JSON object doesnot have a username key
        '''
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(
                    {
                        'email': 'mikeyy@tokyo.com'
                    }
                ),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        '''
        Ensure error is thrown if the email already exists
        '''
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'mikeyy',
                    'email': 'mikeyy@tokyo.com'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username':'mikeyy',
                    'email': 'mikeyy@tokyo.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Sorry. That email already exists', data['message']
            )
            self.assertIn('fail', data['status'])

if __name__ == "__main__":
    unittest.main()
