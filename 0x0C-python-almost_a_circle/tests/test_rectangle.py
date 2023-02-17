import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self, w, h, x, y, d):
        rec = Rectangle(w, h, x, y, d)

        self.assertEqual(rec.width, w)
        self.assertEqual(rec.height, h)
        self.assertEqual(rec.x, x)
        self.assertEqual(rec.y, y)
        self.assertEqual(rec.id, d)
    
    def test_rectangleIdAlx(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_init(self):
        # Rectangle._Rectangle__nb_objects = 0
        setUp(10, 20, 0, 0, 7)
        

if __name__ == "__main__":
    unittest.main()