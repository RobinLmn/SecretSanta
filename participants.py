import random

class Participant:
    def __init__(self, name, email, address, assignee=None):
        self.name = name
        self.email = email
        self.address = address
        self.assignee = None
    
    def set_assignee(self, assignee):
        self.assignee = assignee

    def match(self, possibleAssignments):
        size = len(possibleAssignments)

        if size == 0:
            return False

        match = random.randint(0, size-1)
        self.assignee = possibleAssignments[match]

        return True

def check(p1, p2, forbiddenPairs):
    for c in forbiddenPairs:
        if p1 in c and p2 in c:
            return False
    return True 

def match(participants, forbiddenPairs):
    success = False

    while (not success):
        success = True
        matched = []

        for p in participants:
            possibleMatch = []
            for p2 in participants:
                if p2.address != p.address and not p2 in matched and check(p.name, p2.name, forbiddenPairs):
                    possibleMatch.append(p2)

            success = success and p.match(possibleMatch)
            matched.append(p.assignee)