import tkinter as tk
from tkinter import messagebox
from prediction import predict_score
import matplotlib.pyplot as plt


def plot_prediction(predicted_score, current_runs, total_balls):
    plt.figure(figsize=(6, 4))
    plt.plot(['Current', 'Predicted'], [current_runs, predicted_score], marker='o', linestyle='-', color='blue')
    plt.title(f'Current Runs: {current_runs} | Balls: {total_balls} | Predicted Score: {predicted_score:.2f}')
    plt.ylabel('Runs')
    plt.xlabel('Score Type')
    plt.ylim(0, max(current_runs, predicted_score) + 50)  # Adjust y-axis for better visibility
    plt.grid()
    plt.show()


def on_predict():
    try:
        current_runs = int(current_runs_entry.get())
        current_overs = float(current_overs_entry.get())

        # Convert overs to total balls
        total_balls = int(current_overs) * 6 + round((current_overs - int(current_overs)) * 6)

        # Predict the score using total balls
        predicted_score = predict_score(current_runs, current_overs)

        # Display the prediction in a message box
        messagebox.showinfo("Prediction", f"Predicted total runs: {predicted_score:.2f}")

        # Plot the prediction
        plot_prediction(predicted_score, current_runs, total_balls)
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

# Run the application
root.mainloop()
