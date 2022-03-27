import unittest

from Labb8 import *


class SyntaxTest(unittest.TestCase):
    def testSyntaktisktKorrekt(self):
        """Testar syntaktiskt korrekt molekyl"""
        self.assertEqual(checkMoleculeSyntax("H2"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("P21"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("Ag3"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("Fe12"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("Xx5"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("H10100"), "Formeln är syntaktiskt korrekt")


    def testSyntaktisktInkorrekt(self):
        """Testar syntaktiskt inkorrekt molekyl"""
        self.assertEqual(checkMoleculeSyntax("a"), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(checkMoleculeSyntax("cr12"), "Saknad stor bokstav vid radslutet cr12")
        self.assertEqual(checkMoleculeSyntax("8"), "Saknad stor bokstav vid radslutet 8")
        self.assertEqual(checkMoleculeSyntax("Cr0"), "För litet tal vid radslutet ")
        self.assertEqual(checkMoleculeSyntax("Pb1"), "För litet tal vid radslutet ")
        self.assertEqual(checkMoleculeSyntax("H01011"), "För litet tal vid radslutet 1011")


if __name__== "__main__":
    unittest.main()