import tkinter as tk
from tkinter import messagebox
from prediction import predict_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_prediction(predicted_score, current_runs, total_balls):
    # Create a new figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(['Current', 'Predicted'], [current_runs, predicted_score], marker='o', linestyle='-', color='blue')
    ax.set_title(f'Current Runs: {current_runs} | Balls: {total_balls} | Predicted Score: {predicted_score:.2f}')
    ax.set_ylabel('Runs')
    ax.set_xlabel('Score Type')
    ax.set_ylim(0, max(current_runs, predicted_score) + 50)  # Adjust y-axis for better visibility
    ax.grid()

    return fig


def on_predict():
    try:
        current_runs = int(current_runs_entry.get())
        current_overs = float(current_overs_entry.get())

        # Convert overs to total balls
        total_balls = int(current_overs) * 6 + round((current_overs - int(current_overs)) * 6)

        # Predict the score using total balls
        predicted_score = predict_score(current_runs, current_overs)

        # Display the prediction in the label
        prediction_label.config(text=f"Predicted total runs: {predicted_score:.2f}")

        # Plot the prediction
        fig = plot_prediction(predicted_score, current_runs, total_balls)

        # Clear the previous plot if it exists
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Embed the plot in the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values for runs and overs.")


# Create the main application window
root = tk.Tk()
root.title("Cricket Score Predictor")

# Create and place the input labels and entries
tk.Label(root, text="Current Runs:").grid(row=0, column=0, padx=10, pady=5)
current_runs_entry = tk.Entry(root)
current_runs_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Current Overs:").grid(row=1, column=0, padx=10, pady=5)
current_overs_entry = tk.Entry(root)
current_overs_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place the predict button
predict_button = tk.Button(root, text="Predict Score", command=on_predict)
predict_button.grid(row=2, columnspan=2, pady=10)

# Label to display prediction
prediction_label = tk.Label(root, text="", font=("Arial", 14))
prediction_label.grid(row=3, columnspan=2, pady=10)

# Frame to hold the plot
plot_frame = tk.Frame(root)
plot_frame.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
