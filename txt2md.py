# Simple txt to README.md
# Just download txt and png after updating from
# https://coggle.it/diagram/Wh2vqsX_9wABvABu and
# run this script
head='# Deep Neural Network Architecture Mindmaps\n' \
     'There are so many new models and architectures. ' \
     'If you find something interesting and worth paying attention to, ' \
     'please send us a pull requests (PR) and write issues.\n' \
     '`README.md` is automatically generated. Please send PRs on the `Neural Net Arch Genealogy.txt` file.\n' \
     '## Mindmap Coggle Link\n' \
     'https://coggle.it/diagram/Wh2vqsX_9wABvABu\n' \
     '![https://coggle.it/diagram/Wh2vqsX_9wABvABu](DNN_Mindmap.png)\n' \
     '## Text Version\n' \
     'This is automatically generated. Please send a PR on the `DNN.txt` file.\n'

tail = '\n## Contributions\nYour pull requests and issues are always welcome.' \

with open('DNN.txt') as fin, open('README.md', 'w') as fout:
    fout.write(head)
    for line in fin:
        tab_count = line.count('\t')
        if not tab_count:
            continue

        spaces = ['  ' for i in range(tab_count-1)]
        fout.write(''.join(spaces) + '* ' + line.replace('\t', ''))

    fout.write(tail)
