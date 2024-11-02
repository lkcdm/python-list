import argparse
import os
import csv
from datetime import datetime, timedelta
import time

class Task:
    def __init__(self, description, category='个人', priority='中', due_date=None):
        self.description = description
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "已完成" if self.completed else "未完成"
        return f"{self.description} ({self.category}, {self.priority}, {self.due_date}, {status})"

def load_tasks():
    """加载列表"""
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                task = Task(row[0], row[1], row[2], row[3])
                task.completed = row[4] == 'True'
                tasks.append(task)
    return tasks

def save_tasks(tasks):
    """保存列表"""
    with open('tasks.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task.description, task.category, task.priority, task.due_date, task.completed])

def add_task(tasks, description, category, priority, due_date):
    """添加新任务"""
    task = Task(description, category, priority, due_date)
    tasks.append(task)
    print(f"任务 '{description}' 已添加。")

def list_tasks(tasks):
    """列出任务"""
    if not tasks:
        print("没有任务。")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_completed(tasks, index):
    """标记任务为已完成"""
    if 0 < index <= len(tasks):
        tasks[index - 1].mark_completed()
        print(f"任务 '{tasks[index - 1].description}' 已标记为已完成。")
    else:
        print("无效的任务编号。")

def delete_task(tasks, index):
    """删除任务"""
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"任务 '{removed.description}' 已删除。")
    else:
        print("无效的任务编号。")

def search_tasks(tasks, keyword):
    """搜索任务"""
    found_tasks = [task for task in tasks if keyword in task.description]
    if not found_tasks:
        print("没有找到匹配的任务。")
    else:
        for index, task in enumerate(found_tasks, start=1):
            print(f"{index}. {task}")

def export_tasks(tasks, filename):
    """导出任务列表"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["描述", "类别", "优先级", "截止日期", "状态"])
        for task in tasks:
            writer.writerow([task.description, task.category, task.priority, task.due_date, task.completed])
    print(f"任务已导出到 {filename}。")

def set_reminder(tasks, index, interval):
    """设置任务提醒"""
    if 0 < index <= len(tasks):
        task = tasks[index - 1]
        if not task.completed:
            print(f"任务 '{task.description}' 将在 {interval} 秒后提醒。")
            time.sleep(interval)
            print(f"提醒：任务 '{task.description}' 需要完成。")
        else:
            print("该任务已标记为已完成，无需提醒。")
    else:
        print("无效的任务编号。")

def main():
    parser = argparse.ArgumentParser(description="简易待办事项列表应用")
    subparsers = parser.add_subparsers(dest='command')

    # 添加
    add_parser = subparsers.add_parser('add', help='添加新任务')
    add_parser.add_argument('description', type=str, help='任务描述')
    add_parser.add_argument('--category', type=str, default='个人', help='任务类别')
    add_parser.add_argument('--priority', type=str, choices=['高', '中', '低'], default='中', help='任务优先级')
    add_parser.add_argument('--due-date', type=str, default=None, help='任务截止日期 (YYYY-MM-DD)')

    # 列出
    list_parser = subparsers.add_parser('list', help='列出所有任务')

    # 完成
    complete_parser = subparsers.add_parser('complete', help='标记任务为已完成')
    complete_parser.add_argument('index', type=int, help='要标记为已完成的任务编号')

    # 删除
    delete_parser = subparsers.add_parser('delete', help='删除任务')
    delete_parser.add_argument('index', type=int, help='要删除的任务编号')

    # 搜索
    search_parser = subparsers.add_parser('search', help='搜索任务')
    search_parser.add_argument('keyword', type=str, help='搜索关键词')

    # 导出
    export_parser = subparsers.add_parser('export', help='导出任务列表')
    export_parser.add_argument('filename', type=str, help='导出文件名')

    # 提醒
    reminder_parser = subparsers.add_parser('reminder', help='设置任务提醒')
    reminder_parser.add_argument('index', type=int, help='要设置提醒的任务编号')
    reminder_parser.add_argument('interval', type=int, help='提醒间隔（秒）')

    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == 'add':
        add_task(tasks, args.description, args.category, args.priority, args.due_date)
    elif args.command == 'list':
        list_tasks(tasks)
    elif args.command == 'complete':
        mark_completed(tasks, args.index)
    elif args.command == 'delete':
        delete_task(tasks, args.index)
    elif args.command == 'search':
        search_tasks(tasks, args.keyword)
    elif args.command == 'export':
        export_tasks(tasks, args.filename)
    elif args.command == 'reminder':
        set_reminder(tasks, args.index, args.interval)

    save_tasks(tasks)

if __name__ == "__main__":
    main()
