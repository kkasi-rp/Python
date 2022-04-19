
class Simple:
    def __init__(this, a):
        this.a = a

    def get_a(this):
        return this.a

obj = Simple(10)
print(obj.a)
print(obj.get_a())