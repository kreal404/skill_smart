history = ['']
current = 0
last_op = 0

def BastShoe(command: str) -> str:
    global history, current, last_op
    op = command.split(' ', 1)

    if op[0] == '1':
        if last_op in ['1', '2']:
            history = history[:current+1]
        history.append(history[current] + op[1])
        current += 1
        last_op = '1'
    elif op[0] == '2':
        if last_op in ['1', '2']:
            history = history[:current+1]
        history.append(history[current][:-int(op[1])])
        current += 1
        last_op = '2'
    elif op[0] == '3':
        index = int(op[1])
        if index < len(history[current]):
            return history[current][index]
        else:
            return ''
    elif op[0] == '4':
        if current > 0:
            current -= 1
        last_op = '4'
    elif op[0] == '5':
        if current < len(history) - 1:
            current += 1
        last_op = '5'

    return history[current]

