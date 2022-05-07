import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    contents = []
    for key in balls.keys():
      for num in range(balls[key]):
        contents.append(key)
    
    self.contents = contents

  def draw(self, num_balls):
    drawn_balls = []
    if(num_balls > len(self.contents)):
      return self.contents
    for i in range(num_balls):
      random_ball = random.choice(self.contents)
      drawn_balls.append(random_ball)
      self.contents.remove(random_ball)

    return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  for i in range(num_experiments):
    expected_colors = copy.deepcopy(expected_balls)
    new_hat = copy.deepcopy(hat)
    colors = new_hat.draw(num_balls_drawn)

    for ball_color in colors:
      if ball_color in expected_colors:
        expected_colors[ball_color] -= 1

    if all(num <= 0 for num in expected_colors.values()):
      success_count += 1
  
  return success_count/num_experiments



