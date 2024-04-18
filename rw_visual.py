import matplotlib.pyplot as plt
from random_walk import RandomWalk


# построение случайного блуждания
rw = RandomWalk()
rw.fill_walk()

# нанесение точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.YlOrBr,
           s=10, edgecolors='none')
# выделение первой и последней точек
ax.scatter(0, 0, c='green', s=80)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='black', s=80)
# удаление осей
#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)

plt.show()

# продолжение построения графиков
'''
keep_running = input('Make another walk? (y/n): ')
if keep_running == 'n':
    break
'''