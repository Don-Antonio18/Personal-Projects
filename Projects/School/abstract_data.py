# given a tuple of points, create abstraction for points:
#testing to see if i can push 

def makePoint(x,y):
# write function to pull out value of ur functions
  return (x,y)

def XCoord(pt):
  return pt[0]

def YCoord(pt):
  return pt[1]

# in order to create a new point as tuple:
new_point = makePoint(2, 4)
print (new_point) 

# return coordinates 
print (XCoord(new_point))
print (YCoord(new_point))

#create start and end segments
def segStart(segment):
  return segment[0]

def segEnd(segment):
  return segment[1]
  
# a LINE SEGMENT is a pair of points:
def makeSegment(start, end):
  # return points as tuple:
  return new_point(start) + new_point(end)

# create two lines:
point1 = makePoint(1,2)
point2 = makePoint(3,4)
