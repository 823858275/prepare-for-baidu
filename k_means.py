from collections import defaultdict
from random import uniform
from math import sqrt
def generate_k(data_set,k):
    centers=[]
    dimensions=len(data_set[0])
    min_max=defaultdict(int)
    for point in data_set:
        for i in range(dimensions):
            val=point[i]
            min_key="min_"+str(i)
            max_key="max_"+str(i)
            if min_key not in min_max or val<min_max[min_key]:
                min_max[min_key]=val
            if max_key not in min_max or val>min_max[max_key]:
                min_max[max_key]=val
    for i in range(k):
        rand_point=[]
        for j in range(dimensions):
            min_val=dimensions["min_"+str(j)]
            max_val=dimensions["max_"+str(j)]
            rand_point.append(uniform(min_val,max_val))
        centers.append(rand_point)
    return centers
def distance(a,b):
    dimensions=len(a)
    _sum=0
    for dimension in range(dimensions):
        difference=(a[dimension]-b[dimension])**2
        _sum+=difference
    return sqrt(_sum)
def assign_points(data_points,centers):
    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments
def update_centers(data_set,assignments):
    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)

    for points in new_means.itervalues():
        centers.append(point_avg(points))
    return centers
def point_avg(points):
    dimensions = len(points[0])

    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0
        for p in points:
            dim_sum += p[dimension]
        new_center.append(dim_sum / float(len(points)))
    return new_center


def k_means(dataset,k):
    k_points=generate_k(dataset,k)#随机生成k个簇的中心点
    assignments = assign_points(dataset, k_points) #确定每个点属于哪个簇
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)#求每个簇的均值作为新的中心点
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    return zip(assignments, dataset)