class MyString:
    def __init__(self, value=''):
        # Check if the value is a string; if not, print the message
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Check if the new value is a string; if not, print the message
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = new_value

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')
    
    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')
        
    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Use regular expressions to split by sentence-ending punctuation
        import re
        sentences = re.split(r'[.!?]', self.value)
        # Strip whitespace and filter out empty sentences
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
