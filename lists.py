# append(), insert e extend()
# pop() e reverse() e remove()
# sort() e sorted()
# min(), max() e sum()
# enumarate() e index()
# join() e split()

strings = ['cafe', 'chocolate', 'pão', 'leite', 'manteiga']

nums = [100, 236, 700, 33, 90, 8768]

precos = [3.00,4.95, 50.70, 200.99, 97.05, 1.09 ]

# Usar o append para adicionar um item a lista
strings.append('requeijão')
strings.insert(0, 'Café Da Manhã:')
popped_string = strings.pop()
sorted_strings = sorted(strings)
print(popped_string)
print(sorted_strings)

nums.append(346)
nums.insert(0, 800)
nums.remove(800)
popped = nums.pop()
nums.extend(precos)
sorted_nums = sorted(nums)

for i,index in enumerate(nums):
    print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print(popped)
print(sorted_nums)

# Usar o enumemarate e index para numerar os itens

# Usar o join e o split para manipular strings

