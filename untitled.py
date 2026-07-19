import re
import random

# Each rule: a compiled regex pattern paired with one or more possible responses.
# This structure is intentionally simple to extend later — a new rule is just
# one more (pattern, responses) tuple, and the fallback hook below is where
# a future AI service call would plug in.

rules = [
    (re.compile(r"\b(hi|hello|hey)\b", re.IGNORECASE),
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]),
    (re.compile(r"\bhow are you\b", re.IGNORECASE),
        ["I'm just a program, but I'm running smoothly! How about you?"]),
    (re.compile(r"\byour name\b", re.IGNORECASE),
        ["I'm a simple rule-based chatbot built for MSAI-631."]),
    (re.compile(r"\b(help|what can you do|capabilities)\b", re.IGNORECASE),
        ["I can greet you, tell you my name, chat a little, and respond to "
         "basic questions. Try asking 'what can you do', saying hello, or "
         "asking how I am."]),
    (re.compile(r"\b(bye|goodbye|exit|quit)\b", re.IGNORECASE),
        ["Goodbye! Have a great day."]),
    (re.compile(r"\bjoke\b", re.IGNORECASE),
        ["Why did the developer go broke? Because they used up all their cache."]),
]

def call_ai_service(user_input):
    """
    Placeholder extension point. In a future assignment this is where a call
    to an AI service (e.g., Azure Cognitive Services or a transformer model)
    would go. For now it just returns a generic fallback.
    """
    return None

def get_response(user_input):
    if not user_input or not user_input.strip():
        return "I didn't catch that — could you type something?"

    for pattern, responses in rules:
        if pattern.search(user_input):
            return random.choice(responses)

    ai_response = call_ai_service(user_input)
    if ai_response:
        return ai_response

    return ("I'm not sure how to respond to that yet. Try 'help' to see what I can do.")