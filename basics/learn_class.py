class Cookie:
  def __init__(self, color):
    self.color = color
    
  def get_color(self):
    return self.color
  
  def set_color(self, color):
    self.color = color
    
    
#create a cookie instance
cookie_1 = Cookie("green")
cookie_2 = Cookie("blue")

cookie_1.set_color('red')
cookie_2.set_color('yellow')

print(cookie_1.color)
color_2 = cookie_2.get_color()
print(color_2)