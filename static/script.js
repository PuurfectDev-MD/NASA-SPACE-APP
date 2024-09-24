const words = ["Explore", "Learn", "Understand"];  // The words to type and delete
const typingSpeed = 200;  // Speed of typing (in milliseconds)
const deletingSpeed = 150;  // Speed of deleting (in milliseconds)
const delayBetweenWords = 1200;  // Delay between the end of typing one word and start of deleting
const delayBeforeTyping = 500;  // Pause before typing the next word
let currentWordIndex = 0;
let currentLetterIndex = 0;
let isDeleting = false;

const typingTextElement = document.getElementById('typing-text');

function type() {
    const currentWord = words[currentWordIndex];
    
    if (!isDeleting && currentLetterIndex <= currentWord.length) {
        // Typing the word
        typingTextElement.textContent = currentWord.slice(0, currentLetterIndex);
        currentLetterIndex++;
        setTimeout(type, typingSpeed);
    } else if (isDeleting && currentLetterIndex >= 0) {
        // Deleting the word
        typingTextElement.textContent = currentWord.slice(0, currentLetterIndex);
        currentLetterIndex--;
        setTimeout(type, deletingSpeed);
    } else if (!isDeleting && currentLetterIndex > currentWord.length) {
        // Start deleting after a short delay
        isDeleting = true;
        setTimeout(type, delayBetweenWords);
    } else if (isDeleting && currentLetterIndex < 0) {
        // Clear the text completely before typing the next word
        typingTextElement.textContent = '';
        isDeleting = false;
        currentWordIndex = (currentWordIndex + 1) % words.length;  // Loop over the words
        currentLetterIndex = 0;  // Reset letter index before starting next word
        setTimeout(type, delayBeforeTyping);  // Wait before typing the next word
    }
}

// Start the typing effect
type();
