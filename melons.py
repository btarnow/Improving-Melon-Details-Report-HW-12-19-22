
melons = {
    'Honeydew': {
        'price': 0.99,
        'seedless': True,
        'flesh_color': None,
        'rind_color': None,
        'average_weight': None,
    },

    'Crenshaw': {
        'price': 2.00,
        'seedless': False,
        'flesh_color': None,
        'rind_color': None,
        'average_weight': None,
    },

    'Crane': {
        'price': 2.50,
        'seedless': False,
        'flesh_color': None,
        'rind_color': None,
        'average_weight': None,
    },

    'Casaba': {
        'price': 2.50,
        'seedless': False,
        'flesh_color': None,
        'rind_color': None,
        'average_weight': None,
    },

    'Cantaloupe': {
        'price': 0.99,
        'seedless': False,
        'flesh_color': None,
        'rind_color': None,
        'average_weight': None,
    }
}

#MY FIRST ATTEMPT: 
# ##########################################################################################
# UPDATED THE DATA INTO ONE DICT. I REALIZED THAT NESTING A DICT. WITHIN A DICT. WOULD BE MORE READABLE
#Dictionary Key: Melon Name
#Dictionary Value: A tuple that include...
    #[0] = melon_price
    #[1] = melon_seedlessness
    #[2] = fresh_color
    #[3] = rind_color 
    #[4] = average_weight
# 
# melons = {
#     'Honeydew': (0.99, True, None, None, None),
#     'Crensaw': (2.00, False, None, None, None),
#     'Crane': (2.50, False, None, None, None),
#     'Casaba': (2.50, False, None, None, None),
#     'Cantaloupe': (0.99, False, None, None, None),
# }


##BELOW IS THE ORIGINAL PROVIDED CODE THAT WE NEED TO UPDATE TO IMPROVE PER HW DIRECTIONS:
##########################################################################################
# melon_names = {
#     1: 'Honeydew',
#     2: 'Crenshaw',
#     3: 'Crane',
#     4: 'Casaba',
#     5: 'Cantaloupe',
# }

# melon_prices = {
#     1: 0.99,
#     2: 2.00,
#     3: 2.50,
#     4: 2.50,
#     5: 0.99,
# }

# melon_seedlessness = {
#     1: True,
#     2: False,
#     3: False,
#     4: False,
#     5: False,
# }