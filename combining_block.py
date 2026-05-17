def checkerboard():
  for count in range (10):
    vm.createText('8', 60, True, [Block.PINK_WOOL, Block.CYAN_WOOL])
    vm.moveTo(1, Direction.UP)
  vm.moveTo(2, Direction.DOWN)
  vm.createText('8', 58, False, Block.BLUE_WOOL)
    
  