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

  def pick4(self):
     """Pick 4 Beepers"""
     pick_beeper()
     pick_beeper()
     pick_beeper()
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

  def put4(self):
     """Put 4 beepers in a line"""
     self.put2()
     self.m()
     self.put2()
    
  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m2()
    kt.tl()
    kt.m2()
    kt.tr()
    kt.put4()
    kt.tl()
    kt.m()
    kt.put3()
    kt.tl()
    kt.m()
    kt.put3()
    kt.tl()
    kt.m()
    kt.put2()
    kt.m()
    kt.tl()
    pass


if __name__ == "__main__":
    run_karel_program()
