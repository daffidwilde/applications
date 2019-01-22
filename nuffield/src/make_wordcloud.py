import string
import sys

from wordcloud import WordCloud

if __name__ == '__main__':
    student_num = str(sys.argv[1])
    file_name = f'../personal_statements/student_{student_num}.txt'

with open(file_name, 'r') as f:
    alltext = f.read()
    remove = dict.fromkeys(map(ord, '\n' + string.punctuation))
    text = alltext.translate(remove).lower()

def main():

    wordcloud = WordCloud(
        width=1200,
        height=600,
        margin=0,
        max_words=500,
        collocations=False,
        background_color=None,
        mode='RGBA').generate(text).to_file(file_name.replace('.txt', '.png'))

if __name__ == '__main__':
    main()
