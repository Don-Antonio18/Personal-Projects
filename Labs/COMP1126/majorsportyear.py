def majorSportYear(x):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "\n'Olympics, Copa America and European Championships' "
    elif year % 4 == 2:
        return "\n'FIFA Men World Cup' "
    elif year % 4 == 3:
        return "\n'ICC Cricket World Cup, FIFA Women World Cup and Netball World Cup'"
    elif year % 4 != 2:
        return"\n'IAAF World Athletic Championships and Gold Cup'"
    else:
        return "\n'IAAF World Athletic Championships and Gold Cup'"
year = int(input("\n Enter Major Sport Year: "))
print (majorSportYear(year))