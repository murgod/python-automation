from alive_progress import alive_bar



with alive_bar(3) as bar:
    for i in range(1000000000000000000000000000):
        bar()
