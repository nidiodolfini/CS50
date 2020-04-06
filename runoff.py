import sys
preferences = [[],[]]

def vote(voter): #, rank, name
    for i in range(voter):
        vote = input(f'Rank {i+1}: ')




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


candidates = []
candidate = {}

arg = sys.argv
if len(arg) > 10:
    print('max of candidates is 9')
    exit()

voters = int(input('Number of voters:'))
vote(voters)