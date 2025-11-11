import matplotlib.pyplot as plt
import numpy as np

def scatter_plot():
    """Create a scatter plot"""
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='red', s=60, alpha=0.7)
    plt.title('Scatter Plot Example')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    plt.show()

def line_plot():
    """Create a line plot"""
    x = np.linspace(0, 10, 50)
    y = x ** 2
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'b-', linewidth=2, marker='o', markersize=4)
    plt.title('Line Plot: y = x²')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    plt.show()

def bar_plot():
    """Create a bar plot"""
    categories = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
    values = [35, 25, 20, 30, 15]
    
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    plt.title('Programming Language Popularity')
    plt.xlabel('Languages')
    plt.ylabel('Popularity (%)')
    plt.xticks(rotation=45)
    plt.show()

def histogram():
    """Create a histogram"""
    data = np.random.normal(100, 15, 1000)  # Normal distribution
    
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, alpha=0.7, edgecolor='black')
    plt.title('Histogram of Normal Distribution')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_basic_functions():
    """Plot basic mathematical functions"""
    x = np.linspace(-10, 10, 100)
    
    plt.figure(figsize=(15, 10))
    
    # Linear function
    plt.subplot(2, 3, 1)
    y_linear = 2*x + 1
    plt.plot(x, y_linear, 'r-', linewidth=2)
    plt.title('Linear: y = 2x + 1')
    plt.grid(True, alpha=0.3)
    
    # Quadratic function
    plt.subplot(2, 3, 2)
    y_quadratic = x**2
    plt.plot(x, y_quadratic, 'g-', linewidth=2)
    plt.title('Quadratic: y = x²')
    plt.grid(True, alpha=0.3)
    
    # Cubic function
    plt.subplot(2, 3, 3)
    y_cubic = x**3
    plt.plot(x, y_cubic, 'b-', linewidth=2)
    plt.title('Cubic: y = x³')
    plt.grid(True, alpha=0.3)
    
    # Sine function
    plt.subplot(2, 3, 4)
    y_sin = np.sin(x)
    plt.plot(x, y_sin, 'orange', linewidth=2)
    plt.title('Sine: y = sin(x)')
    plt.grid(True, alpha=0.3)
    
    # Exponential function
    plt.subplot(2, 3, 5)
    y_exp = np.exp(x/3)
    plt.plot(x, y_exp, 'purple', linewidth=2)
    plt.title('Exponential: y = e^(x/3)')
    plt.grid(True, alpha=0.3)
    
    # Logarithmic function
    plt.subplot(2, 3, 6)
    y_log = np.log(np.abs(x) + 1)
    plt.plot(x, y_log, 'brown', linewidth=2)
    plt.title('Logarithm: y = log(|x| + 1)')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def plot_custom_function():
    """Plot a custom mathematical function"""
    x = np.linspace(-5, 5, 100)
    y = x**3 - 3*x**2 + 2*x + 5  # Custom polynomial
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'red', linewidth=3)
    plt.title('Custom Function: y = x³ - 3x² + 2x + 5')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, alpha=0.3)
    plt.show()

def run_all_basic_plots():
    """Run all basic data plots"""
    print("=== Creating Basic Data Plots ===")
    scatter_plot()
    line_plot()
    bar_plot()
    histogram()

def run_all_function_plots():
    """Run all function plots"""
    print("=== Creating Function Plots ===")
    plot_basic_functions()
    plot_custom_function()

def run_everything():
    """Run all plots"""
    print("=== Creating ALL Plots ===")
    scatter_plot()
    line_plot()
    bar_plot()
    histogram()
    plot_basic_functions()
    plot_custom_function()

# Main execution
if __name__ == "__main__":
    print("Data & Function Visualization")
    print("1. Basic data plots")
    print("2. Function plots") 
    print("3. Everything")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        run_all_basic_plots()
    elif choice == "2":
        run_all_function_plots()
    elif choice == "3":
        run_everything()
    else:
        print("Invalid choice. Running basic plots...")
        run_all_basic_plots()