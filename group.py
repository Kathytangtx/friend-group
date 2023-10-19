"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill': {
        'age': 26,
        'job': 'biologist',
        'relationship':{
            'friend' : 'zalika',
            'partner' : 'john'
        },
    },
    'Zalika':{
        'age':'28',
        'job':'artist',
        'relationship' :{
            'friend' :'jill'
        },
    },
    'John': {
        'age' : 27,
        'job' : 'writer',
        'relationship': {
            'partner' : 'Jill'
        },
    }, 
    'Nash':{
        'age' : 34,
        'job' : 'chef',
        'relationship':{
            'landlord' : 'Zalika',
            'cousin' : 'john'


        }
    }   
    }



    





#Create an example instance, in an editor or a notebook, of a structure for this group:
# Jill is 26, a biologist and she is Zalika's friend and John's partner.
 #Zalika is 28, an artist, and Jill's friend
#john is 27, a writer, and Jill's partner.
#Nash is 34, a chef, John's cousin and Zalika's landlord.