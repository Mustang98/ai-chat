function fetchCharacters() {
  fetch('http://35.193.20.238:8000/characters')
    .then(response => response.json())
    .then(data => {
      const characterList = document.getElementById('characterList');

      data.characters.forEach(character => {
        const listItem = document.createElement('li');
        listItem.textContent = character.name;
        characterList.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

document.addEventListener('DOMContentLoaded', fetchCharacters);
