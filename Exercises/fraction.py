from gcd import gcd

class Fraction:
  def __init__(self, nominator, denominator):
      self.__nominator = nominator
      self.__denominator = denominator

  def __eq__(self, o):
    return (isinstance(o, Fraction) 
    and (self.__reduce().__nominator == o.__reduce().__nominator) 
    and (self.__reduce().__denominator == o.__reduce().__denominator))
    

    #if type(o) is not Fraction:
    #  return False
    #return (self.__nominator == o.__nominator) and (self.__denominator == o.__denominator)

  def multiply(self, other):
    return Fraction(self.__nominator*other.__nominator, self.__denominator*other.__denominator).__reduce()

  def add(self, o):
    return Fraction((self.__nominator * o.__denominator) + (o.__nominator * self.__denominator)
    , self.__denominator * o.__denominator).__reduce()

  def divide(self, o):
    return self.multiply(Fraction(o.__denominator, o.__nominator)).__reduce()

  def __repr__(self):
      return str(self.__nominator) + "/" + str(self.__denominator)

  def __reduce(self):
    divider = gcd(self.__nominator, self.__denominator)
    return Fraction(self.__nominator / divider, self.__denominator / divider)