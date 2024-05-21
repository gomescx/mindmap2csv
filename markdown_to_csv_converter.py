import csv

def parse_markdown_to_csv(markdown_file, csv_file):
    with open(markdown_file, 'r') as md_file:
        lines = md_file.readlines()

    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Level 2', 'Level 3', 'Level 4', 'Level 5'])

        level_2 = level_3 = level_4 = level_5 = ''
        for line in lines:
            line = line.strip()
            if line.startswith('## '):
                level_2 = line[3:]
                level_3 = level_4 = level_5 = ''
            elif line.startswith('### '):
                level_3 = line[4:]
                level_4 = level_5 = ''
            elif line.startswith('#### '):
                level_4 = line[5:]
                level_5 = ''
            elif line.startswith('##### '):
                level_5 = line[6:]
            else:
                continue

            csv_writer.writerow([level_2, level_3, level_4, level_5])

if __name__ == '__main__':
    parse_markdown_to_csv('data/source.markdown', 'data/output.csv')
