# -*- coding: utf-8 -*- 
graph = {}       ������ϵ�ֵ�
graph["����"] = {}
graph["����"]["����"] = 5
graph["����"]["�ڽ�"] = 0
graph["����"] = {}
graph["����"]["����"] = 30
graph["����"]["���ӹ�"] = 35
graph["�ڽ�"] = {}
graph["�ڽ�"]["����"] = 15
graph["�ڽ�"]["���ӹ�"] = 20
graph["����"] = {}
graph["����"]["����"] = 20
graph["���ӹ�"] = {}
graph["���ӹ�"]["����"] = 10
graph["����"] = {}
#print(graph)
infinity = float("inf")
costs = {}       �ڵ�Ȩֵ�ֵ�
costs["����"] = 5
costs["�ڽ�"] = 0
costs["����"] = infinity
costs["���ӹ�"] = infinity
costs["����"] = infinity
parents = {}       #���׽ڵ��ֵ�
parents["����"] = "����"
parents["�ڽ�"] = "����"
parents["����"] = None
parents["���ӹ�"] = None
parents["����"] = None
processed = []      ��list����ѷ��ʵĽڵ�
def find_lowest_cost_node(costs):   �ڵ㴦����
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node
	node = find_lowest_cost_node(costs)

while node is not None:     ����û�б����ʹ��Ľڵ�
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

#print (parents)

key = "����"
L = ["����"]
while True:				#ת��Ϊlist���� Ȼ�������
	key = parents[key]
	L.append(key)
	if key == "����":
		break
i = -1
print ("·��Ϊ��",end='')
for x in L:
	print (L[i],end='')
	if L[i] != "����":
		print ("-->",end='')
	i = i-1