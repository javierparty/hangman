import random as r

text = 'Heft Haus Sofa Liebe Hund Katze Auto'
words = set(text.split())
wrong_tries = set()
playing_word = r.choice(list(words))
p_w = playing_word.casefold()
board_done = [x + ' ' for x in playing_word]
board = ['_ ' for x in playing_word]

while board != board_done and len(wrong_tries) < 4:
    print('\n' + ''.join(board) + '\n\n' +
          'Schon probiert: ' + ''.join([x + ' ' for x in wrong_tries]) + '\n'
          'Versuche: ' + str(4 - len(wrong_tries)))
    let = input('Welcher Buchstabe? ').casefold()
    if let == p_w:
        board = board_done
    elif let == '':
        print('\ndas verstehe ich nicht...')
    elif let not in p_w:
        wrong_tries.add(let.upper())
        if len(let) > 1:
            print('\nNein, ' + let.upper() + ' ist nicht das Wort...')
        else:
            print('\n' + let.upper() + ' ist leider nicht im Wort...')
    else:
        index = 0
        while let in p_w[index:]:
            index = p_w.find(let, index)
            board[index] = board_done[index]
            index += 1

if board == board_done:
    print('\n' + ''.join(board_done) + ' --> Gewonnen!' + '\n')
else:
    print('\n:-( Schade, du hast keine Versuche übrig.\n' +
          'Das Wort war: ' + ''.join(board_done) + '\n')
