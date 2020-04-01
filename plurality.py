import sys

candidates = []
candidate = {}

arg = sys.argv
if len(arg) > 10:
    print('max of candidates is 9')
    exit()


def add_candidate(args):
    for i in range(1, len(arg)):
        candidate['name'] = arg[i]
        candidate['vote'] = 0
        candidates.append(candidate.copy())


def vote(number_of_vote):
    i = 0
    while i < number_of_vote:
        voted = input('Vote:')
        for ind, vote in enumerate(candidates):
            if voted in candidates[ind]['name']:
                candidates[ind]['vote'] += 1
                i += 1
                invalid = False
                break
        else:
            invalid = True
        if invalid:
            print('Invalid vote.')


def print_winner():
    max_vote = 0
    for i in range(len(candidates)):
        if candidates[i]['vote'] > max_vote:
            max_vote = candidates[i]['vote']
    for i in range(len(candidates)):
        if candidates[i]['vote'] == max_vote:
            print(candidates[i]['name'])


add_candidate(arg)
number_of_vote = int(input('Number of voters: '))
vote(number_of_vote)
print_winner()

