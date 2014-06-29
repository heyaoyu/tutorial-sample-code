import time

class ActiveEngine(object):

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        while len(self.commands) > 0:
            command = self.commands.pop(0)
            command.execute()


class WakeUpCommand(object):

    def __init__(self):
        self.executed = False

    def execute(self):
        self.executed = True


class SleepCommand(object):

    def __init__(self, millseconds, ae, wakeup_command):
        self.counter = 0
        self.sleeptime = millseconds
        self.engine = ae
        self.wakeup_command = wakeup_command
        self.started = False
        self.startTime = None

    def execute(self):
        self.counter += 1
        currentTime = round(time.time()*1000)
        if(not self.started):
            self.started = True
            self.startTime = currentTime
            self.engine.add_command(self)
        else:
            delta = currentTime - self.startTime
            if(delta < self.sleeptime):
                self.engine.add_command(self)
            else:
                self.engine.add_command(self.wakeup_command)


def main():
    wakeup = WakeUpCommand()
    ae = ActiveEngine()
    sleepCommand = SleepCommand(5000, ae, wakeup)
    ae.add_command(sleepCommand)
    start = round(time.time()*1000)
    ae.run()
    stop = round(time.time()*1000)
    delta = stop - start
    print sleepCommand.counter
    print delta

if __name__ == '__main__':
    main()