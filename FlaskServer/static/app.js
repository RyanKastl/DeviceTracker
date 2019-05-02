(function() {
  
  var app = angular.module("DeviceTracker", ["ngRoute"]);
  
  app.config(function($routeProvider, $interpolateProvider) {
    $routeProvider
      .when("/main", {
        templateUrl: "main.html",
        controller: "MainController"
      })
      .otherwise({redirectTo:"/"});
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
  });
  
}());