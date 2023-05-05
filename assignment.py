import sys

class GraduationCeremony:
    def __init__(self, days):

        self.consecutive_days: int = 4 # number of consecutive days of attendance required
        self.days: int = days # number of days
        self.valid_ways: int = 0  # number of valid ways to attend classes
        self.invalid_ways: int = 0  # number of ways to miss last day
        
        # check for invalid input
        if self.days < self.consecutive_days or self.days < 0:
            raise Exception(f"Invalid input: {self.days}\nValid input: Enter 4 or greater than 4")
        
    def get_count_ways_to_attend_classes(self):
        days, consecutive_days = self.days, self.consecutive_days
        dp = [1] * (consecutive_days + 1)
        dp[consecutive_days] = 0

        for _ in range(1, days + 1):
            temp = [0] * (consecutive_days + 1)
            for j in range(consecutive_days - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            # update dp and temp arrays
            temp, dp = dp, temp

        
        self.valid_ways = dp[0] # total number of valid ways to attend classes
        self.invalid_ways = temp[1]  # total number of ways to miss the last day
        
        return self.valid_ways
    
    def get_probability_to_miss_ceremony(self):
        # calculate the probability of missing the ceremony
        return f"{self.invalid_ways}/{self.valid_ways}"
        
if __name__ == "__main__":
    try:
        while True:
            days = input("\nEnter the number of days or press enter to exit: ")
            if days:
                days = int(days)
                gcObj = GraduationCeremony(days)
                
                # Task 1: The number of ways to attend classes over N days.
                ways = gcObj.get_count_ways_to_attend_classes()
                print("*" * 70)
                print(f"Task 1. The number of ways to attend classes over {days} days: {ways}")

                # Task 2: The probability that you will miss your graduation ceremony.
                probability = gcObj.get_probability_to_miss_ceremony()
                print(f"Task 2. The probability that you will miss your graduation ceremony: {probability}")
                print("*" * 70)
            else:
                sys.exit(0)
    except Exception as e:
        print("Exception: ", e)
