import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# def count_nb_line():
#     return 3

# def count_nb_column():
#     return 4

# def cout_nb_input():
#     return 5

def cout_nb_button():
    return True



class TestClub(unittest.TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_
    """
    def setUp(self) -> None:
        """Définie mes paramètres d'initialisation
        """
        
        
    # def test_count(self):
    #     count = count_nb_line()
    #     self.assertEqual(count, 3)
        
    # def test_nb_columns(self):
    #     count = count_nb_column()
    #     self.assertIsNotNone(count)
        
    # def nombre_input(self):
    #     count = cout_nb_input()
    #     self.assertEqual(count, 4)
        
    def test_nb_button(self):
        count = cout_nb_button()
        self.assertEqual(count, True)
        
    
    
if __name__ == "__main__":
    unittest.main()