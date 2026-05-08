def p():
	height = 8
	for count in range(height):
		# the 1st layer is when count = 0
		# the square width is 15, i.e. (7 - count) * 2 + 1

		# the 7th layer is when count = 6
		# the square width is 1, i.e. (7 - count) * 2 + 1
				
		
		width = (7-count)*2+1
		vm.createSquare(width, FALSE, Block.DIAMOND_BLOCK)
		vm.moveTo(1, Direction.UP)

def p2():
	height = 8
	for count in range(height):
		width = (height - 1 - count) * 2 + 1
		vm.createSquare(width, FALSE, Block.DIAMOND_BLOCK)
		vm.moveTo(1, Direction.UP)


def pickaxe():
  vm.giveToPlayer(Equip.RIGHT_HAND, Item.NETHERITE_PICKAXE)
