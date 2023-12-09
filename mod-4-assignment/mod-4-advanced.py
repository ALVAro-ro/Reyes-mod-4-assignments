'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if to_member or from_member not in social_graph:
        print("Error: User not found.")
    
    elif to_member in social_graph.get(from_member).get("following"):
        
        if from_member in social_graph.get(to_member).get("following"):
            return "friends"
        else:
            return "follower"
        
    elif from_member in social_graph.get(to_member).get("following"):
        
        return "followed by"
    
    else:
        return "no relationship"



def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    row_set=()
    i=0
    for row in board:
        row_set=set(board[i])
        
        if len(row_set)==1:
            return str(row_set) + " is the winner"
        i+=1
    
    col_list=(list(zip(*board)))
    i=0
    for col in col_list:
        col_set=set(col_list[i])
        
        if len(col_set)==1:
            return str(col_set) + " is the winner"
        i+=1
    
    i=0
    updown_diagonal = set([board[i][i]for i,v in enumerate(board)])
    
    if len(updown_diagonal) == 1:
        return str(updown_diagonal) + " is the winner"
    
    grid=len(board)
    i=0
    downup_diagonal = set([board[grid-1-i][i]for i,v in enumerate(board)])
    
    if len(downup_diagonal) == 1:
        return str(downup_diagonal) + " is the winner"
    
    else:
        return "NO WINNER"


def eta(first_stop, second_stop, route_map = {
         ("upd","admu"):{
             "travel_time_mins":10
         },
         ("admu","dlsu"):{
             "travel_time_mins":35
         },
         ("dlsu","upd"):{
             "travel_time_mins":55
         }
        }):
    
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    current_stop = first_stop
    travel_time = 0
    
    
    if current_stop == second_stop:
        return "You are already at your destination."
    
    while current_stop != second_stop:
        
        for x in route_map.keys():
            
            if current_stop==x[0]:
                next_stop = x[1] 
        
        current_leg = (current_stop,next_stop)
        
        travel_time += route_map[current_leg]["travel_time_mins"]
        
        current_stop = next_stop
        
    return "ETA: " + str(travel_time) + " minutes"