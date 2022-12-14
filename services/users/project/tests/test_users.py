import json
import unittest

from project.tests.base import BaseTestCase
from project.api.models import User
from project import db


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(BaseTestCase):
    """Tests for the Users Service"""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""

        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())  # json -> dict
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
                '/users',  # /users route
                data=json.dumps({  # dict -> json string
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
                    'username': 'mikeyy',
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

    def test_single_user(self):
        '''
        Ensure get single user behaves correctly
        '''
        user = add_user(username='mikeyy', email='mikeyy@tokyo.com')
        # user = User(username='mikeyy', email='mikeyy@tokyo.com')
        # db.session.add(user)
        # db.session.commit()
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('mikeyy', data['data']['username'])
            self.assertIn('mikeyy@tokyo.com', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        '''
        Ensure error is thrown if an id isn't provided
        '''
        with self.client:
            response = self.client.get('users/pow')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("User doesn't exist", data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        '''
        Ensure error is thrown if the id doesnot exist.
        '''
        with self.client:
            response = self.client.get('/users/420')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("User doesn't exist", data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        '''
        Ensure get all users behaves correctly.
        '''
        add_user('mikeyy', 'mikeyy@tokyo.com')
        add_user('toma', 'toma@tokyo.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('mikeyy', data['data']['users'][0]['username'])
            self.assertIn(
                'mikeyy@tokyo.com', data['data']['users'][0]['email']
            )
            self.assertIn('toma', data['data']['users'][1]['username'])
            self.assertIn(
                'toma@tokyo.com', data['data']['users'][1]['email']
            )
            self.assertIn('success', data['status'])

    def test_main_no_users(self):
        '''
        Ensure the main route behaves correctly when no users have been
        added to the database
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>All Users</h1>', response.data)
        self.assertIn(b'<p>No users!</p>', response.data)

    def test_main_with_users(self):
        '''
        Ensure the main route behaves correctly when users have been
        added to the database
        '''
        add_user('mikeyy', 'mikeyy@tokyo.com')
        add_user('toma', 'toma@tokyo.com')
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>All Users</h1>', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'mikeyy', response.data)
            self.assertIn(b'toma', response.data)


if __name__ == "__main__":
    unittest.main()
