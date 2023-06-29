angular.module('characterApp', [])
  .controller('characterController', function($scope, $http) {
    $http.get('http://35.193.20.238:8000/characters')
      .then(function(response) {
        $scope.characters = response.data.characters;
      })
      .catch(function(error) {
        console.error('Error:', error);
      });
  });
