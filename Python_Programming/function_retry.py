import random
import time


def is_status_success():
    print("Checking tha status of the process")
    list_to_chose_form = [True, True, False, False, False, False, False]
    bool_to_return = random.choice(list_to_chose_form)
    return bool_to_return


def retry_with_counter_until_status_is_success(max_retry=10, sleep_time=3):
    is_success = False
    counter = 0
    while counter < max_retry:
        counter += 1
        print("Retry no: {}".format(counter))
        is_success = is_status_success()
        print("The success status is: {}".format(is_success))
        if is_success:
            print("The Process is success")
            break
        else:
            time.sleep(sleep_time)

    if not is_success:
        raise Exception("The format did not succeed after trying for {} seconds.".format(max_retry * sleep_time))


retry_with_counter_until_status_is_success()
