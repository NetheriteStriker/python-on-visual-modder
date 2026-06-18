def chest():
  vm.createSquare(4, True, Block.OAK_LOG)
  vm.moveTo(1, Direction.UP)
  for count in range(3):
    vm.createSquare(4, False, Block.OAK_FENCE)
    vm.moveTo(1, Direction.UP)

def rope():
  for coumt in range(4):
    vm.createSquare(4, False, [Block.DARK_OAK_FENCE, dict(AMOUNT=2, TYPE=Block.AIR)])
    vm.moveTo(1, Direction.UP)


def ball():
  vm.moveTo(16, Direction.UP)
  for court in range(60):
    vm.createCircle(18, False, [Block.BLUE_WOOL, Block.WHITE_WOOL])
    vm.changeInclination(3)

def hotairballoon():
  
  chest()
  
  rope()
  
  ball()