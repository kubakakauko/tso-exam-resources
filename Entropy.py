import math

p_yes = float(input("Enter p(yes): "))
p_no = float(input("Enter p(no): "))

n = p_yes + p_no


f_yes = p_yes / n
f_no  = p_no  / n

# Calculate the entropy
entropy = -(f_yes) * math.log2(f_yes) - (f_no) * math.log2(f_no)


# Display the results
print("Entropy: ", entropy)
