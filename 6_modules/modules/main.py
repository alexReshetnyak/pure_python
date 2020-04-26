# import shopping.shopping_cart
# import shopping.more_shopping.shopping_cart
from shopping.more_shopping import shopping_cart
from utility import divide


product = shopping_cart.buy("apple")

print("product:", product)
print("divide(6, 3):", divide(6, 3))  # 2

if __name__ == "__main__":
    print("max[1, 2, 3]:", max([1, 2, 3]))  # 3
