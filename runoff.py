import sys
preferences = [[],[]]
candidates = []
candidate = {}

def vote(voter, candidates): #, rank, name
    for j in range(voter):
        i = 1
        while i < len(candidates)+1:
            voted = input(f'Rank {i}: ')
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
        print()

def add_candidate(args):
    for i in range(1, len(arg)):
        candidate['name'] = arg[i]
        candidate['vote'] = 0
        candidate['eliminated'] = False
        candidates.append(candidate.copy())

def tabulate():
    pass


def print_winner():
    pass


def find_min():
    pass


def is_tie(min):
    pass


def eliminate(min):
    pass


arg = sys.argv
if len(arg) > 10:
    print('max of candidates is 9')
    exit()
add_candidate(arg)

votes = int(input('Number of voters:'))
vote(votes, candidates)
print(candidates)