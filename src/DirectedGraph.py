from src import GraphInterface
from src import NodeData
from src import EdgeData
class DirectedGraph(GraphInterface):
    # this dictionary will keep data in this format , id: Node object
    graph:dict[int:NodeData]={}
    def DirectedGraph(self, graphNew):
        self.graph:dict[int:NodeData]=graphNew.graph
        self.nodeCount:int=graphNew.nodeCount
        self.edgeCount:int=graphNew.edgeCount
        self.MC:int=graphNew.MC
    def getNode(self,id:int)->NodeData:
        return self.graph.get(id)
    def v_size(self)-> int:
        return self.nodeCount
    def e_size(self)->int:
        return self.edgeCount
    def get_all_v(self)-> dict:
        return self.graph
    def all_in_edges_of_node(self, id1: int) -> dict:
        return 0
    def all_out_edges_of_node(self, id1: int) -> dict:
        return 0
    def get_mc(self) -> int:
        return self.MC
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:#so this is like the function connect
        node:NodeData=self.graph.get(id1)
        if node.get(id2)==None or self.graph.get(id1)==None or self.graph.get(id2)==None:
            return False
        else:
            node[id2]= EdgeData(id1,id2,weight)
            self.edgeCount += 1
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.graph.get(node_id)==None:
            return False
        else:
            if pos==None:
              #Ask what to do in this case!!!!
             return False
            else:
             self.graph[node_id]=NodeData(pos[0],pos[1],pos[2],node_id)
             self.nodeCount+=1
             return True
    def remove_node(self, node_id: int) -> bool:
        if self.graph.get(node_id)==None:#node doesn't exist
            return False
        else:
            node: NodeData = self.graph.get(node_id)
            self.edgeCount-=len(node.Node)
            node.Node.clear()
            self.graph.pop(node_id)
            self.nodeCount-=1
            return True
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.graph.get(node_id1)==None or self.graph.get(node_id2)==None:
            return False
        else:
            node:NodeData=self.graph.get(node_id1)
            node.Node.pop(node_id2);
            self.edgeCount-=1
            return True

