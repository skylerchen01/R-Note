## Working with vectors

# Creating vectors
x <- c(1, 2, 3, 4, 5)
y <- 2:6
z <- seq(1, 3, by = 0.5) # step size

# Properties
typeof(x)
length(x)
y
z

# Addition
sum <- x + y
print(sum)

# Multiplication
product <- x * y
print(product)

# Squaring
squared_x <- x^2
squared_y <- y^2
print(squared_x)
print(squared_y)

# Access first element
y[1]    
y
# Access the first and 3rd elements
y[c(1, 3)]   
y
# Access all but 3rd element
y[-3]  
y
# Add a new element
y <- c(y, 7)
y
# Change the second element
y[2] <- 10
y
# Remove the fourth element
y <- y[-4]
y

# Initialize an empty numeric vector to store squared values
squared_values <- numeric(length(x))

# Loop through the original vector
for (i in seq_along(x)) {
  squared_values[i] <- vector1[i]^2
}

print(squared_values)
