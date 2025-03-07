import math

def minConnect(sensors11, sensors22, r) :            # tính số lượng Sensors cần thiết để tạo đường kết nối cho 2 vùng sensor11 và sensor22
    sensors1 = copy.deepcopy(sensors11)
    sensors2 = copy.deepcopy(sensors22)
    numSensor = 0
    len_sensor = len(sensors1)
    dis = lambda s1, s2: math.sqrt((s1[0]-s2[0])**2 + (s1[1]-s2[1])**2)
    while(len_sensor > 0) :
        minDis = 1e9
        minIndex = 0
        for i in range(0, len(sensors2)) :
            if dis(sensors1[0], sensors2[i]) < minDis : 
                minDis = dis(sensors1[0], sensors2[i])
                minIndex = i
        sensors1.pop(0)
        sensors2.pop(minIndex)
        len_sensor -= 1
        numSensor += int((minDis-2*r)/(2*r)) + 1
    return numSensor

def calculate_minimum_spanning_tree_length(edges):           # tính số sensors cần cho kết nối toàn vùng nhờ thuật toán Prim

    # Tạo đồ thị
    G = nx.Graph()

    # Thêm các cạnh vào đồ thị
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    # Tìm cây khung nhỏ nhất sử dụng thuật toán Prim
    mst = nx.minimum_spanning_tree(G)
    # Tính tổng trọng số của các cạnh trong cây khung nhỏ nhất
    mst_length = sum(data['weight'] for _, _, data in mst.edges(data=True))

    # In trọng số và các cạnh tương ứng
    return mst_length

