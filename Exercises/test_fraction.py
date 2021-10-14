from fraction import Fraction


def test_equality():
  half = Fraction(1,2)
  otherhalf = Fraction(1,2)
  assert(half == otherhalf)

def test_notEqual():
  half = Fraction(1, 2)
  oneThird = Fraction(1, 3)
  assert(half != oneThird)

def test_differentObjectsAreNotEqual():
  half = Fraction(1, 2)
  assert(half != 1)

def test_fractionAsAString():
  half = Fraction(1, 2)
  assert(str(half) == "1/2")

def test_reduction():
  half = Fraction(1, 3)
  otherHalf = Fraction(3, 9)
  assert(half == otherHalf)

def test_add():
  aThird = Fraction(1, 3)
  half = Fraction(1, 2)
  assert(half.add(aThird) == Fraction(5, 6))

def test_divide():
  aThird = Fraction(1, 3)
  half = Fraction (1, 2)
  assert(half.divide(aThird) == Fraction(3, 2))