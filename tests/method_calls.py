import unittest
import os
import sys

class TestMethodCalls(unittest.TestCase):
    """
    Tests a call from each method of GET, POST, PUT, and DELETE. This ensures
    the method calls are working properly (at least the ones in here) and therefore
    data is passing through the library correcly and requester is handling sending
    and receiving calls.
    """
    
    def setUp(self):
        sys.path.append('..')
        
        from odins_spear.api import Api
        # Set up API object
        self.api = Api(base_url=os.getenv("ODIN_URL"), username= os.getenv("ODIN_USERNAME"), 
               password="ODIN_PASSWORD")
        
        self.service_provider_id = os.getenv("TEST_SERVICE_PROVIDER_ID")
        self.group_id = os.getenv("TEST_GROUP_ID")
        self.user_id = os.getenv("TEST_USER_ID")
        
        self.test_user_data = {
            "serviceProviderId": self.service_provider_id,
            "groupId": self.group_id,
            "userId": self.user_id,
            "firstName": "Mark",
            "lastName": "Corrigan",
        }        
        
    def test_post_user(self):
        """ Builds test user in test environment and checks response.
        """
        self.assertEquals(
            self.api.post.user(
                service_provider_id=self.service_provider_id,
                group_id=self.group_id,
                data=self.test_user_data
            ),
            []
        )
    
    
    def test_get_user(self):
        """ Gets built user from system and checks name to confirm user was built correctly.
        """
        self.assertEqual(
            self.api.get.user_by_id(self.test_user_data["userId"])["firstName"],
            self.test_user_data["firstName"]
        )
    
    
    def test_put_user(self):
        """ Updates users first and last name and the checks response has no error.
        """
        self.test_user_data["firstName"] = "Jeremy"
        self.test_user_data["lastName"] = "Usborne"
             
        self.assertEqual(
            self.api.put.user(
                service_provider_id=self.service_provider_id,
                group_id=self.group_id,
                updates=self.test_user_data
            ),
            []
        )
    
    
    def test_delete_user(self):
        """ Deletes test user from system.
        """
        
        self.assertEqual(
            self.api.delete.user(
                user_id=self.user_id
            ),
            []
        )
    
    
if __name__ == '__main__':
    unittest.main()
