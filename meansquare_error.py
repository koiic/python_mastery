# calculate the mean square error between two list of numbers

predictions = [10, 20, 30]
actual_lists = [12,18,35]

def mean_square_error(pred, actual):
    
    square_err = [(pred[i] - actual[i]) **2 for i in range(len(pred))]
    return sum(square_err) / len(square_err)

print(mean_square_error(predictions, actual_lists))
    

def efficient_mean_square(pred, actual):
    square_err = [(one_pred - one_actual) **2 for one_pred, one_actual in zip(pred, actual_lists)]
    return sum(square_err) / len(square_err)

print(efficient_mean_square(predictions, actual_lists))