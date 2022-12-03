import random

class Participant:
    def __init__(self, name, email, forbidden_matches):
        self.name = name
        self.email = email
        self.forbidden_matches = forbidden_matches
        self.assignee = None

    def match(self, possibleAssignments):
        size = len(possibleAssignments)

        if size == 0:
            return False

        match = random.randint(0, size-1)
        self.assignee = possibleAssignments[match]

        return True

def match(participants):
    success = False

    while not success:
        success = True
        matched = []

        for p1 in participants:
            possibleMatches = []
            for p2 in participants:
                if p1 != p2 and not p2 in matched and not p2.name in p1.forbidden_matches:
                    possibleMatches.append(p2)
            success = success and p1.match(possibleMatches)
            matched.append(p1.assignee)