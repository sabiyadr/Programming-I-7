from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for Move"""
    move()

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

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def m2(self):
   """Move two times"""
   self.m()
   self.m()
  
  def m4(self):
      """Move four times"""
      self.m2()
      self.m2()
    
  def pinset(self):
     """Sets the pins in bowling formation"""
     self.m4()
     self.tl()
     self.m()
     self.put()
     self.m()
     self.tl()
     self.m()
     self.put()
     self.tl()
     self.tl()
     self.m()
     self.m()
     self.put()
     self.tl()
     self.m()
     self.tr()
     self.m()
     self.put()
     self.tl()
     self.tl()
     self.m2()
     self.put()
     self.m2()
     self.put()
     self.tr()
     self.m()
     self.tl()
     self.m()
     self.tr()
     self.tr()
     self.put()
     self.m2()
     self.put()
     self.m2()
     self.put()
     self.m2()
     self.put()
    
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.pinset()
    pass


if __name__ == "__main__":
    run_karel_program()
