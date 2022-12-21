import streamlit as st 
st.title("MATH TOOL")
st.header("The all in one tool")
choice = st.sidebar.radio("Choose an options",["Home","Roots of the equation","Side of a right angled triangle","Perimeter","Area","Volume","Dot Product","Cross Product"])

if choice == "Home":
    st.write("So, what do you want to do today?")
    st.write("Chosen options from left sidebar")
    st.text("Hope it helps you!!")
    
if choice=="Roots of the equation":
    st.text("Roots of the equations")
    st.latex(r'''
        f \left(x\right) = ax^2 + bx + c
        ''')
    st.latex(r'''
        D^2 = (b^2 - 4ac)
        ''')
    st.write("Enter the coefficients")
    a=st.number_input("Enter the value of a: ")
    b=st.number_input("Enter the value of b: ")
    c=st.number_input("Enter the value of c: ")
    d=(b**2 - 4*a*c)**(1/2)
    if st.button("Submit"):
        st.write("The value of discriminant is",d)
        x1=(-b+d)/(2*a)
        x2=(-b-d)/(2*a) 
        st.write("The value of roots of the given equation are",x1,"and",x2)
    else:
        st.write("Please click on submit button")
        
if choice==('Side of a right angled triangle'):
    def pythagoras(a=0,b=0,c=0):
        st.latex(r'''
                Hypotenuse^2 = Perpendicular^2 + Base^2
                ''')
        st.write("Enter the sides")
        p=st.number_input("Enter the value of perpendicular: ")
        base=st.number_input("Enter the value of base: ")
        h=st.number_input("Enter the value of hypotenuse: ")
        if st.button("Submit"):
            if p==False:
                p=(h**2 - base**2)**0.5 
                st.write("The value of perpendicular is",p)
            elif base==False:
                base=(h**2 - p**2)**0.5
                st.write("The value of base is",base)
            elif h==False:
                h=(p**2 + base**2)**0.5
                st.write("The value of  hypotenuse is",h)
            else:
                st.write("Please enter values in two fields") 
        else:
            st.write("Please click on submit button")
    pythagoras()
if choice=="Perimeter":
    
    st.write("Perimeter of different shapes")
    
    choice1=st.radio('Shapes',['Square','Rectangle','Circle'])
    if choice1==("Square"):
        st.latex(r'''
                 Perimeter = 4*Side''')
        side=st.number_input("Enter the value of side:")
        perimeter=side*4
        if st.button("Submit"):
            st.write("Perimeter of Square is",perimeter)
        else:
            st.write("Please click on submit button")
            
    if choice1==("Rectangle"):
        st.latex(r'''
                 Perimeter = 2*\left(Length + Breadth\right)''')
        length=st.number_input("Enter the value of length:")
        breadth=st.number_input("Enter the value of breadth:")
        perimeter=2*(length + breadth)
        
        if st.button("Submit"):
            st.write("Perimeter of Rectangle is",perimeter)
        else:
            st.write("Please click on submit button")
           
    if choice1==("Circle"):
        
        st.latex(r'''
                 Circumference = 2*π*Radius''')
        radius=st.number_input("Enter the value of radius:")
        circumference=2*22*radius/7
        
        if st.button("Submit"):
          st.write("Circumference of Circle is",circumference)
        else:
            st.write("Please click on submit button")
if choice=='Area':
    st.write("Area of different shapes")
    
    choice1=st.radio('Shapes',['Square','Rectangle','Circle','Cylinder','Cone'])
    if choice1==("Square"):
        st.latex(r'''
                 Area = Side^2''')
        side=st.number_input("Enter the value of side:")
        area=side**2
        if st.button("Submit"):
            st.write("Area of Square is",area)
        else:
            st.write("Please click on submit button")
            
    if choice1==("Rectangle"):
        st.latex(r'''
                 Area = (Length*Breadth)''')
        length=st.number_input("Enter the value of length:")
        breadth=st.number_input("Enter the value of breadth:")
        area=(length*breadth)
        
        if st.button("Submit"):
            st.write("Perimeter of Rectangle is",area)
        else:
            st.write("Please click on submit button")
           
    if choice1==("Circle"):
        
        st.latex(r'''
                 Area = π*Radius^2''')
        radius=st.number_input("Enter the value of radius:")
        area=22*radius*radius/7
        
        if st.button("Submit"):
          st.write("Area of Circle is",area)
        else:
            st.write("Please click on submit button")
            
    if choice1==("Cylinder"):
            st.latex(r'''
                     Total Surface Area = 2*π*Radius*\left(Radius + Height\right)''')
            radius=st.number_input("Enter the value of radius:")
            height=st.number_input("Enter the value of height:")
            TSA=  2*22*radius*(radius + height)/7 
            if st.button("Submit"):
                st.write("Total Surface Area of cylinder is",TSA)
            else:
                st.write("Please click on submit button")
                
