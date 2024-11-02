## 功能 / Features 🛠️

- **任务分类 / Task Categorization**：支持将任务分为不同的类别，例如工作、个人等。Supports dividing tasks into different categories, such as Work, Personal, etc.
- **设置任务优先级 / Set Task Priority**：允许用户为任务设置优先级，例如高、中、低。Allows users to set priorities for tasks, such as High, Medium, Low.
- **提醒功能 / Reminder Function**：定时提醒用户完成任务。Provides timely reminders for completing tasks.
- **搜索任务 / Search Task**：允许用户通过关键词搜索任务。Allows users to search tasks via keywords.
- **导出任务 / Export Tasks**：将任务列表导出为 CSV 或其他格式的文件。Exports the task list as a CSV or other format file.

## 使用 / Usage 📝

### 添加任务 / Add Task 📃

```sh
python main.py add "完成报告" --category 工作 --priority 高 --due-date 2024-11-05
```

### 列出任务 / List Tasks 📚

```sh
python main.py list
```

### 完成任务 / Complete Task ✔️

```sh
python main.py complete 1
```

### 删除任务 / Delete Task ❌

```sh
python main.py delete 1
```

### 搜索任务 / Search Task 🔍

```sh
python main.py search 报告
```

### 导出任务 / Export Tasks 💾

```sh
python main.py export tasks.csv
```

### 设置提醒 / Set Reminder ⏰

```sh
python main.py reminder 1 60
```

### 示例 / Example 📘

```sh
python main.py add "完成报告" --category 工作 --priority 高 --due-date 2024-11-05
python main.py list
python main.py complete 1
python main.py delete 1
python main.py search 报告
python main.py export tasks.csv
```

## 贡献 / Contribution 🤝

欢迎提交 Issue 和 Pull Request！我会在有时间的情况下更新本项目的。

Welcome to submit Issues and Pull Requests! I will update this project when I have time.

## 许可证 / License 📜

本项目采用 MIT 许可证，详情参见 [LICENSE](LICENSE) 文件。

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for details.