import tkinter as tk
from itertools import combinations

def tsp_dynamic_programming(distance_matrix):
    n = len(distance_matrix)
    all_sets = []
    g = {}
    p = {}

    for x in range(1, n):
        g[x + 1, ()] = distance_matrix[x][0]

    def get_minimum(k, a):
        if (k, a) in g:
            return g[k, a]
        
        values = []
        all_min = []
        for j in a:
            set_a = list(a)
            set_a.remove(j)
            all_min.append([distance_matrix[k - 1][j - 1] + get_minimum(j, tuple(set_a)), j])

        g[k, a] = min(all_min)[0]
        p[k, a] = min(all_min)[1]

        return g[k, a]

    for x in range(1, n):
        all_sets.append(x + 1)

    min_cost = get_minimum(1, tuple(all_sets))
    optimal_path = []

    def get_optimal_path(start, a):
        if len(a) == 0:
            return
        optimal_path.append((start, a))
        new_start = p[start, a]
        set_a = list(a)
        set_a.remove(new_start)
        get_optimal_path(new_start, tuple(set_a))

    get_optimal_path(1, tuple(all_sets))

    optimal_path_final = [1]
    for x in optimal_path:
        optimal_path_final.append(p[x])
    optimal_path_final.append(1)

    return optimal_path_final, min_cost, g, p

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Dynamic Programming")
        
        self.label = tk.Label(root, text="Masukkan Matrix Jarak (pisahkan dengan koma, baris baru dengan enter):")
        self.label.pack()
        
        self.text = tk.Text(root, height=10, width=50)
        self.text.pack()
        
        self.button = tk.Button(root, text="Hitung TSP", command=self.calculate_tsp)
        self.button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.results_text = tk.Text(root, height=10, width=50)
        self.results_text.pack()
    
    def calculate_tsp(self):
        input_data = self.text.get("1.0", tk.END).strip()
        distance_matrix = []
        
        for line in input_data.split("\n"):
            distance_matrix.append(list(map(int, line.split(","))))
        
        optimal_path, min_cost, g, p = tsp_dynamic_programming(distance_matrix)
        
        self.result_label.config(text=f"Rute Terbaik: {optimal_path}\nJarak Terkecil: {min_cost}")
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "Langkah-langkah Dynamic Programming:\n\n")
        
        self.results_text.insert(tk.END, "g (biaya minimum):\n")
        for key, value in g.items():
            self.results_text.insert(tk.END, f"g{key} = {value}\n")
        
        self.results_text.insert(tk.END, "\np (langkah optimal):\n")
        for key, value in p.items():
            self.results_text.insert(tk.END, f"p{key} = {value}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
