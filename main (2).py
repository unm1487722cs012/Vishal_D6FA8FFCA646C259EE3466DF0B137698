#write a function called linear search_products that takes the list of products and a target product name as input.the function should perform a linear search to find the target product in the list and return a list of indices of all occurence of the product if found.or an empty list if the product is not found
def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index, product in enumerate (productlist):
    if product==targetproduct:
      indices.append(index)
  return indices
product=["shoes","boot ","boot","shoes ","sandals"]
target="shoes "
target2="bag"
result=linearsearchproduct(product, target2)
print (result)