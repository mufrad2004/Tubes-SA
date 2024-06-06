import tkinter as tk
from tkinter import ttk
from itertools import permutations
import sys

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    num_points = len(permutation)
    for i in range(num_points):
        total_distance += distance_matrix[permutation[i]][permutation[(i + 1) % num_points]]
    return total_distance

def tsp_exhaustive_search(distance_matrix):
    num_points = len(distance_matrix)
    all_permutations = permutations(range(num_points))
    min_distance = sys.maxsize
    best_permutation = None
    all_results = []

    for permutation in all_permutations:
        current_distance = calculate_total_distance(permutation, distance_matrix)
        all_results.append((permutation, current_distance))
        if current_distance < min_distance:
            min_distance = current_distance
            best_permutation = permutation

    return best_permutation, min_distance, all_results

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Exhaustive Search")
        
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
        
        best_permutation, min_distance, all_results = tsp_exhaustive_search(distance_matrix)
        
        self.result_label.config(text=f"Titik Terbaik: {best_permutation}\nJarak Terkecil: {min_distance}")
        
        self.results_text.delete("1.0", tk.END)
        for permutation, distance in all_results:
            self.results_text.insert(tk.END, f"Urutan: {permutation}, Jarak: {distance}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
