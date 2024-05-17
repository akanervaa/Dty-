import matplotlib.pyplot as plt
import myData
def flex_index(max_potential, min_potential, duration):
    # Define the values for the intervals
    intervals = []
    for i in range(len(max_potential)):
        intervals.append((min_potential[i],max_potential[i]))
    'print(intervals)'
    # Create x-axis values centered at 0
    x_values = list(range(len(myData.Time)))
    
    # Create a list of colors for the bars (green for the negative part, lightblue for the positive part)
    bar_colors = ['green' if start < 0 else 'green' for start, end in intervals]
    
    # Extract the start and end values for the bars
    starts, ends = zip(*intervals)
    heights = []
    for t in range(len(intervals)):
        heights.append(abs(starts[t])+abs(ends[t]))
    # Calculate the y-axis limits
    y_min = min(starts)
    y_max = max(ends)
    y_range = max(abs(y_min), abs(y_max))
    
    # Create the bar chart with bars representing the full range between values
    plt.figure(figsize=(15, 10), dpi=300)  # Set the chart's size and DPI
    plt.bar(x_values, heights, bottom=starts, color=bar_colors, align='edge', width=0.7, label='Energy flexibility available in '+duration)
    # Set the x-axis ticks at the center of the bars and label them as time steps
    plt.xticks(x_values, [f'{i}' for i in x_values], rotation=0, ha='center')
    
    # Set the y-axis limits
    plt.ylim(y_min - 2, y_max + 2)
    
    # Add a dotted line at zero value
    plt.axhline(0, color='black', linestyle='--', label='Zero Value')
    
    # Set the title and axis labels
    plt.title('Energy flexibility of aeration in WWTP')
    plt.xlabel('Time Step / [h]')
    plt.ylabel('Difference in total Aeration Energy Consumption compared to normal scenario / ($\mathrm{kWh}$)')
    
    # Show the legend
    plt.legend()
    
    # Save the chart with at least 300 DPI
    plt.savefig('flexibilityIndexStorage.png', dpi=300)
    
    # Show the chart
    plt.show()
