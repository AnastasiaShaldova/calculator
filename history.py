class History:
    def __init__(self):
        self.filename = 'history.txt'

    def save_history(self, operation, result):
        with open(self.filename, 'a') as file:
            file.write(f'{operation}: {result}\n')

    def show_history(self):
        with open(self.filename, 'r') as file:
            history = file.read()
        print('История операций:')
        print(history)
