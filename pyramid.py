def p():
	for count in range(7):
		vm.createSquare((7-count)*2+1, false, Block.DIAMOND_BLOCK)
		vm.moveTo(1, Direction.UP)



def p2():
	height = 7
	for count in range(height):

		# the first layer is when count = 0
		# the square width is 15, which is (height-count) * 2 + 1, e.g. (7 - count) * 2 + 1

		# the top layer is when count = height - 1

		width = (height-count) * 2 + 1

		vm.createSquare(width, FALSE, Block.DIAMOND_BLOCK)
		vm.moveTo(1, Direction.UP)

