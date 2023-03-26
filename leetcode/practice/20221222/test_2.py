"""
완제품이 무엇인지 찾아야함

각 노드번호 별 재료비, 인건비를 구해야함

"""

cost_per_node = dict()


def solution(n, costs, edges):
    complete_product_node = get_complete_product_node(n, edges)

    cost_of_materials_and_personnel_expenses_per_node_number = get_cost_per_node(n, costs, edges)

    answer = []
    return answer


def get_cost_per_node(n, costs, edges):
    for i in range(1, n + 1):
        cost_per_node[i] = costs[i - 1]


def test_get_cost_per_node():
    assert get_cost_per_node(n=4, costs=[1, 1, 1, 1], edges=[[4, 3, 2,], [3, 2, 2], [2, 1, 2]]) == {
        "1": (8, 7),
        "2": (4, 3),
        "3": (2, 1),
        "4": (1, 0),
    }


def get_complete_product_node(n, edges):
    temp = {i for i in range(1, n + 1)}

    for edge in edges:
        try:
            temp.remove(edge[0])
        except KeyError:
            pass

    return list(temp)[0]


def test_get_complete_product_node():
    assert get_complete_product_node(4, [[4, 3, 2], [3, 2, 2], [2, 1, 2]]) == 1
    assert get_complete_product_node(4, [[3, 1, 2], [1, 2, 1], [4, 1, 2], [4, 2, 3]]) == 2
