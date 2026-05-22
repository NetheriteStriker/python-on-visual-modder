def sun():
  for count in range(8):
    vm.createLine(100, [Block.REDSTONE_BLOCK, Block.GOLD_BLOCK])
    vm.changeDirection(22.5)


def stair():
  vm.moveTo(10, Direction.FORWARD)
  for count in range(100):
    vm.createLine(21, [Block.REDSTONE_BLOCK, Block.GOLD_BLOCK, Block.EMERALD_BLOCK])
    vm.moveTo(1, Direction.UP)
    vm.moveTo(2, Direction.LEFT)
    vm.createBlock(Block.TORCH)
    vm.moveTo(2, Direction.RIGHT)
    vm.changeDirection(6)
