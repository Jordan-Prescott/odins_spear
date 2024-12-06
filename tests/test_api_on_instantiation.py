import unittest
import os
import sys


class TestOnApiInstantiation(unittest.TestCase):
    """ 
    Test library is setting up correctly when instatiating API object e.g.ensuring objects are 
    handed to other objects that need them to function. Finally, tests authentication needed
    to utilise the library.
    """
    
    
    def setUp(self):
        sys.path.append('..')
        
        from odins_spear.api import Api
        # Set up API object
        self.api = Api(base_url=os.getenv("ODIN_URL"), username= os.getenv("ODIN_USERNAME"), 
               password="ODIN_PASSWORD")
        

    def test_logger_set_up(self):
        """ Logger has been set up and username set correctly
        """
        self.assertEqual(
            self.api.username,
            self.api.logger._user
        )

    def test_requester_set_up(self):
        """ Logger has been set up and username set correctly
        """
        # base url
        self.assertEqual(
            self.api.base_url,
            self.api._requester.base_url
        )

        # rate limit
        self.assertEqual(
            self.api.rate_limit,
            self.api._requester.rate_limit
        )
        
        # logger
        self.assertIs(
            self.api.logger,
            self.api._requester.logger
        )

    
    def test_method_set_up(self):
        """ Methods are correctly setup with requester
        """
        # GET
        self.assertIs(
            self.api._requester,
            self.api.get._requester
        )

        # POST
        self.assertIs(
            self.api._requester,
            self.api.post._requester
        )
        
        # PUT
        self.assertIs(
            self.api._requester,
            self.api.put._requester
        )
        
        # DELETE
        self.assertIs(
            self.api._requester,
            self.api.delete._requester
        )
        
    def test_scripter_set_up(self):
        """ Scripter is setup with the API needed
        """
        self.assertIs(
            self.api.scripter.api,
            self.api
        )
        
        
    def test_reporter_set_up(self):
        """ Reporter is setup with the API needed
        """
        self.assertIs(
            self.api.reporter.api,
            self.api
        )


    def test_authentication(self):
        """ API object is able to authenticate.
        """
        try:
            self.assertEqual(
                self.api.authenticate(), 
                True
            )
        except Exception:
            self.fail("Authentication failed.")
            

if __name__ == '__main__':
    unittest.main()