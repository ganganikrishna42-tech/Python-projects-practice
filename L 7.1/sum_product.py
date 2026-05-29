def sum_product():
    a = [1, 2, 3, 4, 5]
    sum_of_list = sum(a)
    product_of_list = 1
    for num in a:
        product_of_list *= num
    print("Sum of the list is: ", sum_of_list)
    print("Product of the list is: ", product_of_list)

sum_product()