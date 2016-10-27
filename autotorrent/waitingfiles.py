class WaitingFiles(object):
    def __init__(self):
        self.waitingfiles = []

    def insert(self, fn, tn):
        self.waitingfiles.append([fn, tn])

    def getone(self):
        if self.waitingfiles:
            return self.waitingfiles.pop(0)
        return None
