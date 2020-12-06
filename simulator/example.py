from simulator import Simulator

bounding_box = (13.34014892578125, 52.52791908000258, 13.506317138671875, 52.562995039558004)
result = Simulator(bounding_box).simulate(10)

print(result)