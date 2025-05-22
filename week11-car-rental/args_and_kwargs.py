
def test(a, *args, **kwargs):
    print("A:", a)
    print("Args:", args)
    print("Kwargs:", kwargs)


test(10, 12, 45, 54, 24, name='john', age=45)