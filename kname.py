from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for Move"""
    move()

  def m2(self):
   """Move two times"""
   self.m()
   self.m()
    
  def m3(self):
     """Move three times"""
     self.m2()
     self.m()
    
  def m4(self):
      """Move four times"""
      self.m2()
      self.m2()
  
  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put3(self):
     """Put 3 beepers in a line"""
     self.put2()
     self.m()
     self.put()
    
  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def l(self):
     """Print L using beepers"""
     self.m()
     self.put2()
     self.tl()
     self.tl()
     self.m()
     self.m()
     self.tr()
     self.put5()
     self.tr()
     self.m()
     self.m()
     self.m()
     self.m()
     self.tr()
     self.m()
     self.m()
     self.m()
     self.m()
     self.tl()
    
  def r(self):
     """Print R using beepers"""
     self.tl()
     self.put5()
     self.tr()
     self.put5()
     self.tr()
     self.put3()
     self.tr()
     self.put5()
     self.ta()
     self.m()
     self.tr()
     self.m()
     self.put()
     self.m()
     self.tl()
     self.m()
     self.put()
     self.m()
     self.m()
     self.m()
     self.m()
  
  def i(self):
     """Print I using beepers"""
     self.tl()
     self.put5()
     self.m2()
     self.put()
     self.tr()
     self.m2()
     self.tr()
     self.m4()
     self.m2()
     self.tl()
     
  def t(self):
     """Print T using beepers"""
     self.tl()
     self.put5()
     self.tr()
     self.tr()
     self.m2()
     self.ta()
     self.tl()
     self.m()
     self.put()
     self.tl()
     self.tl()
     self.m2()
     self.put()
     self.m2()
     self.tr()
     self.m()
     self.m()
     self.tl()

  def y(self):
     """Print Y using beepers"""
     self.tl()
     self.m2()
     self.put3()
     self.tr()
     self.tr()
     self.m2()
     self.tl()
     self.m()
     self.put3()
     self.m()
     self.tl()
     self.put3()
     self.tr()
     self.tr()
     self.m3()
     self.put2()
     self.tr()
     self.put3()
     self.ta()
     self.m4()

    
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.r()
    kt.i()
    kt.t()
    kt.y()
    kt.i()
    kt.l()
    pass


if __name__ == "__main__":
    run_karel_program()
