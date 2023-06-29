var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) {
  // Initialize characters array
  $scope.characters = [];

  // Fetch characters from API
  $http.get('http://35.193.20.238:8000/characters')
    .then(function(response) {
      $scope.characters = response.data.characters;
    })
    .catch(function(error) {
      console.log('Error fetching characters:', error);
    });

  // Select character
  $scope.selectCharacter = function(character) {
    $scope.selectedCharacter = character;
  };
});
