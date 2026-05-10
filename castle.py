def castle():
  for count in range(10):
    if count==9:
      vm.createCircle(10, False, [Block.QUARTZ_PILLAR, Block.AIR])
    else:
      vm.createCircle(10, False, [Block.DIAMOND_BLOCK, Block.QUARTZ_PILLAR])
      vm.moveTo(1, Direction.UP)
  vm.moveTo(10, Direction.DOWN)
  for clount in range(20):
    if clount==19:
      vm.createCircle(4, False, [Block.QUARTZ_PILLAR, Block.AIR])
    else:
      vm.createCircle(4, False, [Block.QUARTZ_PILLAR, Block.NETHERITE_BLOCK])
      vm.moveTo(1, Direction.UP)