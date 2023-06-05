def tempo():
    import datetime
    test = datetime.datetime.today()
    teste = str(test + datetime.timedelta(days=7))
    return teste[0:10]


def tempo2():
    from datetime import datetime
    te = datetime.now().date()
    return te
