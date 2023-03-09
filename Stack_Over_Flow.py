import requests
import time


class StackOverflow:
    def get_latest_questions(self):
        todate = int(time.time())
        fromdate = todate - 172800
        url = "https://api.stackexchange.com/2.3/questions?fromdate=" + f"{fromdate}" + "&todate=" + \
              f"{todate}" + "&order=desc&sort=creation&tagged=python&site=stackoverflow&filter=total"
        response = requests.get(url)
        print(f"За последние 2 дня было {response.json()['total']} вопросов, которые содержат тэг 'Python'")

if __name__ == '__main__':
    two_days_with_python = StackOverflow()
    two_days_with_python.get_latest_questions()
