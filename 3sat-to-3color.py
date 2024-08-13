#reducao 3sat para 3coloracao
def sat3_to_3color(sat3):
    graph = {}
    variablesSat3 = readVariables3sat(sat3)

    addVertex(graph, ('B', 'Blue'))
    addVertex(graph, ('R', 'Red'))
    addVertex(graph, ('G', 'Green'))

    addEdge(graph, ('B', 'Blue'), ('R', 'Red'))
    addEdge(graph, ('B', 'Blue'), ('G', 'Green'))
    addEdge(graph, ('R', 'Red'), ('G', 'Green'))

    for element in variablesSat3:

        addVertex(graph, (element, 'Sem cor'))
        addVertex(graph, ('!'+element, 'Sem cor'))

        addEdge(graph, (element, 'Sem cor'), ('!'+element, 'Sem cor'))
        addEdge(graph, (element, 'Sem cor'), ('B', 'Blue'))
        addEdge(graph, ('!'+element, 'Sem cor'), ('B', 'Blue'))


    for i in range(len(sat3)):

        addVertex(graph, ('A'+str(i), 'Sem cor'))
        addVertex(graph, ('B'+str(i), 'Sem cor'))
        addVertex(graph, ('C'+str(i), 'Sem cor'))
        addVertex(graph, ('D'+str(i), 'Sem cor'))
        addVertex(graph, ('E'+str(i), 'Sem cor'))
        addVertex(graph, ('F'+str(i), 'Sem cor'))

        addEdge(graph, ('A'+str(i), 'Sem cor'), ('G', 'Green'))
        addEdge(graph, ('B'+str(i), 'Sem cor'), ('G', 'Green'))
        addEdge(graph, ('C'+str(i), 'Sem cor'), ('G', 'Green'))
        addEdge(graph, ('D'+str(i), 'Sem cor'), ('G', 'Green'))
        addEdge(graph, ('F'+str(i), 'Sem cor'), ('R','Red'))
        addEdge(graph, ('E'+str(i), 'Sem cor'), ('D'+str(i), 'Sem cor'))
        addEdge(graph, ('E'+str(i), 'Sem cor'), ('F'+str(i), 'Sem cor'))
        addEdge(graph, ('E'+str(i), 'Sem cor'), ('B'+str(i), 'Sem cor'))
        addEdge(graph, ('D'+str(i), 'Sem cor'), ('A'+str(i), 'Sem cor'))
        addEdge(graph, ('C'+str(i), 'Sem cor'), ('F'+str(i), 'Sem cor'))
        addEdge(graph, (sat3[i][0], 'Sem cor'), ('A'+str(i), 'Sem cor'))
        addEdge(graph, (sat3[i][1], 'Sem cor'), ('B'+str(i), 'Sem cor'))
        addEdge(graph, (sat3[i][2], 'Sem cor'), ('C'+str(i), 'Sem cor'))

    return graph

#adiciona vertice no grafo
def addVertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []

#adiciona aresta no grafo
def addEdge(graph, vertex1, vertex2):
    if vertex1 in graph and vertex2 in graph:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
        
#leitura de todas variaveis do problema
def readVariables3sat(sat3):
    varInSat3 = []
    for i in range(len(sat3)):
        for j in range(len(sat3[i])):
            if sat3[i][j][0] == '!' and sat3[i][j][1:] not in varInSat3:
                varInSat3.append(sat3[i][j][1:])
            elif sat3[i][j][0] != '!' and sat3[i][j] not in varInSat3 :
                varInSat3.append(sat3[i][j])
    return varInSat3

#certificado
def checkColoring(graph):
    for vertex in graph:
        for neighbor in graph[vertex]:
            if vertex[0] == neighbor[0] and vertex[1] == neighbor[1]:
                return False
    return True


def main():

    sat3 = [['x1', 'x4', '!x3'],[ 'x5', 'x3', 'x4'],['!x5', 'x2', 'x3']]
    print(sat3_to_3color(sat3))

if __name__ == "__main__":
    main()



