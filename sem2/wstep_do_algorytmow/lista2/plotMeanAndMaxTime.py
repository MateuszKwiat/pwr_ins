import imports as im
import plotly.graph_objects as go
import meanAndMaxTime


def plotMeanAndMaxTime():
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    timeOfBubbleSorts = [0]*10
    timeOfInsertionSorts = [0]*10
    timeOfSelectionSorts = [0]*10

    bubbleSortResults = [0]*len(sizes)
    insertionSortResults = [0]*len(sizes)
    selectionSortResults = [0]*len(sizes)

    maxValuesBubbleSort = [0]*len(sizes)
    maxValuesInsertionSort = [0]*len(sizes)
    maxValuesSelectionSort = [0]*len(sizes)
    
    for i in range(0, len(sizes)):
        arr = [0]*sizes[i]
        timeOfBubbleSorts, timeOfInsertionSorts, timeOfSelectionSorts = meanAndMaxTime.meanAndMaxTime(arr, sizes[i], False)
        bubbleSortResults[i] = im.mean(timeOfBubbleSorts)
        insertionSortResults[i] = im.mean(timeOfInsertionSorts)
        selectionSortResults[i] = im.mean(timeOfSelectionSorts)

        maxValuesBubbleSort[i] = max(timeOfBubbleSorts)
        maxValuesInsertionSort[i] = max(timeOfInsertionSorts)
        maxValuesSelectionSort[i] = max(timeOfSelectionSorts)

    fig = go.Figure()
    # bubble sort plot
    fig.add_trace(go.Scatter(x=sizes, y=bubbleSortResults, mode='lines', 
                            name='Bubble sort mean time', line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=sizes, y=maxValuesBubbleSort, mode='markers',
                            name='Bubble sort max time', line=dict(color='blue', width=6)))

    # insertiob sort plot
    fig.add_trace(go.Scatter(x=sizes, y=insertionSortResults, mode='lines',
                            name='Insertion sort mean time', line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=sizes, y=maxValuesInsertionSort, mode='markers', 
                            name='Insertion sort max time', line=dict(color='red', width=6)))

    # selection sort
    fig.add_trace(go.Scatter(x=sizes, y=selectionSortResults, mode='lines',
                            name='Selection sort mean time', line=dict(color='green', width=4)))
    fig.add_trace(go.Scatter(x=sizes, y=maxValuesSelectionSort, mode='markers', 
                            name='Selection sort max time', line=dict(color='green', width=6)))

    fig.update_layout(title='Mean and max times of sorting algorithms', 
                      xaxis_title='number of elements',
                      yaxis_title='time in seconds')
    fig.show()