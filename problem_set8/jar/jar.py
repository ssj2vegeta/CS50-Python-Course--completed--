class Jar():
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError
        self.jarcapacity= capacity
        self.jarsize = 0


    def __str__(self):
        outputstring = ""
        try:
            for i in range(int(self.jarsize)):
                outputstring = outputstring + "🍪"
        except:
           return "empty"
        finally:
            return outputstring
    def deposit(self, n):
        if n + self.jarsize > self.jarcapacity:
            raise ValueError
        else:
            self.jarsize += n

    def withdraw(self, n):
         if self.jarsize - n < 0:
            raise ValueError
         else:
            self.jarsize -= n

    @property
    def capacity(self):
        return self.jarcapacity

    @property
    def size(self):
        return self.jarsize

def main():
    jar = Jar()
    jar.jarsize = 5
    print(jar)



if __name__ == "__main__":
    main()