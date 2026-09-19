import os

def process_text(text: str) -> str:
    """Utility to format and clean text input before processing."""
    return text.strip().capitalize()

def main():
    sample_input = "  hello world from openai project  "
    result = process_text(sample_input)
    print(f"Original: '{sample_input}'")
    print(f"Processed: '{result}'")

if __name__ == "__main__":
    main()
