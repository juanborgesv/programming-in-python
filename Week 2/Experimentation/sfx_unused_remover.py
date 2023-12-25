'''
Deletes every line that has "// No references" in a txt. file.
'''
with open('old_sfx.txt', 'r') as file:
    all_content = file.readlines()

    with open('new_sfx.txt', 'w') as new_file:
        with open('changes_sfx.text', 'w') as changes_file:
            for line in all_content:
                if '// No references.' not in line:
                    new_file.write(line)
                else:
                    changes_file.write(line)
