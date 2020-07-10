# indexing
records = [
    ('Tim', 'Texas'),
    ('Adam', 'Florida'),
    ('Austin', 'Florida'),
    ('Kai', 'South Carolina'),
]
#     Understand
# given a list of records, build an index
# so we can quickly find everyone in a given state
#     plan
# iterate through the tuples in our list
# Build a dictionary as we go
# use states as keys, names as values
# if a state isnt in dictionary, add it as key
##value: [name1, name2, name3]
# possible value data structures: list, set, nest hastable
###{state: {name:lastname}}
# if we have good pseudocode, then we're done planning
'''for name, state in records:
    value = index.setdefault(state, [])
    value.append(name)'''


def build_index(records):
    index = {}
    # iterate through list
    for name, state in records:
        # for reach pair, check if the state is in the dictionary
        if state in index:
            # if so, append the name to the list
            index[state].append(name)
    # if not, add the key and list (with name in it)
        else:
            index[state] = [name]
    return index


idx = build_index(records)
print(idx['Florida'])
