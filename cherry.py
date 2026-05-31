def Ball():
  for count in range(36):
    vm.createCircle(16, False, Block.RED_WOOL)
    vm.changeInclination(5)
  vm.setInclination(0)
  vm.moveTo(16, Direction.UP)
  for count in range(30):
    vm.createCircle(4, False, Block.GREEN_WOOL)
    vm.changeInclination(5)
    vm.moveTo(1, Direction.UP)