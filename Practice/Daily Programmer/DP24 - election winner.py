__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/qxuug/3152012_challenge_25_easy/
In an election, the person with the majority of the votes is the winner. Sometimes due to similar number of votes, there are no winners.
Your challenge is to write a program that determines the winner of a vote, or shows that there are no winners due to a lack of majority.
"""

def compare_votes(list):
    """

    !!!Misunderstood challenge!!!

    compares vote counts for candidates
    :param args: list of vote counts
    :return: index of winning vote, or -1 for no winner
    """
    total = sum(list)
    if max(list)/total > .5:
        return list.index((max(list)))
    else:
        return -1

def count_votes(votes):
    """
    compares list of votes for a candidate by name
    :param list: ["Obama","Romney","Warren"...]
    :return:winner or "runoff"
    """
    cand_dict = {}
    top = []
    topvotes = 0
    total = 0
    for person in votes:
        cand_dict[person] +=1
        total +=1
    for candidate in cand_dict:
        if cand_dict[candidate] > topvotes:
            top[0] = candidate
            del top[1:]
            topvotes = cand_dict[candidate]
        elif cand_dict[candidate] == topvotes:
            top.append(candidate)
        else:
            pass
    if len(top)>1:
        return "Runoff between {} and {}".format(top[0],top[1])
    else:
        return top[0]

def count_votes_better(votes):
    cand_dict = {}
    topvotes = 0
    total = 0
    for person in votes:
        cand_dict[person] +=1
        total +=1
    for i in range(2):  #  have to do twice to make sure to compare the first one to any new max, and delete it if lower
        for candidate in cand_dict:
            if cand_dict[candidate] >= topvotes:
                topvotes = cand_dict[candidate]
            else:
                del cand_dict[candidate]
    return cand_dict.keys()

def winner(votes):
    try:
        return [e for e in set(votes) if(votes.count(e) > len(votes)/2)][0] # [0] formats it to just the item, not a list of len 1
    except IndexError:
        return None

def plurality(election):
    import collections
    votes = sorted(collections.Counter(election).items(),
                   key=lambda a: a[1], reverse=True)
    if votes[0][1] > votes[1][1]:
        return votes[0][0], float(votes[0][1])/len(election)
    else:
        return None, 0.0

def winner1(election):
    plur, fraction = plurality(election)
    if fraction >= 0.5:
        return plur
    else:
        return None

print(winner(["a","c","c","b","b"]))