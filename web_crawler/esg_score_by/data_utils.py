import os
import json


cur_dir = os.getcwd()

def issues_by_category(as_list: bool = False):
    path = cur_dir + "/data/reformulate/reformulate_theme.json"
    with open(path, "r") as file:
        issues = json.loads(file.read())

    if not as_list:
        return issues

    issue_list = []
    for issue in issues:
        for _issue in issues[issue]:
            issue_list.extend(issues[issue][_issue])
    return issue_list


def issues_as_list():
    return issues_by_category(as_list=True)


if __name__ == '__main__':
    issues = issues_as_list()
    print(issues)
    print(len(issues))
