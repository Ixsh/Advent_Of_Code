# Open the file and split entries based upon empty lines
with open('C:/Users/durha/Desktop/input.txt', 'r', encoding='utf-8') as f:
  arr = f.read().split('\n\n')
  
f.close()


def count_answers(answers, op = 1):
    """
    Finds the sum of the questions answered.
    op = 1: Sums the counts of questions answered 'yes' by anyone in a group
    op = 2: Sums the counts of questions answered 'yes' by all in a group
    """
    count = 0
    for answer in answers:
        if op == 1:
            count += len(set(''.join(answer.split('\n'))))
        elif op == 2:
            count += len(set.intersection(*[set(elem) for elem in answer.split('\n')]))
    return count


# print(count_answers(arr))
print(count_answers(arr, op = 2))
