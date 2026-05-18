def checkerboard():
  for count in range (10):
    vm.createText('8', 60, True, [Block.PINK_WOOL, Block.CYAN_WOOL])
    vm.moveTo(1, Direction.UP)
  vm.moveTo(2, Direction.DOWN)
  vm.createText('8', 58, False, Block.BLUE_WOOL)
    

def smily_face():
  vm.createCircle(30, True, [dict(GROUND=True, TYPE=Block.YELLOW_WOOL)])
  vm.createCircle(30, False, [dict(GROUND=True, TYPE=Block.BLACK_WOOL)])
  vm.moveTo(10, Direction.FORWARD)
  vm.moveTo(15, Direction.RIGHT)
  vm.createCircle(5, True, [dict(GROUND=True, TYPE=Block.LIGHT_BLUE_WOOL)])
  vm.createCircle(5, False, [dict(GROUND=True, TYPE=Block.BLACK_WOOL)])
  vm.moveTo(25, Direction.LEFT)
  vm.createCircle(6, True, [dict(GROUND=True, TYPE=Block.LIGHT_BLUE_WOOL)])
  vm.createCircle(6, False, [dict(GROUND=True, TYPE=Block.BLACK_WOOL)])
  vm.moveTo(5, Direction.RIGHT)
  vm.moveTo(12, Direction.BACKWARD)
  vm.createSquare(6, True, [dict(GROUND=True, TYPE=Block.WHITE_WOOL)])
  vm.createSquare(6, False, [dict(GROUND=True, TYPE=Block.BLACK_WOOL)])
  vm.moveTo(12, Direction.BACKWARD)
  vm.createArc(7, 7, 180, True,[dict(GROUND=True, TYPE=Block.RED_WOOL), dict(GROUND=True, TYPE=Block.BLACK_WOOL)])
  vm.createArc(7, 7, 180, False, [dict(GROUND=True, TYPE=Block.BLACK_WOOL)])

  