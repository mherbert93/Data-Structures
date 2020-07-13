

our_list = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# for val in our_list:
#     print(val)


def our_function(our_list):
    for val in our_list:
        if isinstance(val, list):
            our_function(val)
        else:
            print(val)

our_function(our_list)