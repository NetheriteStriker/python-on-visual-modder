def cake():
  for count in range(3):
    vm.createCircle(8, False, Block.RED_WOOL)
    vm.moveTo(1, Direction.UP)
    vm.createCircle(8, False, Block.WHITE_WOOL)
    vm.moveTo(1, Direction.UP)
      
  vm.createCircle(8, False, [Block.AIR,Block.TORCH])

  vm.createCircle(4, False, [Block.RED_CONCRETE, Block.AIR])