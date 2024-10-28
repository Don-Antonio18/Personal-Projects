def findLastLeapYears(yearBounds):
    def is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 4 != 0:
            return False
        elif year % 100 == 0  and year % 400 != 0:
            return False
        else: 
            return False
    
    def nearest_leap_year(year):
        prev_leap = year
        while prev_leap > 0: #year shouldn't be less than 0
            prev_leap -= 1   # decrements year backwards,
            if is_leap_year(prev_leap): #until leap year is found
                break
        
        next_leap = year
        while next_leap < 5000:  #year shouldn't exceed 5000
            next_leap += 1   #increments year forwards, 
            if is_leap_year(next_leap): #until leap year is found 
                break

        #check distance between year and last leap year
        time_since = year - prev_leap if prev_leap > 0 else ('infinite time since last leap')
        #check distance between year and next_leap leap year
        time_to_next_leap = next_leap - year

        #return last leap year if it's closer than next leap year
        return prev_leap if time_since >= time_to_next_leap else next_leap

        #loop through list of years and return closet leap year
        return [nearest_leap_year for year in yearBounds]

        
        
