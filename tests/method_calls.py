import unittest
import os
import sys
import time

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
        self.api = Api(base_url=os.getenv("ODIN-URL"), username= os.getenv("ODIN-USERNAME"), 
               password="ODIN-PASSWORD")
        
        self.service_provider_id = os.getenv("TEST-SERVICE-PROVIDER-ID")
        self.group_id = os.getenv("TEST-GROUP-ID")
        self.user_id = os.getenv("TEST-USER-ID")
        
        self.test_user_data = {
            "serviceProviderId": self.service_provider_id,
            "groupId": self.group_id,
            "userId": self.user_id,
            "firstName": "Mark",
            "lastName": "Corrigan",
            "callingLineIdFirstName": "Mark",
            "callingLineIdLastName": "Corrigan",
            "password": "password",
        }        
    
    
    def test_first(self):
        """ API object is able to authenticate.
        """
        try:
            self.assertEqual(
                self.api.authenticate(), 
                True
            )
        except Exception:
            self.fail("Authentication failed.")
    
    
    def test_second(self):
        """ Builds test user in test environment and checks response.
        """
        try:
            build_user = self.api.post.user(
                service_provider_id=self.service_provider_id,
                group_id=self.group_id,
                data=self.test_user_data
            )
        except Exception:
            build_user = "Failed"
        
        time.sleep(1)
        
        self.assertEquals(
            type(build_user),
            dict
        )
        
    
    # def test_third(self):
    #     """ Gets built user from system and checks name to confirm user was built correctly.
    #     """
    #     try:
    #         get_user = self.api.get.user_by_id(self.user_id)
    #         self.test_user_data = get_user,
    #     except Exception:
    #         get_user = "Failed"
            
    #     time.sleep(2)
        
    #     self.assertEqual(
    #             get_user["userId"],
    #             self.user_id
    #         )
            
    
    # def test_fourth(self):
    #     """ Updates users first and last name and the checks response has no error.
    #     """
    #     self.test_user_data["firstName"] = "Jeremy"
    #     self.test_user_data["lastName"] = "Usborne"
    #     self.test_user_data["callingLineIdFirstName"] = "Jeremy"
    #     self.test_user_data["callingLineIdLastName"] = "Usborne"
        
    #     try: 
    #         update_user = self.api.put.user(
    #                 service_provider_id=self.service_provider_id,
    #                 group_id=self.group_id,
    #                 updates=self.test_user_data
    #             )
    #     except Exception:
    #         update_user = False
        
    #     time.sleep(2)
        
    #     self.assertEqual(
    #         update_user["firstName"],
    #         self.test_user_data["firstName"]
    #     )
        
    
    def test_fifth(self):
        """ Deletes test user from system.
        """
        try:
            delete_user = self.api.delete.user(
                    user_id=self.user_id
                )  
        except Exception:
            delete_user = False
        
        time.sleep(2)
        
        self.assertEqual(
            delete_user,
            list
        )
        
    
if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: 1 if x > y else -1 if x < y else 0
    unittest.main()
