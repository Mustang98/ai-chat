angular.module('myApp', [])
  .controller('CharacterController', function($scope, $http) {
    $scope.characters = [];
    $scope.selectedCharacter = null;

    // Make a GET request to the API to fetch characters
    $http.get('http://35.193.20.238:8000/characters')
      .then(function(response) {
        // Assign the characters to the $scope variable
        $scope.characters = response.data.characters;
      })
      .catch(function(error) {
        console.log('Error:', error);
      });

    $scope.selectCharacter = function(character) {
      $scope.selectedCharacter = character;
    };
  });
