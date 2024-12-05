''''Write a function shipping_charges that takes weight of a package and where it is national “N” or
international “I” destination to which it is being shipped. The function calculates the shipping charges
and returns the values.'''


def shipping_charges(x,z):

    weight_in_pounds = x
    if weight_in_pounds < 2:
        cost = 1.10 * weight_in_pounds
    elif weight_in_pounds > 2 and weight_in_pounds < 6:
        cost = 2.20 * weight_in_pounds
    elif weight_in_pounds > 6 and weight_in_pounds < 10:
        cost = 3.7 * weight_in_pounds
    elif weight_in_pounds > 10 and z == "N":
        cost = 3.8 * weight_in_pounds
    elif weight_in_pounds > 10 and z == "I":
        cost = 4.50 * weight_in_pounds
    return f"The cost is {cost}"

        
package_weight = float(input("Enter the weight of the package to 2 decimal places: "))
location = input("Enter N for National and I for International Shipping: ")
print("The cost of the item is ", (shipping_charges (package_weight,location)) )


