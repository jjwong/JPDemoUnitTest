import unittest

class TestVariableAssignments(unittest.TestCase):

    def test_side_effect_should_overwrite_original(self):
        # Create the value
        original = ["red", "green", "blue"]
        value = ["red", "green", "blue"]

        print("*** Side Effect should overwrite original variable values. ***")
        print("Outside the function, the value starts as {}".format(value))

        self.side_effect(value)

        print("Outside the function, the value is now {}".format(value))
        self.assertNotEqual(original, value)

    def test_no_side_effect_should_retain_original(self):
        # Create the value
        original = ["red", "green", "blue"]
        value = ["red", "green", "blue"]

        print("*** No Side Effect - Variables should retain their values. ***")
        print("Outside the function, the value starts as {}".format(value))

        self.no_side_effect(value)

        print("Outside the function, the value is now {}".format(value))
        self.assertEqual(original, value)

    def side_effect(self, value):
        # Do something to modify the value
        value[1] = "purple"
        print("Inside the function, the value becomes {}".format(value))

    def no_side_effect(self, value):
        value_received = []
        for item in value:
            value_received.append(item)

        # Do something to modify the value
        value_received[1] = "orange"
        print("Inside the function, the value becomes {}".format(value_received))

if __name__ == "__main__":
    unittest.main()