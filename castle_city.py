def create_wall():
  for count in range(5):
    vm.createCircle(20, False, Block.GOLD_BLOCK)
    vm.moveTo(1, Direction.UP)

def create_8_circles():
  for count in range(8):
    vm.moveTo(20, Direction.FORWARD)
    vm.createCircle(4, False, Block.GOLD_BLOCK)
    vm.moveTo(20, Direction.BACKWARD)
    vm.changeDirection(45)

def create_8_towers():
  for count in range(8):
    create_8_circles()
    vm.moveTo(1, Direction.UP)

def create_towered_wall():
  create_wall()
  vm.moveTo(Position.START)
  create_8_towers()
  