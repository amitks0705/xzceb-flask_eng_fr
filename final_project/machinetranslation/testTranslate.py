import unittest
import translator
class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.translateEnglishToFrench("English"), 
            translator.translateEnglishToFrench("English")) 
        
class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.translateFrenchToEnglish("French"), 
            translator.translateFrenchToEnglish("French")) 
        
unittest.main()