if choice=="Volume":
    st.write("Volume of different shapes")
    
    choice1=st.radio('Shapes',['Cube','Cuboid','Sphere','Cylinder','Cone'])
    if choice1==("Cube"):
        st.latex(r'''
                 Volume = Side^3''')
        side=st.number_input("Enter the value of side:")
        volume=side**3
        if st.button("Submit"):
            st.write("Volume of Cube is",volume)
        else:
            st.write("Please click on submit button")
            
    if choice1==("Cuboid"):
        st.latex(r'''
                 Volume = Length*Breadth*Height''')
        length=st.number_input("Enter the value of length:")
        breadth=st.number_input("Enter the value of breadth:")
        height=st.number_input("Enter the value of height:")
        volume=length*breadth*height
        
        if st.button("Submit"):
            st.write("Volume of Cuboid is",volume)
        else:
            st.write("Please click on submit button")
           
    if choice1==("Sphere"):
        
        st.latex(r'''
                 Volume = 4/3*π*Radius^3''')
        radius=st.number_input("Enter the value of radius:")
        volume=4*22*(radius**3)/21
        
        if st.button("Submit"):
          st.write("Volume of Circle is",volume)
        else:
            st.write("Please click on submit button")
    if choice1==("Cylinder"):
        st.latex(r'''
                 Volume = π*Radius^2*Height''')
        radius=st.number_input("Enter the value of radius:")
        height=st.number_input("Enter the value of height:")
        volume=22*radius*radius*height/7
        if st.button("Submit"):
            st.write("Volume of Cylinder is",volume)
        else:
            st.write("Please click on submit button")
            
    if choice1==("Cone"):
        st.latex(r'''
                 Volume = 1/3*π*Radius^2*Height''')
        radius=st.number_input("Enter the value of radius:")
        height=st.number_input("Enter the value of height:")
        volume=22*radius*radius*height/21
        if st.button("Submit"):
            st.write("Volume of Cone is",volume)
        else:
            st.write("Please click on submit button")
if choice=="Dot Product":
    st.write("Dot Product of Two Vectors")
    st.latex(r'''
             A = a1x + b1y + c1z''')
    st.latex(r'''
             B = a2x + b2y + c2z''')
    st.latex(r'''
             A.B = a1a2 + b1b2 + c1c2''')
    a1=st.number_input("Enter the value of a1:")
    b1=st.number_input("Enter the value of b1:")
    c1=st.number_input("Enter the value of c1:")
    a2=st.number_input("Enter the value of a2:")
    b2=st.number_input("Enter the value of b2:")
    c2=st.number_input("Enter the value of c2:")
    dot_product=a1*a2 + b1*b2 + c1*c2
    if st.button("Submit"):
        st.write("Dot Product of Two Vectors is",dot_product)
    else:
        st.write("Please click on submit button")
if choice=="Cross Product":
    st.write("Cross Product of Two Vectors")
    st.latex(r'''
              A = a1x + b1y + c1z''')
    st.latex(r'''
              B = a2x + b2y + c2z''')
    st.latex(r'''
              AxB = x\left(b1c2-b2c1\right) -y\left(a1c2-a2c1\right) + z\left(a1b2-a2b1\right)'''   )
    a1=st.number_input("Enter the value of a1:")
    b1=st.number_input("Enter the value of b1:")
    c1=st.number_input("Enter the value of c1:")
    a2=st.number_input("Enter the value of a2:")
    b2=st.number_input("Enter the value of b2:")
    c2=st.number_input("Enter the value of c2:")
    cross_productx=(b1*c2-b2*c1)
    cross_producty=(a1*c2-a2*c1)
    cross_productz=(a1*b2-a2*b1) 
    if st.button("Submit"):
        st.write(f"The value of the Cross product of two Vectors is {cross_productx}x - {cross_producty}y + {cross_productz}z")
    else:
        st.write("Please click on submit button")   