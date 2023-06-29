angular.module('myApp', [])
    .controller('CharacterController', function ($scope, $http) {
        var current_user_id = 'a9f08c90-8b69-4e2a-889a-8366cd3cbb6d'

        $scope.characters = [];
        $scope.selectedCharacter = null;
        $scope.dialogue = null;
        $scope.newMessage = '';

        // data = {
        //     "characters": [{
        //         "id": "34f3d314-7554-4787-aff8-2198f9d7ab0d", "name": "Ariana Grande"
        //     }, {
        //         "id": "153105be-d51d-46ce-8150-b8191e7a36ad", "name": "Elon Musk"
        //     }, {
        //         "id": "6bd217ca-7fa9-4d5a-80e0-dd4d4cc1e1d2", "name": "Eva Elfie"
        //     }, {
        //         "id": "186bcf43-e1d1-4d2b-8ff7-9611cd5d11f2", "name": "Billie Eilish"
        //     }, {
        //         "id": "fd63ee7f-4661-46ef-97a4-9dc861b823f2", "name": "Spiderman"
        //     }, {"id": "b6d83bbe-79fb-4ff5-bd15-55c38acf0c02", "name": "Barbie"}]
        // }
        // $scope.characters = data.characters;

        // Fetch characters
        $http.get('http://35.193.20.238:8000/characters')
            .then(function (response) {
                $scope.characters = response.data.characters;
                $scope.selectCharacter($scope.characters[0])
            })
            .catch(function (error) {
                console.log(error);
            });

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


// var app = angular.module('myApp', []);
//
// app.controller('CharacterController', function($scope, $http) {
//   $scope.characters = [];
//
//   // Fetch the list of characters
//   // $http.get('http://35.193.20.238:8000/characters')
//   //   .then(function(response) {
//   //     $scope.characters = response.data.characters;
//   //   })
//   //   .catch(function(error) {
//   //     console.log('Error fetching characters:', error);
//   //   });
//     $scope.characters = {"characters":[{"id":"34f3d314-7554-4787-aff8-2198f9d7ab0d","name":"Ariana Grande"},{"id":"153105be-d51d-46ce-8150-b8191e7a36ad","name":"Elon Musk"},{"id":"6bd217ca-7fa9-4d5a-80e0-dd4d4cc1e1d2","name":"Eva Elfie"},{"id":"186bcf43-e1d1-4d2b-8ff7-9611cd5d11f2","name":"Billie Eilish"},{"id":"fd63ee7f-4661-46ef-97a4-9dc861b823f2","name":"Spiderman"},{"id":"b6d83bbe-79fb-4ff5-bd15-55c38acf0c02","name":"Barbie"}]}
//
//   $scope.selectCharacter = function(character) {
//     // Create the dialogue data
//     var dialogueData = {
//       user_id: 'a9f08c90-8b69-4e2a-889a-8366cd3cbb6d', // Replace with the actual user ID
//       character_id: character.id
//     };
//
//     // Send a POST request to /dialogues
//     // $http.post('http://35.193.20.238:8000/dialogues', dialogueData)
//     //   .then(function(response) {
//     //     // Update the messages in the dialogue section
//     //     $scope.messages = response.data.messages;
//     //   })
//     //   .catch(function(error) {
//     //     console.log('Error creating dialogue:', error);
//     //   });
//       $scope.messages = {"id":"3a9f1312-93fb-4663-ba0c-5fd15a77b941","messages":[{"id":"4d7b29b7-d7cb-43d3-a209-88bcfb4d1659","content":"This is a new message","sender_type":"user"},{"id":"9ed7bb28-c23c-4f71-aa8a-ad432d461d9f","content":"This is a new message","sender_type":"user"},{"id":"1e8ca516-6001-44cd-bd5d-9c38e6e03838","content":"I agree that This is a new message","sender_type":"bot"},{"id":"fde13c99-67ef-4c75-a9bb-65d1ccf3df04","content":"This is a new message2","sender_type":"user"},{"id":"ce930550-8605-4be5-b32e-bd1254dff2d6","content":"I agree that This is a new message2","sender_type":"bot"}]}
//   };
// });