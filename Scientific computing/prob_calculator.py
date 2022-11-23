import random
import copy


class Hat:
    def __init__(self, **args):
        self.contents = []
        for item, count in args.items():
            for i in range(count):
                self.contents.append(item)

    def draw(self, count):
        content_copy = self.contents  # copy.copy(self.contents)
        if len(self.contents) >= count:
            drawn = []
            for _ in range(count):
                random_number = random.randint(0, len(content_copy) - 1)
                drawn.append(content_copy[random_number])
                content_copy.pop(random_number)
        else:
            drawn = content_copy
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    positive_results = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        outcome = hat_copy.draw(num_balls_drawn)
        right_colors = 0
        for color in expected_balls.keys():
            if outcome.count(color) >= expected_balls[color]:
                right_colors += 1
        if right_colors == len(expected_balls):
            positive_results += 1
    probability = float(positive_results) / num_experiments
    return probability
