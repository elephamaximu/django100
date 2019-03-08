class CodeConverter:
    regex = r'\d{5}'

    def to_python(self, value):
        print("to_python함수", type(value), value)
        return int(value) 

    