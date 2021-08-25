rating = [7, 10, 4, 2, 9]
print(f"rating = {rating}")
rating.sort(reverse=True)
print('Сортированный rating = ', rating)

new_rating = int(input('Введите новое значение ретинга: '))

for i in rating:
    if new_rating > i and new_rating > 0:
        rating.insert((rating.index(i)), new_rating)
        print(rating)
    elif new_rating < i:
        rating.insert(len(rating),new_rating)
        print(rating)
        break
