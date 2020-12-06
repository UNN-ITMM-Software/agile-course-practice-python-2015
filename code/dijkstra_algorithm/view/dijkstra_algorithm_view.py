import tkinter as tk

from dijkstra_algorithm.viewmodel.dijkstra_algorithm_viewmodel import DAViewModel


class GUIView:
    view_model = DAViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#fafafa'
        self.root.title('Алгоритм Дейкстры')
        self.root.geometry('630x400')
        # self.root.resizable(width=False, height=True)

        self.frame = tk.Frame(self.root, bg='#fafafa')
        self.result_frame = tk.Frame(self.root, bg='#fafafa')
        self.lbl_num_vertex = tk.Label(self.root, text="Введите число вершин графа:")
        self.input_num_vertex = tk.Entry(self.root)
        self.input_graph = tk.Button(self.root, text="Задать граф", state='disabled')
        self.lbl_start_vertex = tk.Label(self.root, text="Введите стартовую вершину алгоритма:")
        self.input_start_vertex = tk.Entry(self.root)
        self.run = tk.Button(self.root, text="Запустить алгоритм")
        self.entries = []
        self.result = []

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.lbl_num_vertex.grid(row=0, column=0)
        self.input_num_vertex.grid(row=0, column=1)
        self.input_graph.grid(row=0, column=2)
        self.lbl_start_vertex.grid(row=1, column=0)
        self.input_start_vertex.grid(row=1, column=1)
        self.run.grid(row=1, column=2)
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.result_frame.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

    def bind_events(self):
        self.input_num_vertex.bind('<KeyRelease>', self.num_vertex_changed)
        self.input_start_vertex.bind('<KeyRelease>', self.start_vertex_changes)
        self.input_graph.bind('<Button-1>', self.input_graph_clicked)
        self.run.bind('<Button-1>', self.run_clicked)

    def num_vertex_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def start_vertex_changes(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def input_graph_clicked(self, event):
        self.mvvm_bind()
        self.draw_table()
        self.mvvm_back_bind()

    def run_clicked(self, event):
        self.mvvm_bind()
        self.draw_result(self.view_model.run_dijkstra(self.read_weights()))
        self.mvvm_back_bind()

    def draw_table(self):

        if self.view_model.get_btn_create_graph_state() == 'disabled':
            return

        self.frame.destroy()
        self.frame = self.frame = tk.Frame(self.root, bg='#fafafa')
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.entries = []

        rows = int(self.input_num_vertex.get())
        cols = int(self.input_num_vertex.get())
        for i in range(rows):
            self.entries.append([])
            for j in range(cols):
                self.entries[i].append(tk.Entry(self.frame, width=3))
                self.entries[i][j].grid(row=i, column=j)

    def draw_result(self, result):

        self.result_frame.destroy()
        self.result_frame = tk.Frame(self.root, bg='#fafafa')
        self.result_frame.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)
        self.result = []

        lbl_result = tk.Label(self.result_frame, text="Кратчайшие пути до всех вершин:")
        lbl_result.grid(row=0, column=0)

        for j, dist in enumerate(result):
            self.result.append(tk.Label(self.result_frame, text=str(dist)))
            self.result[-1].grid(row=0, column=j + 1)

    def read_weights(self):
        rows = int(self.input_num_vertex.get())
        cols = int(self.input_num_vertex.get())
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(self.entries[i][j].get())

        return matrix

    def mvvm_bind(self):
        self.view_model.set_num_vertex(self.input_num_vertex.get())
        self.view_model.set_start_vertex(self.input_start_vertex.get())

    def mvvm_back_bind(self):
        self.input_num_vertex.delete(0, tk.END)
        self.input_num_vertex.insert(tk.END, self.view_model.get_num_vertex())

        self.input_graph.config(state=self.view_model.get_btn_create_graph_state())

        self.input_start_vertex.delete(0, tk.END)
        self.input_start_vertex.insert(tk.END, self.view_model.get_start_vertex())