$("document").ready(() => {
  $("#headline").hide(0);
  $("#headline").slideDown(1000);

  $(".feature-text").hide(0);
  $(".feature-text").slideDown(2000);
});

var chatbotVisibility = false;
var chatSection = document.getElementsByClassName('chat')[0];

const toggleChatBot = () => {
  chatbotVisibility ? chatSection.style.display = 'block' : chatSection.style.display = 'none';
  chatbotVisibility =! chatbotVisibility;
  $(".chat").toggle(500);
}

const getResponse = () => {
  let chat = []
  let reqres = document.getElementsByClassName('message')
  document.getElementsByClassName('chats')[0].innerHTML += `
  <div class='sent message'>${document.getElementById('chatbox').value}</div>
  `
  document.getElementById('chatbox').value = ''

  for (let i = 0; i < reqres.length; i++) {
    if (i % 2 == 0) chat.push({
      role: 'user',
      parts: reqres[i].innerText
    })
    else chat.push({
      role: 'model',
      parts: reqres[i].innerText
    })
  }

  fetch('http://localhost:8000/api/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({chat})
  }).then((res) => {
    return res.json()
  }).then((response) => {
    document.getElementsByClassName('chats')[0].innerHTML += `
  <div class='received message'>${response}</div>
  `
  })
}
