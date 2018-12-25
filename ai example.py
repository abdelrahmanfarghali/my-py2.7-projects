def treesearch(problem):
    frontier = []
    loop:
        if frontier is empty:return fail
        path = remove0choice(frontier)
        s = pathend
        if s is a goal:return path
        for a in actions:
            add[path+a>result(s,a)]
            to frontier
            unless result(s,a) in frontier + explored

            #####

            
