import unittest
from onlinevars import OnlineVars

class TestOnlineVars(unittest.TestCase):
    """
    Test suite for the OnlineVars client.
    """

    def setUp(self):
        """
        Set up a fresh client for each test.
        This ensures that tests are isolated and don't interfere with each other.
        """
        self.client = OnlineVars()
        # Ensure the remote state is clean before running the test.

    def test_initial_state_is_empty(self):
        """Test that a new client instance has no variables."""
        variables = self.client.list()
        self.assertEqual(variables, [])

    def test_set_new_variable(self):
        """Test creating a new variable and check status, text, and value."""
        # Test creation of a string variable
        status, text = self.client.set("greeting", "Hello, World!")
        self.assertEqual(status, 201)
        self.assertEqual(text, "created")

        # Verify it can be retrieved correctly
        value = self.client.get("greeting")
        self.assertEqual(value, "Hello, World!")

        # Test creation of an integer variable
        status, text = self.client.set("counter", 100)
        self.assertEqual(status, 201)
        self.assertEqual(text, "created")
        
        value = self.client.get("counter")
        self.assertEqual(value, 100)

    def test_list_all_variables(self):
        """Test that list() returns all created variables, sorted alphabetically."""
        self.client.set("greeting", "Hello")
        self.client.set("counter", 100)
        
        variables = self.client.list()
        # The original script's assertion implies the API returns a sorted list.
        # We test for this specific order.
        self.assertEqual(variables, ["counter", "greeting"])

    def test_update_existing_variable(self):
        """Test updating a variable and check status, text, and new value."""
        # First, create the variable
        self.client.set("greeting", "Hello, World!")

        # Now, update it
        status, text = self.client.set("greeting", "Hello, API Client!")
        self.assertEqual(status, 200)
        self.assertEqual(text, "updated")

        # Verify the updated value is retrieved
        updated_value = self.client.get("greeting")
        self.assertEqual(updated_value, "Hello, API Client!")

    def test_remove_variable(self):
        """Test removing a variable and ensuring it's no longer accessible."""
        # Create a variable to be removed
        self.client.set("counter", 100)
        
        # Verify it exists before removal
        self.assertIn("counter", self.client.list())

        # Remove it
        self.client.rem("counter")

        # Verify it is no longer in the list
        self.assertNotIn("counter", self.client.list())

    def test_get_deleted_or_nonexistent_variable(self):
        """Test that getting a removed or non-existent variable returns None."""
        # Test getting a variable that was never created
        nullvar = self.client.get("invalid-name!")
        self.assertIsNone(nullvar, "Getting a non-existent variable should return None.")
        
        # Create and then delete a variable
        self.client.set("temp_var", "will be deleted")
        self.client.rem("temp_var")

        # Test getting the deleted variable
        deleted_var = self.client.get("temp_var")
        self.assertIsNone(deleted_var, "Getting a deleted variable should return None.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
