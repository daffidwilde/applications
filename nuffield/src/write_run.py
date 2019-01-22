with open('run.sh', 'w') as f:
    for i in range(1, 4):
        f.write(f'python make_wordcloud.py {i}' + '\n')
