#   ID Number: 620170333
#   Hackerrank Handle: antoniokerruni
#   Hackerank Exercise: Leaps and Bounds

def findLastLeapYears(yearBounds):
    def is_leap_year(year):
        if year % 4 != 0:
            return False
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
        
    def find_closest_leap_year(year):
        # Find previous leap year
        prev = year
        while prev > 0:
            prev -= 1
            if is_leap_year(prev):
                break
                
        # Find next leap year
        next_leap = year
        while next_leap < 5000:  
            next_leap += 1
            if is_leap_year(next_leap):
                break
        
        # Compare distances
        prev_distance = year - prev if prev > 0 else float('inf')
        next_distance = next_leap - year
        
        # Return the closer one, preferring the earlier year if distances are equal
        return prev if prev_distance <= next_distance else next_leap
    
    # Process each year and return results
        return [find_closest_leap_year(year) for year in yearBounds]