def d():
    animal = "cat"
    def e():
        nonlocal animal
        animal = "rat"
        print("Inside nested function:", animal)
    
    print("Before using e():", animal)
    e()
    print("After using e():", animal)

animal = "dog"
d()
print("Global animal:", animal)