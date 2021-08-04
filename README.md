# python-multiprocessing-sample
Basic python multiprocessing using calculator app.

# Installation
Just install python, nothing else

# Working

All the calculation functions are running on different processes.

**result**: This variable has been shared between all the processes in order to get the outputs from all the functions and access it in the parent function.

# Result

```python
{'subtract': -1, 'add': 3, 'divide': 0.5, 'multiply': 2}
{'subtract': -1, 'add': 7, 'divide': 0.75, 'multiply': 12}
{'subtract': -1, 'add': 11, 'divide': 0.8333333333333334, 'multiply': 30}
```

