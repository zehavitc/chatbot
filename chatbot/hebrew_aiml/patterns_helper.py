__author__ = 'zehavitc'


def ngrams(input, n):
    input = clean_input(input).split()
    output = []
    for i in range(len(input) - n + 1):
        output.append(' '.join(c for c in input[i:i + n]))
    return output


def clean_input(input):
    characters_to_remove = [u',', u'.', u'?', u':', u';']
    return ''.join(c for c in input if c not in characters_to_remove)
    # n = ngrams("a b cd ef",2)

    # print(n)
