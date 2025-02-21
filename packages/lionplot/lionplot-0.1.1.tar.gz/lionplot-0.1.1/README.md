# Lionplot Package

This is a simple package to create a lionplot. A lionplot is a categorical scatterplot with errorbars.
Consider that you have three categories (independent variables), e.g., "orange", "blue" and "green", and two groups, "A" and "B", and a dependent variable, e.g., "y". You can use this plot to compare the means of the dependent variable between the two groups, for each category.

<!-- include local image -->
![Lionplot](imgs/example.pdf)

## Usage
Assume you have the following arrays
```python
print(x)
>> ['blue', 'green', 'orange', 'blue', 'green', 'orange']
print(y)
>> [11.00385443,  9.48885355,  9.34449002, 16.19138262, 16.06753942, 16.89107449]
print(yerr)
>> [0.9982947 , 1.0022813 , 0.99986582, 0.99908995, 0.99837166, 0.99931396]
print(group)
>> ['A', 'A', 'A', 'B', 'B', 'B']
```
where `x` is the category, `y` is the average, `yerr` is the confidence interval (95\%) and group is the group assignment. You can create a lionplot as follows:

```python
from lionplot import lionplot

lionplot(
    x=x,
    y=y,
    ax=ax,
    yerr=yerr,
    hue_values=group,
)
```

@2025, Leonardo Alchieri
