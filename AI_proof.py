from bs4 import BeautifulSoup
import re
import os
import enchant
from transformers import pipeline

def highlight_errors(text, grammar_checker):
    """Identify and highlight errors in text using both regex and AI."""
    spell_checker = enchant.Dict("en_US")
    words = text.split()
    highlighted_text = []
    
    patterns = {
        "spelling_errors": [r"\bteh\b", r"\brecieve\b", r"\boccured\b"],  # Example misspellings
        "grammar_errors": [r"\b(a|an) (apple|egg|orange)\b", r"\b(he|she|it) (were|are)\b"],  # Grammar mistakes
        "punctuation_mistakes": [r"\b(However|Therefore|Moreover),[^ ]", r"\?\."],  # Punctuation errors
        "sentence_construction": [r"[^.!?]\n[A-Z]", r", and ,", r", but ,"],  # Sentence structure mistakes
        "nonidiomatic_expressions": [r"\bcomprise of\b", r"\bdue to the fact that\b"]  # Non-idiomatic expressions
    }
    
    for word in words:
        if not spell_checker.check(word):
            highlighted_text.append(f'<span style="background-color: red;">{word}</span>')
        else:
            highlighted_text.append(word)
    text = " ".join(highlighted_text)
    
    for category, regex_list in patterns.items():
        for regex in regex_list:
            text = re.sub(regex, lambda m: f'<span style="background-color: red;">{m.group(0)}</span>', text, flags=re.IGNORECASE)
    
    # AI-based grammar correction
    ai_suggestions = grammar_checker(text)
    for suggestion in ai_suggestions:
        incorrect_text = suggestion['word']
        text = text.replace(incorrect_text, f'<span style="background-color: red;">{incorrect_text}</span>')
    
    return text

def process_html_file(input_file, output_file, grammar_checker):
    """Process an HTML file, highlight errors, and save the corrected file."""
    with open(input_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    for tag in soup.find_all(["p", "li", "span", "div"]):
        if tag.string:
            tag.string.replace_with(BeautifulSoup(highlight_errors(tag.string, grammar_checker), "html.parser"))
    
    with open(output_file, "w", encoding="utf-8") as output:
        output.write(str(soup))
    
    print(f"Processed: {input_file} -> {output_file}")

# Initialize local AI-based grammar checker
grammar_checker = pipeline("fill-mask", model="bert-base-cased")

# Example Usage
input_files = ["peerj-18835.html", "peerj-18918.html", "peerj-cs-2622.html", "peerj-cs-2626.html", "peerj-cs-2637.html"]
output_files = [f"corrected_{os.path.basename(f)}" for f in input_files]

for inp, out in zip(input_files, output_files):
    process_html_file(inp, out, grammar_checker)
