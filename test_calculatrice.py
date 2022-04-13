import calculatrice, unittest



class Mytest(unittest.TestCase):
    def test_somme(self):
        a=2
        b=5
        s= calculatrice.somme(a,b)
        self.assertEqual(7,s)

    def test_diff(self):
        a=5
        b=2
        d=calculatrice.soustraction(a,b)
        self.assertEqual(3,d)

if __name__=="__main__":
    unittest.main()


