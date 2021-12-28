from tkinter import *
from tkinter import simpledialog

from src import DiGraph
from src import GraphAlgo

program = Tk()
program.title("Graphs")
program.geometry("700x700")

graph = DiGraph.DiGraph()
Graph = GraphAlgo.GraphAlgo(graph)


def draw_graph():
    Graph.plot_graph()


def saved():
    file_input = simpledialog.askstring(title="file",
                                        prompt="enter a file name:  (the file will appear/update after closing the program)")
    Graph.save_to_json(file_input)


def loaded():
    file_input = simpledialog.askstring(title="file", prompt="enter a file name or path:")
    Graph.load_from_json(file_input)


def disconnect():
    src_input = simpledialog.askinteger(title="src", prompt="enter the key of the src node:")
    dest_input = simpledialog.askinteger(title="dest", prompt="enter the key of the dest node")

    Graph.get_graph().remove_edge(src_input, dest_input)


def connect():
    src_input = simpledialog.askinteger(title="src", prompt="enter the key of the src node:")
    dest_input = simpledialog.askinteger(title="dest", prompt="enter the key of the dest node")
    w_input = simpledialog.askfloat(title="w", prompt="enter the weight of the edge")

    Graph.get_graph().add_edge(src_input, dest_input, w_input)


def remove():
    node_input = simpledialog.askinteger(title="node", prompt="enter the key of the desired node to be removed:")
    Graph.get_graph().remove_node(node_input)


def add():
    key_input = simpledialog.askinteger(title="key", prompt="enter the node's key: ")
    X_input = simpledialog.askstring(title="x", prompt="enter the x value of the pos: ")
    Y_input = simpledialog.askstring(title="y", prompt="enter the y value of the pos: ")
    pos = X_input + "," + Y_input + "," + "0.0"
    Graph.get_graph().add_node(key_input, pos)


my_menu = Menu(program)
program.config(menu=my_menu)

# file
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=saved)
file_menu.add_command(label="Load", command=loaded)
file_menu.add_separator()
file_menu.add_command(label="Draw a graph", command=draw_graph)

# edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Disconnect nodes", command=disconnect)
edit_menu.add_command(label="Connect nodes", command=connect)
edit_menu.add_command(label="Remove a node", command=remove)
edit_menu.add_command(label="Add a node", command=add)

program.mainloop()
