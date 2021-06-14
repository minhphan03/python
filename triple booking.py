
class MyCalendarTwo:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.calendar) - 1):
            [s, e] = self.calendar[i]
            if (s < end and start < e):
                [st, en] = [max(start, s),min(end, e),]
                for j in range(i + 1, len(self.calendar)):
                    [s_, e_] = self.calendar[j]
                    
                    if st < e_ and s_ < en:
                        print("false")
                        return False

        self.calendar.append([start, end])
        return True
