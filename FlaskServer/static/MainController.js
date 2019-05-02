// Code goes here
(function() {

  	var app = angular.module("DeviceTracker");
  
  	app.controller("MainController", ['$scope', '$interval', '$location', '$rootScope', MainController]);

  	function MainController($scope, $interval, $location, $rootScope) {

	    $scope.devices = {};

	    $scope.getDevices = function () {
			$.get(
			    "/refresh/",
			    {paramOne : 1, paramX : 'abc'},
			    function(data) {
			    	$scope.devices = data;
			       	console.log(data)
			    }
			);
	    };

	    $scope.initialize = function(data) {
	    	$scope.devices = data;
	    };
  	};
}());