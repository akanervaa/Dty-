import pyomo.environ as pyomo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import myData
from matplotlib.animation import FuncAnimation
def plot(max_dV, P_max, V_max,image_paths,i, model, PowerCosts, time_steps, V0, V_values, P_values, dV_values, Power_color, Discharge_color, Charge_color, number, previous_storage = 24*[0], prev_storage_color = 'black', cost_value_scen='min'):
    flows = []
    for i in previous_storage:
        x = i*myData.alfa
        flows.append(x)
    if cost_value_scen > 0:
        # Find the index with the highest penalty cost
        penalty_index = max(PowerCosts, key=PowerCosts.get)
        Limit = 'max'
    else:
        penalty_index = min(PowerCosts, key=PowerCosts.get)
        Limit = 'min'
    # Define colors for P1, and V1
    colors = [Power_color, Discharge_color, Charge_color]
    			 
    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 6),dpi=300)
    			 
    # Create bar positions
    bar_positions = np.arange(len(time_steps))
    			 
    # Define the width of each bar
    bar_width = 0.7
    			 
    # Calculate the x-coordinates for previous storage flow
    x = bar_positions
    			 
     			 
    # Create bars for P
    p1_bar = ax.bar(x, P_values, width=bar_width, color=Power_color, label='Dissolved oxygen generated and consumed in zone '+number+' by aerators to satisfy the quality requirements')			 
    # Calculate the starting position for green bars (negative dV values) at P_values
    neg_dv_y = P_values
    # Create bars for negative dV values (green)
    neg_dv_values = [max(val, 0) for val in dV_values]
    dv_bar_neg = ax.bar(x, neg_dv_values, width=bar_width, color=Discharge_color, label='Stored dissolved oxygen consumed in zone '+number+' to satisfy the demand', bottom=neg_dv_y)
    			 
    # Calculate the starting position for light blue bars (positive dV values)
    pos_dv_y = [x + y for x, y in zip(P_values, neg_dv_values)]
    			 
    # Create bars for positive dV values (light blue)
    pos_dv_values = [min(val, 0) for val in dV_values]
    dv_bar_pos = ax.bar(x, pos_dv_values, width=bar_width, color=Charge_color, label='Dissolved oxygen generated in zone '+number, bottom= pos_dv_y)
    # Calculate the starting position for purple bars at P_values
    flow_y = [x + y for x, y in zip(P_values, pos_dv_y)]
    # Create bars for flow from previous storage
    #flow_bar = ax.bar(x, flows, width=bar_width, color=prev_storage_color, label='Material flow from previous storage',bottom=P_values)
    
    # Create a line plot for V values and V0
    # Add V0 at time step -1
    x_with_v0 =  list(x)
    V_values_with_v0 = V_values
    			 
    ax.plot(x_with_v0, V_values_with_v0, marker='o', linestyle='-', color='black', label='Amount of dissolved oxygen (DO) at the end of the step')
    			 
    # Set the labels and title
    ax.set_xlabel('Time Steps')
    ax.set_ylabel('Powers (kWh)')
    ax.set_title('Dissolved oxygen storage behavior in zone '+number)
    			 
    # Set the x-axis ticks and labels
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(time_steps)
    			 
    # Plot the demand curve as a plain black line
    #ax.plot(x, demand_values, linestyle='--', color='black', label='Demand d(t)')
    			 
    # Create a legend
    ax.legend()
    			 
    # Set the y-axis limits
    y_min = 0
    y_max = 2.5
    ax.set_ylim(y_min, y_max)
    # Add text for the max penalty cost
    penalty_text = Limit+f' cost at t={penalty_index}'
    			 
    # Create a text box in the northwest corner of the plot
    ax.annotate(penalty_text, xy=(0, 0.8), xycoords='axes fraction', fontsize=14,
    xytext=(20, -20), textcoords='offset points',
    bbox=dict(boxstyle="square,pad=0.3", edgecolor="black", facecolor="white"))
    			 
    # Calculate the total cost from the model's objective function
    total_cost = model.objective()
    			 
    # Create a text box with the information
    info_text = f"Max Negative dV: {max_dV:.2f}\nMax Positive dV: {max_dV:.2f}\nMax P1: {P_max:.2f}\nMax V: {V_max:.2f}\nTotal Cost: {total_cost:.2f}"
    			 
    # Add the text box to the plot
    ax.text(0.768, 0.56, info_text, transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle="square,pad=0.5", facecolor="white", alpha=0.7))
    
    # Save the plot as a PNG image
    image_path = f'plots/plot_{i}MAX'+number+'.png'
    plt.savefig(image_path, dpi=300)  # Save the plot as a PNG image
    image_paths.append(image_path)  # Store the path to the image
 
    plt.show()
    '''
    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.axis('off')  # Turn off the axis
    ax.set_title('')  # Clear the frame title
    '''

    
