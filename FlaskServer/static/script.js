(function () {

$scope.buildBoard = function () {
	$scope.dimension = 75;
	$scope.range = 4;
	$scope.board = [];

	for (var i = 0; i < $scope.dimension; i++) {
		$scope.board.push([]);
		for (var j = 0; j < $scope.dimension; j++) {
			$scope.board[i].push(Math.floor(Math.random() * $scope.range) + 1);
		}
	}
}

var printBoard = function () {
	for (var i = 0; i < $scope.dimension; i++) {
		var row = "";
		for (var j = 0; j < $scope.dimension; j++) {
			row += $scope.board[j][i] + ", ";
		}
		console.log(row);
	}
}

var addNeighbors = function (cell, origin, stack) {
	var cellx = cell.x;
	var celly = cell.y;
	if (cellx + 1 < $scope.dimension && $scope.board[cellx+1][celly] == origin) {
		stack.push({ x: cellx+1, y: celly});
	}
	if (cellx - 1 >= 0 && $scope.board[cellx-1][celly] == origin) {
		stack.push({ x: cellx-1, y: celly});
	}
	if (celly - 1 >= 0 && $scope.board[cellx][celly-1] == origin) {
		stack.push({ x: cellx, y: celly-1});
	}
	if (celly + 1 < $scope.dimension && $scope.board[cellx][celly+1] == origin) {
		stack.push({ x: cellx, y: celly+1});
	}
	return stack;
}

var move = function (choice, origin) {
	var stack = [];
	var currentCell = { x: 0, y: 0 };
	stack.push(currentCell);
	while (stack.length > 0) {
		currentCell = stack[0];
		if ($scope.board[currentCell.x][currentCell.y] == choice) {
			stack = stack.splice(1, stack.length - 1);
			continue;
		}
		$scope.board[currentCell.x][currentCell.y] = choice;
		stack = stack.splice(1, stack.length - 1);
		stack = addNeighbors(currentCell, origin, stack);
	}
}


var checkState = function () {
	var origin = $scope.board[0][0];
	for (var i = 0; i < $scope.dimension; i++) {
		for (var j = 0; j < $scope.dimension; j++) {
			if ($scope.board[i][j] != origin) {
				return false;
			}
		}
	}
	return true;
}

var begin = function (choice) {
	var origin = $scope.board[0][0];
	move(choice, origin);
	if (checkState()) {
		console.log("YOU WIN!");
	}
}

$scope.buildBoard();

});


