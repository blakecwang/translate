// Load the OpenAI API key
const openaiApiKey = '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';

// Initialize the OpenAI API client
const openai = require('@openai/api')(
  openaiApiKey
);

// Get references to the input and output text areas and the translation button
const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');
const translateBtn = document.getElementById('translate-btn');

// Add a click event listener to the translation button
translateBtn.addEventListener('click', async () => {
  // Get the text from the input text area
  const input = inputText.value;

  // Make the translation request to the OpenAI API
  const response = await openai.translation.translate({
    text: input,
    target_language: 'fr',
  });

  // Set the translated text in the output text area
  outputText.value = response.translations[0].translation;
});
