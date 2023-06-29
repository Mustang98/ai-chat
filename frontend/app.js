angular.module('myApp', [])
    .controller('CharacterController', function ($scope, $http) {
        $scope.characters = [];
        $scope.selectedCharacter = null;
        $scope.dialogue = null;
        $scope.newMessage = '';
        var hostname = 'http://35.193.20.238:8000/'


        // Check for user_id in local storage
        var userId = localStorage.getItem('neiro_user_id');
        if (!userId) {
            // User ID is not available, request it from the server
            $http.post(hostname + 'users')
                .then(function (response) {
                    // Save the received user_id in local storage
                    userId = response.data.id;
                    localStorage.setItem('neiro_user_id', userId);
                })
                .catch(function (error) {
                    console.log(error);
                });
        }


        // Fetch characters
        $http.get('http://35.193.20.238:8000/characters')
            .then(function (response) {
                $scope.characters = response.data.characters;
                $scope.selectCharacter($scope.characters[0])
            })
            .catch(function (error) {
                console.log(error);
            });


        // Select character
        $scope.selectCharacter = function (character) {
            $scope.selectedCharacter = character;
            var dialogueData = {
                user_id: current_user_id, // Replace with the actual user ID
                character_id: character.id
            };

            // Send a POST request to /dialogues
            $http.post('http://35.193.20.238:8000/dialogues', dialogueData)
                .then(function (response) {
                    // Update the messages in the dialogue section
                    $scope.messages = response.data.messages;
                    $scope.dialogue = response.data;
                })
                .catch(function (error) {
                    console.log('Error creating dialogue:', error);
                });

        };


        // Send message
        $scope.sendMessage = function () {
            if ($scope.newMessage.trim() === '') {
                return;
            }

            // Create a new message object
            var newMessage = {
                dialogue_id: $scope.dialogue.id, content: $scope.newMessage.trim()
            };
            $scope.newMessage = '';
            // Send POST request to create a new message
            $http.post('http://35.193.20.238:8000/messages', newMessage)
                .then(function (response) {
                    $scope.selectCharacter($scope.selectedCharacter);
                })
                .catch(function (error) {
                    console.log(error);
                });
        };


    });