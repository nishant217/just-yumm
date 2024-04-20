document.addEventListener('DOMContentLoaded', () => {
	const chatForm = document.getElementById('chat-form');
	const dishNameInput = document.getElementById('dish-name');

	chatForm.addEventListener('submit', async (e) => {
		e.preventDefault();
		const dishName = dishNameInput.value;
		const response = await askGemini(dishName);

		const chat = createChat(dishName, response);
		addChatToDOM(chat);

		dishNameInput.value = '';
	});
});

async function askGemini(message) {
  const url = '/ask_question/';
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ dish_name: message }),
  });
  const data = await response.json();
  return data.response;
}