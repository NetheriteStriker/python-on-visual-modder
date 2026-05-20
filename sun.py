def sun():
  for count in range(8):
    vm.createLine(100, [Block.REDSTONE_BLOCK, Block.GOLD_BLOCK])
    vm.changeDirection(22.5)