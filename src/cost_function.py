def calculate_cost(y_true, y_pred):

    fraud_loss = 1000

    false_alarm_cost = 50

    total_cost = 0

    for i in range(len(y_true)):

        # Missed fraud
        if y_true[i] == 1 and y_pred[i] == 0:

            total_cost += fraud_loss

        # False alarm
        elif y_true[i] == 0 and y_pred[i] == 1:

            total_cost += false_alarm_cost

    return total_cost